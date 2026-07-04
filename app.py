"""Веб-приложение для визуального обучения Python."""

import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from auth_routes import auth_bp
from config import Config
from data.guide_xml import LANDING_DEMO, STEP_CONNECT_DEMO
from data.registry import get_task_with_tests, get_tasks_public, get_topics
from data.topic_guides import get_topic_guide
from extensions import csrf, db, login_manager
from models import TaskProgress, User
from limits import init_rate_limiter, rate_limit_execution
from profile_routes import profile_bp
from progress_service import get_user_task_progress, maybe_record_check
from topic_unlock_service import assert_topic_unlocked, enrich_topics_for_user
from runner.checker import check_solution
from runner.debugger import debug_python_code
from runner.pool import init_execution_pool
from runner.python_to_blocks import python_to_blocks_safe
from runner.sandbox import run_python_code


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    init_execution_pool(
        config_class.MAX_CONCURRENT_EXECUTIONS,
        config_class.EXECUTION_QUEUE_TIMEOUT,
    )
    init_rate_limiter(
        config_class.EXECUTION_RATE_LIMIT,
        config_class.EXECUTION_RATE_WINDOW,
    )

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @login_manager.unauthorized_handler
    def handle_unauthorized():
        if request.path.startswith("/api/"):
            return jsonify({"error": "Требуется авторизация", "authenticated": False}), 401
        return redirect(url_for("auth.login", next=request.url))

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    @app.context_processor
    def inject_landing_demo():
        return {
            "landing_demo_xml": LANDING_DEMO,
            "step_connect_demo_xml": STEP_CONNECT_DEMO,
        }

    with app.app_context():
        db.create_all()
        _ensure_solution_xml_column()
        _normalize_existing_usernames()

    register_routes(app)
    return app


def _normalize_existing_usernames():
    """Привести существующие имена пользователей к нижнему регистру."""
    from sqlalchemy.exc import IntegrityError

    changed = False
    for user in User.query.all():
        normalized = user.username.strip().lower()
        if user.username == normalized:
            continue
        conflict = User.query.filter(
            User.username == normalized, User.id != user.id
        ).first()
        if conflict:
            continue
        user.username = normalized
        changed = True
    if not changed:
        return
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def _ensure_solution_xml_column():
    """Добавить solution_xml в существующую БД без миграций."""
    from sqlalchemy import inspect, text

    inspector = inspect(db.engine)
    if "task_progress" not in inspector.get_table_names():
        return
    columns = {col["name"] for col in inspector.get_columns("task_progress")}
    if "solution_xml" not in columns:
        db.session.execute(text("ALTER TABLE task_progress ADD COLUMN solution_xml TEXT"))
        db.session.commit()


def _execution_http_response(result: dict, *, ok_status: int = 200) -> tuple:
    """Ответ API выполнения с учётом перегрузки сервера."""
    if result.get("overloaded"):
        return jsonify(result), 503
    status = ok_status if result.get("success") else 400
    return jsonify(result), status


def register_routes(app):
    @app.route("/")
    def landing():
        return render_template(
            "landing.html",
            landing_demo_xml=LANDING_DEMO,
            step_connect_demo_xml=STEP_CONNECT_DEMO,
        )

    @app.route("/learn")
    def learn():
        return render_template("index.html")

    @app.route("/api/run", methods=["POST"])
    @rate_limit_execution()
    def run_code():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        stdin_text = data.get("stdin", "")

        if not code.strip():
            return jsonify({"success": False, "output": "", "error": "Код пуст"}), 400

        result = run_python_code(code, stdin_text=stdin_text)
        return _execution_http_response(result)

    @app.route("/api/debug", methods=["POST"])
    @rate_limit_execution()
    def debug_code():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        stdin_text = data.get("stdin", "")

        if not code.strip():
            return jsonify({"success": False, "steps": [], "error": "Код пуст"}), 400

        result = debug_python_code(code, stdin_text=stdin_text)
        return _execution_http_response(result)

    @app.route("/api/python-to-blocks", methods=["POST"])
    def python_to_blocks_api():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        if not isinstance(code, str):
            return jsonify({"success": False, "error": "Некорректный запрос"}), 400
        result = python_to_blocks_safe(code)
        status = 200 if result.get("success") else 400
        return jsonify(result), status

    @app.route("/api/topics", methods=["GET"])
    @login_required
    def list_topics():
        return jsonify({"topics": enrich_topics_for_user(current_user)})

    @app.route("/api/topics/<topic_id>/tasks", methods=["GET"])
    @login_required
    def list_tasks(topic_id):
        if topic_id not in {t["id"] for t in get_topics()}:
            return jsonify({"error": "Тема не найдена"}), 404
        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify({"error": locked["unlock_hint"], "locked": True, **locked}), 403
        return jsonify({"tasks": get_tasks_public(topic_id)})

    @app.route("/api/topics/<topic_id>/guide", methods=["GET"])
    @login_required
    def topic_guide(topic_id):
        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify({"error": locked["unlock_hint"], "locked": True, **locked}), 403
        guide = get_topic_guide(topic_id)
        if not guide:
            return jsonify({"error": "Материалы по теме не найдены"}), 404
        return jsonify({"guide": guide})

    @app.route("/api/check", methods=["POST"])
    @login_required
    @rate_limit_execution()
    def check_task():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        topic_id = data.get("topic_id", "")
        task_id = data.get("task_id", "")
        blocks_xml = data.get("blocks_xml", "")

        if not code.strip():
            return jsonify({"success": False, "message": "Сначала соберите программу из блоков"}), 400

        task = get_task_with_tests(topic_id, task_id)
        if not task:
            return jsonify({"success": False, "message": "Задача не найдена"}), 404

        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify(
                {"success": False, "message": locked["unlock_hint"], "locked": True, **locked}
            ), 403

        result = check_solution(code, task.get("tests", []))
        if result.get("overloaded"):
            return jsonify(
                {
                    "success": False,
                    "message": result.get("message", "Сервер перегружен"),
                    "overloaded": True,
                }
            ), 503

        progress_info = maybe_record_check(
            topic_id,
            task_id,
            code,
            result["success"],
            blocks_xml if isinstance(blocks_xml, str) and blocks_xml.strip() else None,
        )
        if progress_info:
            result["progress"] = progress_info

        status = 200 if result["success"] else 400
        return jsonify(result), status

    @app.route("/api/progress/<topic_id>/<task_id>", methods=["GET"])
    @login_required
    def get_task_progress(topic_id, task_id):
        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify({"error": locked["unlock_hint"], "locked": True, **locked}), 403

        progress = get_user_task_progress(current_user, topic_id, task_id)
        if not progress:
            return jsonify(
                {
                    "has_solution": False,
                    "completed": False,
                    "attempts_count": 0,
                    "solution_xml": None,
                    "solution_code": None,
                }
            )
        return jsonify(
            {
                "has_solution": bool(progress.solution_xml or progress.solution_code),
                "completed": progress.completed,
                "attempts_count": progress.attempts_count,
                "solution_xml": progress.solution_xml,
                "solution_code": progress.solution_code,
            }
        )

    @app.route("/api/me", methods=["GET"])
    def current_user_info():
        if not current_user.is_authenticated:
            return jsonify({"authenticated": False})
        return jsonify(
            {
                "authenticated": True,
                "username": current_user.username,
                "profile_url": "/profile/",
            }
        )


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

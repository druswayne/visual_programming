"""Веб-приложение для визуального обучения Python."""

import os

from flask import Flask, jsonify, redirect, render_template, request, url_for, make_response
from flask_login import current_user, login_required

from auth_routes import auth_bp
from config import Config
from data.guide_xml import (
    LANDING_DEMO,
    LANDING_DEMO_EN,
    STEP_CONNECT_DEMO,
    STEP_CONNECT_DEMO_EN,
)
from data.registry import TASKS_BY_TOPIC, get_task_with_tests, get_topics
from data.localized import get_localized_sandbox_demo, get_localized_topic_guide, get_localized_topics
from data.sandbox_demos import (
    LANDING_TOPIC_META,
    get_sandbox_demo,
)
from extensions import csrf, db, login_manager
from i18n import (
    SUPPORTED_LOCALES,
    _,
    get_block_messages,
    get_blockly_msg_file,
    get_js_messages,
    get_locale,
    get_pyblocks_locale_file,
    ngettext,
    set_request_locale,
)
from models import TaskProgress, User
from limits import init_rate_limiter, rate_limit_execution
from leaderboard_routes import leaderboard_bp
from profile_routes import profile_bp
from progress_service import get_user_task_progress, maybe_record_check
from sandbox_saves_service import (
    MAX_SAVES_PER_USER,
    create_user_save,
    delete_user_save,
    get_user_save,
    list_user_saves,
    update_user_save,
)
from topic_unlock_service import assert_topic_unlocked, enrich_tasks_for_user, enrich_topics_for_user
from runner.checker import check_solution, strip_input_prompts
from runner.debugger import debug_python_code
from runner.pool import init_execution_pool
from runner.python_to_blocks import python_to_blocks_safe
from runner.sandbox import run_python_code


def _strip_run_output(code: str, result: dict) -> dict:
    """Убирает подсказки input() из stdout — они уже показаны в модальном окне."""
    result = {**result}
    if result.get("output"):
        result["output"] = strip_input_prompts(code, result["output"])
    steps = result.get("steps")
    if steps:
        cleaned = []
        for step in steps:
            if step.get("output"):
                step = {**step, "output": strip_input_prompts(code, step["output"])}
            cleaned.append(step)
        result["steps"] = cleaned
    return result


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
            return jsonify({"error": _("api.auth_required"), "authenticated": False}), 401
        return redirect(url_for("auth.login", next=request.url))

    @app.before_request
    def before_request():
        set_request_locale()
        login_manager.login_message = _("flash.login_required")

    @app.context_processor
    def inject_i18n():
        locale = get_locale()
        landing_xml = LANDING_DEMO_EN if locale == "en" else LANDING_DEMO
        step_xml = STEP_CONNECT_DEMO_EN if locale == "en" else STEP_CONNECT_DEMO
        return {
            "landing_demo_xml": landing_xml,
            "step_connect_demo_xml": step_xml,
            "_": _,
            "ngettext": ngettext,
            "get_locale": get_locale,
            "supported_locales": SUPPORTED_LOCALES,
            "locale_names": Config.LANGUAGES,
            "js_messages": get_js_messages(locale),
            "block_messages": get_block_messages(locale),
            "blockly_msg_file": get_blockly_msg_file(locale),
            "pyblocks_locale_file": get_pyblocks_locale_file(locale),
        }

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(leaderboard_bp)

    with app.app_context():
        db.create_all()
        _ensure_solution_xml_column()
        _normalize_existing_usernames()
        _ensure_admin_user()

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


def _ensure_admin_user():
    """Создать admin/admin123 со всеми темами открытыми и пройденными."""
    from datetime import datetime, timezone

    from flask import current_app

    from skills_service import ensure_skills_synced

    admin = User.query.filter_by(username="admin").first()
    changed = False
    if not admin:
        admin = User(username="admin", email="admin@pyblocks.local")
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.flush()
        changed = True

    by_key = {
        (row.topic_id, row.task_id): row
        for row in TaskProgress.query.filter_by(user_id=admin.id).all()
    }
    now = datetime.now(timezone.utc)
    for topic_id, tasks in TASKS_BY_TOPIC.items():
        for task in tasks:
            task_id = task["id"]
            progress = by_key.get((topic_id, task_id))
            if progress is None:
                db.session.add(
                    TaskProgress(
                        user_id=admin.id,
                        topic_id=topic_id,
                        task_id=task_id,
                        completed=True,
                        attempts_count=1,
                        completed_at=now,
                    )
                )
                changed = True
            elif not progress.completed:
                progress.completed = True
                progress.completed_at = progress.completed_at or now
                progress.attempts_count = max(progress.attempts_count or 0, 1)
                changed = True

    if changed:
        db.session.commit()

    with current_app.test_request_context():
        ensure_skills_synced(admin.id)


def _execution_http_response(result: dict, *, ok_status: int = 200) -> tuple:
    """Ответ API выполнения с учётом перегрузки сервера."""
    if result.get("overloaded"):
        return jsonify(result), 503
    status = ok_status if result.get("success") else 400
    return jsonify(result), status


def _landing_topics():
    topics = []
    for topic in get_localized_topics():
        topics.append(
            {
                **topic,
                "task_count": len(TASKS_BY_TOPIC.get(topic["id"], [])),
                "icon": topic.get("icon", "📘"),
                "level": topic.get("level", ""),
                "highlight": topic.get("highlight", False),
            }
        )
    return topics


def register_routes(app):
    @app.route("/set-language/<lang>")
    def set_language(lang):
        from i18n import LOCALE_COOKIE, LOCALE_COOKIE_MAX_AGE, normalize_locale

        locale = normalize_locale(lang)
        next_url = request.args.get("next") or request.referrer or url_for("landing")
        if not next_url.startswith("/"):
            next_url = url_for("landing")
        response = make_response(redirect(next_url))
        response.set_cookie(LOCALE_COOKIE, locale, max_age=LOCALE_COOKIE_MAX_AGE, samesite="Lax")
        return response

    @app.route("/")
    def landing():
        locale = get_locale()
        landing_xml = LANDING_DEMO_EN if locale == "en" else LANDING_DEMO
        step_xml = STEP_CONNECT_DEMO_EN if locale == "en" else STEP_CONNECT_DEMO
        return render_template(
            "landing.html",
            landing_demo_xml=landing_xml,
            step_connect_demo_xml=step_xml,
            landing_topics=_landing_topics(),
        )

    @app.route("/learn")
    def learn():
        return render_template("index.html")

    @app.route("/privacy")
    def privacy():
        return render_template("privacy.html")

    @app.route("/api/sandbox-demo/<demo_id>", methods=["GET"])
    def sandbox_demo(demo_id):
        demo = get_localized_sandbox_demo(demo_id)
        if not demo:
            return jsonify({"success": False, "error": _("api.demo_not_found")}), 404
        return jsonify(
            {
                "success": True,
                "id": demo["id"],
                "title": demo["title"],
                "description": demo["description"],
                "xml": demo["xml"],
            }
        )

    @app.route("/api/run", methods=["POST"])
    @rate_limit_execution()
    def run_code():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        stdin_text = data.get("stdin", "")

        if not code.strip():
            return jsonify({"success": False, "output": "", "error": _("api.code_empty")}), 400

        result = _strip_run_output(code, run_python_code(code, stdin_text=stdin_text))
        return _execution_http_response(result)

    @app.route("/api/debug", methods=["POST"])
    @rate_limit_execution()
    def debug_code():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        stdin_text = data.get("stdin", "")

        if not code.strip():
            return jsonify({"success": False, "steps": [], "error": "Код пуст"}), 400

        result = _strip_run_output(code, debug_python_code(code, stdin_text=stdin_text))
        return _execution_http_response(result)

    @app.route("/api/python-to-blocks", methods=["POST"])
    def python_to_blocks_api():
        data = request.get_json(silent=True) or {}
        code = data.get("code", "")
        if not isinstance(code, str):
            return jsonify({"success": False, "error": _("api.bad_request")}), 400
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
            return jsonify({"error": _("api.topic_not_found")}), 404
        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify({"error": locked["unlock_hint"], "locked": True, **locked}), 403
        return jsonify({"tasks": enrich_tasks_for_user(current_user, topic_id)})

    @app.route("/api/topics/<topic_id>/guide", methods=["GET"])
    @login_required
    def topic_guide(topic_id):
        locked = assert_topic_unlocked(current_user.id, topic_id)
        if locked:
            return jsonify({"error": locked["unlock_hint"], "locked": True, **locked}), 403
        guide = get_localized_topic_guide(topic_id)
        if not guide:
            return jsonify({"error": _("api.guide_not_found")}), 404
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
            return jsonify({"success": False, "message": _("api.build_program_first")}), 400

        task = get_task_with_tests(topic_id, task_id)
        if not task:
            return jsonify({"success": False, "message": _("api.task_not_found")}), 404

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
                    "message": result.get("message", _("api.server_busy")),
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

    def _sandbox_save_error_response(errors: list[str]):
        code = errors[0] if errors else "invalid"
        messages = {
            "title_required": _("sandbox_saves.error_title_required"),
            "blocks_required": _("sandbox_saves.error_blocks_required"),
            "blocks_too_large": _("sandbox_saves.error_blocks_too_large"),
            "code_too_large": _("sandbox_saves.error_code_too_large"),
            "limit_reached": _("sandbox_saves.error_limit", limit=MAX_SAVES_PER_USER),
            "not_found": _("sandbox_saves.error_not_found"),
        }
        status = 404 if code == "not_found" else 400
        return jsonify({"success": False, "error": messages.get(code, code), "code": code}), status

    @app.route("/api/sandbox/saves", methods=["GET"])
    @login_required
    def sandbox_saves_list():
        saves = list_user_saves(current_user)
        return jsonify(
            {
                "success": True,
                "saves": [s.to_summary_dict() for s in saves],
                "limit": MAX_SAVES_PER_USER,
                "count": len(saves),
            }
        )

    @app.route("/api/sandbox/saves", methods=["POST"])
    @login_required
    def sandbox_saves_create():
        data = request.get_json(silent=True) or {}
        save, errors = create_user_save(
            current_user,
            data.get("title"),
            data.get("blocks_xml"),
            data.get("code"),
        )
        if errors:
            return _sandbox_save_error_response(errors)
        return jsonify({"success": True, "save": save.to_detail_dict()}), 201

    @app.route("/api/sandbox/saves/<int:save_id>", methods=["GET"])
    @login_required
    def sandbox_saves_get(save_id):
        save = get_user_save(current_user, save_id)
        if not save:
            return _sandbox_save_error_response(["not_found"])
        return jsonify({"success": True, "save": save.to_detail_dict()})

    @app.route("/api/sandbox/saves/<int:save_id>", methods=["PUT"])
    @login_required
    def sandbox_saves_update(save_id):
        data = request.get_json(silent=True) or {}
        save, errors = update_user_save(
            current_user,
            save_id,
            title=data.get("title"),
            blocks_xml=data.get("blocks_xml"),
            code=data.get("code"),
        )
        if errors:
            return _sandbox_save_error_response(errors)
        return jsonify({"success": True, "save": save.to_detail_dict()})

    @app.route("/api/sandbox/saves/<int:save_id>", methods=["DELETE"])
    @login_required
    def sandbox_saves_delete(save_id):
        if not delete_user_save(current_user, save_id):
            return _sandbox_save_error_response(["not_found"])
        return jsonify({"success": True})

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
    app.run(debug=True, port=5002)

"""Тесты рейтинга пользователей."""

import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from app import create_app
from config import Config
from extensions import db
from leaderboard_service import build_leaderboard
from models import TaskProgress, User


def _make_app(db_dir: str):
    class TestConfig(Config):
        TESTING = True
        WTF_CSRF_ENABLED = False
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(Path(db_dir) / "leaderboard.db")

    return create_app(TestConfig)


def _user(name: str) -> User:
    user = User(username=name, email=f"{name}@example.com")
    user.set_password("password1")
    db.session.add(user)
    db.session.flush()
    return user


def _solve(user: User, task_id: str, attempts: int = 1, when: datetime | None = None, topic_id: str = "io"):
    db.session.add(
        TaskProgress(
            user_id=user.id,
            topic_id=topic_id,
            task_id=task_id,
            completed=True,
            attempts_count=attempts,
            completed_at=when or datetime.now(timezone.utc),
        )
    )


def _with_app(callback):
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        app = _make_app(tmp)
        try:
            with app.app_context():
                callback(app)
        finally:
            with app.app_context():
                db.session.remove()
                db.engine.dispose()


def test_ranking_rewards_volume_and_first_try():
    def run(_app):
        precise = _user("precise")
        busy = _user("busybee")
        starter = _user("starter")
        now = datetime.now(timezone.utc)

        for idx in range(1, 6):
            _solve(precise, f"io-0{idx}", attempts=1, when=now)
        for idx in range(1, 6):
            _solve(busy, f"io-0{idx}", attempts=4, when=now)
        _solve(starter, "io-01", attempts=1, when=now)
        db.session.commit()

        data = build_leaderboard()
        names = [row["username"] for row in data["rows"]]
        assert names[:3] == ["precise", "busybee", "starter"]
        assert "admin" not in names

        by_name = {row["username"]: row for row in data["rows"]}
        assert by_name["precise"]["first_try"] == 5
        assert by_name["precise"]["accuracy"] == 100
        assert by_name["busybee"]["accuracy"] == 0
        assert by_name["precise"]["score"] > by_name["busybee"]["score"]

    _with_app(run)


def test_accuracy_sort_requires_minimum_solved():
    def run(_app):
        lucky = _user("lucky")
        steady = _user("steady")
        now = datetime.now(timezone.utc)
        _solve(lucky, "io-01", attempts=1, when=now)
        for idx in range(1, 6):
            _solve(steady, f"io-0{idx}", attempts=1 if idx < 5 else 3, when=now)
        db.session.commit()

        data = build_leaderboard(sort="accuracy")
        assert data["rows"][0]["username"] == "steady"
        assert data["rows"][1]["username"] == "lucky"

    _with_app(run)


def test_period_filter_hides_old_solves():
    def run(_app):
        oldie = _user("oldie")
        newbie = _user("newbie")
        old = datetime.now(timezone.utc) - timedelta(days=20)
        recent = datetime.now(timezone.utc) - timedelta(days=1)
        for idx in range(1, 4):
            _solve(oldie, f"io-0{idx}", attempts=1, when=old)
        _solve(newbie, "io-01", attempts=1, when=recent)
        db.session.commit()

        week = build_leaderboard(period="week")
        week_names = [row["username"] for row in week["rows"]]
        assert week_names == ["newbie"]

        all_time = build_leaderboard(period="all")
        assert [row["username"] for row in all_time["rows"]][:2] == ["oldie", "newbie"]

    _with_app(run)


def test_current_user_rank_and_page():
    def run(app):
        alpha = _user("alpha")
        beta = _user("beta")
        now = datetime.now(timezone.utc)
        for idx in range(1, 4):
            _solve(alpha, f"io-0{idx}", attempts=1, when=now)
        _solve(beta, "io-01", attempts=1, when=now)
        db.session.commit()

        data = build_leaderboard(current_user_id=beta.id)
        assert data["me"]["rank"] == 2
        assert data["me"]["chase"]["username"] == "alpha"

        client = app.test_client()
        response = client.get("/leaderboard")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "alpha" in html
        assert "beta" in html
        assert "Кто сейчас впереди" in html
        assert "leaderboard.js" in html

    _with_app(run)


def test_hides_internal_test_accounts():
    def run(_app):
        real = _user("simon")
        unlock = _user("__unlock_test__")
        xp = _user("_xp_test_")
        now = datetime.now(timezone.utc)
        for idx in range(1, 6):
            _solve(unlock, f"io-0{idx}", attempts=1, when=now)
            _solve(xp, f"io-0{idx}", attempts=1, when=now)
        _solve(real, "io-01", attempts=1, when=now)
        db.session.commit()

        data = build_leaderboard()
        names = [row["username"] for row in data["rows"]]
        highlight_names = [item["username"] for item in data["highlights"]]
        assert names == ["simon"]
        assert "__unlock_test__" not in names
        assert "_xp_test_" not in names
        assert "simon" in highlight_names
        assert "__unlock_test__" not in highlight_names
        assert "_xp_test_" not in highlight_names

    _with_app(run)


def test_game_missions_count_in_ranking():
    def run(_app):
        only_tasks = _user("tasker")
        gamer = _user("gamer")
        now = datetime.now(timezone.utc)
        _solve(only_tasks, "io-01", attempts=1, when=now)
        _solve(gamer, "walk_3", attempts=1, when=now, topic_id="game_linear")
        db.session.commit()

        data = build_leaderboard()
        by_name = {row["username"]: row for row in data["rows"]}
        assert by_name["gamer"]["solved"] == 1
        assert by_name["tasker"]["solved"] == 1
        assert by_name["gamer"]["score"] == by_name["tasker"]["score"]
        assert by_name["gamer"]["first_try"] == 1

    _with_app(run)


if __name__ == "__main__":
    test_ranking_rewards_volume_and_first_try()
    test_accuracy_sort_requires_minimum_solved()
    test_period_filter_hides_old_solves()
    test_current_user_rank_and_page()
    test_hides_internal_test_accounts()
    test_game_missions_count_in_ranking()
    print("OK")

"""Тесты разблокировки тем."""

from app import create_app
from extensions import db
from models import TaskProgress, User
from topic_unlock_service import (
    is_topic_unlocked,
    required_completed_count,
    get_unlock_info,
)


def test_required_completed_count():
    assert required_completed_count(35) == 18
    assert required_completed_count(10) == 5
    assert required_completed_count(1) == 1


def test_topic_unlock_chain():
    app = create_app()
    with app.app_context():
        db.create_all()
        u = User.query.filter_by(username="__unlock_test__").first()
        if not u:
            u = User(username="__unlock_test__", email="unlock@test.local")
            u.set_password("test")
            db.session.add(u)
            db.session.commit()

        TaskProgress.query.filter_by(user_id=u.id).delete()
        db.session.commit()

        assert is_topic_unlocked(u.id, "io") is True
        assert is_topic_unlocked(u.id, "numbers") is False

        for i in range(18):
            db.session.add(
                TaskProgress(
                    user_id=u.id,
                    topic_id="io",
                    task_id=f"io-{i:02d}",
                    completed=True,
                    attempts_count=1,
                )
            )
        db.session.commit()

        assert is_topic_unlocked(u.id, "numbers") is True
        info = get_unlock_info(u.id, "conditions")
        assert info["unlocked"] is False
        assert info["requires_topic_id"] == "numbers"


if __name__ == "__main__":
    test_required_completed_count()
    test_topic_unlock_chain()
    print("OK")

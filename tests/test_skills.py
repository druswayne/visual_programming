"""Тесты сохранения XP в БД."""

from app import create_app
from extensions import db
from models import SkillBranchXp, SkillXpAward, TaskProgress, User
from progress_service import record_task_check
from skills_service import build_skills_profile


def test_xp_persisted_once():
    app = create_app()
    with app.app_context():
        db.create_all()
        u = User.query.filter_by(username="__xp_test__").first()
        if not u:
            u = User(username="__xp_test__", email="xp@test.local")
            u.set_password("test")
            db.session.add(u)
            db.session.commit()

        SkillXpAward.query.filter_by(user_id=u.id).delete()
        SkillBranchXp.query.filter_by(user_id=u.id).delete()
        TaskProgress.query.filter_by(user_id=u.id).delete()
        db.session.commit()

        record_task_check(u, "io", "io-01", 'print("Привет, мир!")', True)
        skills = build_skills_profile(u.id)
        assert skills["total_xp"] > 0
        assert SkillXpAward.query.filter_by(user_id=u.id).count() == 1
        io_branch = next(b for b in skills["branches"] if b["id"] == "io")
        assert io_branch["completed_count"] == 1
        assert io_branch["xp"] > 0

        xp_before = skills["total_xp"]
        record_task_check(u, "io", "io-01", 'print("Привет, мир!")', True)
        skills_after = build_skills_profile(u.id)
        assert skills_after["total_xp"] == xp_before
        assert SkillXpAward.query.filter_by(user_id=u.id).count() == 1


def test_topic_unlock_chain():
    app = create_app()
    with app.app_context():
        skills = build_skills_profile(-1)
        assert len(skills["branches"]) == 7
        assert skills["branches"][0]["id"] == "io"
        assert skills["branches"][2]["id"] == "conditions"
        assert skills["branches"][2]["locked"] is True


if __name__ == "__main__":
    test_xp_persisted_once()
    test_topic_unlock_chain()
    print("OK")

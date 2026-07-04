"""Сохранение попыток и прогресса пользователя."""

from flask_login import current_user

from extensions import db
from models import TaskAttempt, TaskProgress
from skills_service import award_task_skills_xp


def record_task_check(
    user,
    topic_id: str,
    task_id: str,
    code: str,
    success: bool,
    blocks_xml: str | None = None,
) -> dict:
    """Записать попытку проверки задачи и обновить прогресс."""
    attempt = TaskAttempt(
        user_id=user.id,
        topic_id=topic_id,
        task_id=task_id,
        code=code,
        success=success,
    )
    db.session.add(attempt)

    progress = TaskProgress.query.filter_by(
        user_id=user.id,
        topic_id=topic_id,
        task_id=task_id,
    ).first()

    if not progress:
        progress = TaskProgress(
            user_id=user.id,
            topic_id=topic_id,
            task_id=task_id,
            attempts_count=0,
            completed=False,
        )
        db.session.add(progress)

    was_completed = progress.completed
    progress.record_attempt(success, code, blocks_xml)

    xp_awarded = None
    if success and not was_completed and progress.completed:
        xp_awarded = award_task_skills_xp(
            user.id,
            topic_id,
            task_id,
            progress.attempts_count,
        )

    db.session.commit()

    result = {
        "attempts_count": progress.attempts_count,
        "completed": progress.completed,
        "has_blocks": bool(progress.solution_xml),
    }
    if xp_awarded:
        result["xp_awarded"] = sum(xp_awarded.xp_by_branch.values())
    return result


def maybe_record_check(
    topic_id: str,
    task_id: str,
    code: str,
    success: bool,
    blocks_xml: str | None = None,
) -> dict | None:
    """Записать попытку, если пользователь авторизован."""
    if not current_user.is_authenticated:
        return None
    return record_task_check(current_user, topic_id, task_id, code, success, blocks_xml)


def get_user_task_progress(user, topic_id: str, task_id: str) -> TaskProgress | None:
    return TaskProgress.query.filter_by(
        user_id=user.id,
        topic_id=topic_id,
        task_id=task_id,
    ).first()

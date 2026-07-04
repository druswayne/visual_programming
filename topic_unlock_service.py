"""Разблокировка тем: следующая тема открывается после 50% задач предыдущей."""

from __future__ import annotations

from data.registry import get_tasks_public, get_topics
from data.skills_config import TOPIC_ORDER
from i18n import _
from models import TaskProgress

TOPIC_UNLOCK_PERCENT = 50


def get_previous_topic_id(topic_id: str) -> str | None:
    try:
        index = TOPIC_ORDER.index(topic_id)
    except ValueError:
        return None
    if index <= 0:
        return None
    return TOPIC_ORDER[index - 1]


def required_completed_count(total: int) -> int:
    """Сколько задач нужно решить (50% предыдущей темы, округление вверх)."""
    if total <= 0:
        return 0
    return (total + 1) // 2


def get_topic_completion(user_id: int, topic_id: str) -> dict:
    total = len(get_tasks_public(topic_id))
    if total == 0:
        return {"completed": 0, "total": 0, "percent": 100}

    completed = TaskProgress.query.filter_by(
        user_id=user_id,
        topic_id=topic_id,
        completed=True,
    ).count()
    percent = round(completed / total * 100)
    return {"completed": completed, "total": total, "percent": percent}


def is_topic_unlocked(user_id: int, topic_id: str) -> bool:
    previous_id = get_previous_topic_id(topic_id)
    if not previous_id:
        return True

    previous = get_topic_completion(user_id, previous_id)
    if previous["total"] == 0:
        return True

    required = required_completed_count(previous["total"])
    return previous["completed"] >= required


def get_unlock_info(user_id: int, topic_id: str) -> dict:
    previous_id = get_previous_topic_id(topic_id)
    if not previous_id:
        return {
            "unlocked": True,
            "requires_topic_id": None,
            "requires_topic_title": None,
            "required_completed": 0,
            "previous_completed": 0,
            "previous_total": 0,
            "unlock_hint": None,
        }

    titles = {topic["id"]: topic["title"] for topic in get_topics()}
    previous = get_topic_completion(user_id, previous_id)
    required = required_completed_count(previous["total"])
    unlocked = previous["completed"] >= required
    prev_title = titles.get(previous_id, previous_id)

    return {
        "unlocked": unlocked,
        "requires_topic_id": previous_id,
        "requires_topic_title": prev_title,
        "required_completed": required,
        "previous_completed": previous["completed"],
        "previous_total": previous["total"],
        "unlock_hint": (
            None
            if unlocked
            else _(
                "api.unlock_hint",
                remaining=max(0, required - previous["completed"]),
                total=previous["total"],
                topic=prev_title,
                percent=TOPIC_UNLOCK_PERCENT,
            )
        ),
    }


def enrich_topics_for_user(user) -> list[dict]:
    topics = []
    for topic in get_topics():
        unlock = get_unlock_info(user.id, topic["id"])
        completion = get_topic_completion(user.id, topic["id"])
        topics.append(
            {
                **topic,
                **unlock,
                "completed_count": completion["completed"],
                "total_tasks": completion["total"],
                "topic_percent": completion["percent"],
            }
        )
    return topics


def assert_topic_unlocked(user_id: int, topic_id: str) -> dict | None:
    """Вернуть unlock_info, если тема закрыта (для ответа API 403)."""
    if is_topic_unlocked(user_id, topic_id):
        return None
    return get_unlock_info(user_id, topic_id)

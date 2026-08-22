"""Разблокировка линеек игрового режима (отдельно от курса Python)."""

from __future__ import annotations

from i18n import _
from models import TaskProgress

TRACK_ORDER = ("linear", "conditions", "loops")
TRACK_TOPIC_IDS = {
    "linear": "game_linear",
    "conditions": "game_if",
    "loops": "game_loops",
}
TOPIC_TO_TRACK = {value: key for key, value in TRACK_TOPIC_IDS.items()}
UNLOCK_PERCENT = 50


def topic_id_for_track(track_id: str) -> str:
    return TRACK_TOPIC_IDS[track_id]


def previous_track_id(track_id: str) -> str | None:
    try:
        index = TRACK_ORDER.index(track_id)
    except ValueError:
        return None
    if index <= 0:
        return None
    return TRACK_ORDER[index - 1]


def required_completed_count(total: int) -> int:
    if total <= 0:
        return 0
    return (total + 1) // 2


def track_completion(user_id: int, track_id: str, total: int) -> dict:
    topic_id = topic_id_for_track(track_id)
    if total <= 0:
        return {"completed": 0, "total": 0, "percent": 100}
    completed = TaskProgress.query.filter_by(
        user_id=user_id,
        topic_id=topic_id,
        completed=True,
    ).count()
    percent = round(completed / total * 100) if total else 100
    return {"completed": completed, "total": total, "percent": percent}


def is_track_unlocked(user_id: int | None, track_id: str, totals: dict[str, int]) -> bool:
    if user_id is None:
        return True
    previous = previous_track_id(track_id)
    if not previous:
        return True
    total = totals.get(previous, 0)
    if total <= 0:
        return True
    stats = track_completion(user_id, previous, total)
    return stats["completed"] >= required_completed_count(total)


def get_unlock_info(user_id: int | None, track_id: str, totals: dict[str, int], titles: dict[str, str]) -> dict:
    previous = previous_track_id(track_id)
    unlocked = is_track_unlocked(user_id, track_id, totals)
    if not previous:
        return {
            "unlocked": True,
            "requires_track_id": None,
            "requires_track_title": None,
            "required_completed": 0,
            "unlock_hint": None,
        }
    total = totals.get(previous, 0)
    required = required_completed_count(total)
    title = titles.get(previous, previous)
    hint = None
    if not unlocked:
        hint = _("game.unlock_hint", title=title, count=required)
    return {
        "unlocked": unlocked,
        "requires_track_id": previous,
        "requires_track_title": title,
        "required_completed": required,
        "unlock_hint": hint,
    }

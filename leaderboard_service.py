"""Рейтинг пользователей: объём решений + качество (с первой попытки)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from math import ceil

from sqlalchemy import case, func

from data.registry import TASKS_BY_TOPIC
from extensions import db
from models import SkillXpAward, TaskProgress, User

TOP_LIMIT = 50
MIN_ACCURACY_SOLVED = 5
EXCLUDED_USERNAMES = frozenset({"admin"})

SCORE_SOLVED = 150
SCORE_FIRST_TRY = 35
SCORE_TOPIC = 200

SORTS = ("score", "solved", "accuracy", "xp")
PERIODS = ("all", "week", "month")

TITLES = (
    (80, "legend", "👑"),
    (50, "master", "🏆"),
    (30, "adept", "⭐"),
    (15, "coder", "💻"),
    (5, "apprentice", "📘"),
    (1, "rookie", "🌱"),
)

_TOPIC_TOTALS = {tid: len(tasks) for tid, tasks in TASKS_BY_TOPIC.items()}


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _aware(value: datetime | None) -> datetime | None:
    if value is None:
        return None
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


def _period_start(period: str) -> datetime | None:
    now = _utcnow()
    if period == "week":
        return now - timedelta(days=7)
    if period == "month":
        return now - timedelta(days=30)
    return None


def _title_for(solved: int) -> dict:
    for threshold, key, icon in TITLES:
        if solved >= threshold:
            return {"key": key, "icon": icon}
    return {"key": "spectator", "icon": "👀"}


def _avatar_hue(username: str) -> int:
    return sum(ord(ch) for ch in username) % 360


def _activity_key(last_solved: datetime | None) -> str | None:
    last = _aware(last_solved)
    if last is None:
        return None
    age = _utcnow() - last
    if age <= timedelta(hours=24):
        return "today"
    if age <= timedelta(days=7):
        return "week"
    return None


def _compute_score(solved: int, first_try: int, topics_mastered: int, xp: int) -> int:
    return (
        solved * SCORE_SOLVED
        + first_try * SCORE_FIRST_TRY
        + topics_mastered * SCORE_TOPIC
        + max(0, xp)
    )


def _badges_for(solved: int, first_try: int, accuracy: int, topics_mastered: int) -> list[str]:
    badges: list[str] = []
    if solved >= MIN_ACCURACY_SOLVED and accuracy >= 80:
        badges.append("sniper")
    if first_try >= 8:
        badges.append("spark")
    if topics_mastered >= 1:
        badges.append("closer")
    return badges


def _highlights(ranked: list[dict]) -> list[dict]:
    if not ranked:
        return []
    items: list[dict] = []
    qualified = [row for row in ranked if row["solved"] >= MIN_ACCURACY_SOLVED]
    if qualified:
        sniper = max(qualified, key=lambda row: (row["accuracy"], row["first_try"], row["solved"]))
        items.append(
            {
                "kind": "sniper",
                "username": sniper["username"],
                "hue": sniper["hue"],
                "initial": sniper["initial"],
                "value": f"{sniper['accuracy']}%",
            }
        )
    volume = max(ranked, key=lambda row: (row["solved"], row["score"]))
    items.append(
        {
            "kind": "volume",
            "username": volume["username"],
            "hue": volume["hue"],
            "initial": volume["initial"],
            "value": str(volume["solved"]),
        }
    )
    hot = next((row for row in ranked if row["activity"] == "today"), None)
    if hot:
        items.append(
            {
                "kind": "hot",
                "username": hot["username"],
                "hue": hot["hue"],
                "initial": hot["initial"],
                "value": None,
            }
        )
    return items[:3]


def _sort_key(row: dict, sort: str) -> tuple:
    if sort == "solved":
        return (row["solved"], row["score"], row["first_try"], row["xp"])
    if sort == "accuracy":
        qualified = 1 if row["solved"] >= MIN_ACCURACY_SOLVED else 0
        return (qualified, row["accuracy"], row["solved"], row["score"])
    if sort == "xp":
        return (row["xp"], row["score"], row["solved"])
    return (row["score"], row["solved"], row["first_try"], row["xp"])


def _load_xp_by_user(since: datetime | None) -> dict[int, int]:
    query = db.session.query(
        SkillXpAward.user_id,
        func.coalesce(func.sum(SkillXpAward.xp_total), 0).label("xp"),
    )
    if since is not None:
        query = query.filter(SkillXpAward.awarded_at >= since)
    query = query.group_by(SkillXpAward.user_id)
    return {int(user_id): int(xp or 0) for user_id, xp in query.all()}


def _load_progress_rows(since: datetime | None) -> list[tuple]:
    first_try_expr = func.sum(case((TaskProgress.attempts_count == 1, 1), else_=0))
    query = db.session.query(
        TaskProgress.user_id,
        TaskProgress.topic_id,
        func.count(TaskProgress.id).label("solved"),
        func.coalesce(first_try_expr, 0).label("first_try"),
        func.max(TaskProgress.completed_at).label("last_solved"),
    ).filter(TaskProgress.completed.is_(True))
    if since is not None:
        query = query.filter(TaskProgress.completed_at >= since)
    return query.group_by(TaskProgress.user_id, TaskProgress.topic_id).all()


def build_leaderboard(
    *,
    sort: str = "score",
    period: str = "all",
    current_user_id: int | None = None,
    limit: int = TOP_LIMIT,
) -> dict:
    """Собрать рейтинг. Пользователи без решённых задач не попадают в таблицу."""
    sort = sort if sort in SORTS else "score"
    period = period if period in PERIODS else "all"
    since = _period_start(period)

    progress_rows = _load_progress_rows(since)
    xp_by_user = _load_xp_by_user(since)

    grouped: dict[int, dict] = {}
    for user_id, topic_id, solved, first_try, last_solved in progress_rows:
        entry = grouped.setdefault(
            int(user_id),
            {
                "solved": 0,
                "first_try": 0,
                "topics_mastered": 0,
                "last_solved": None,
                "topic_solved": {},
            },
        )
        solved_n = int(solved or 0)
        first_try_n = int(first_try or 0)
        entry["solved"] += solved_n
        entry["first_try"] += first_try_n
        entry["topic_solved"][topic_id] = solved_n
        total_in_topic = _TOPIC_TOTALS.get(topic_id, 0)
        if total_in_topic and solved_n >= total_in_topic:
            entry["topics_mastered"] += 1
        last = _aware(last_solved)
        if last and (entry["last_solved"] is None or last > entry["last_solved"]):
            entry["last_solved"] = last

    if not grouped:
        return {
            "sort": sort,
            "period": period,
            "rows": [],
            "podium": [],
            "highlights": [],
            "me": None,
            "total_ranked": 0,
            "min_accuracy_solved": MIN_ACCURACY_SOLVED,
        }

    users = User.query.filter(User.id.in_(grouped.keys())).all()
    users_by_id = {user.id: user for user in users}

    ranked: list[dict] = []
    for user_id, stats in grouped.items():
        user = users_by_id.get(user_id)
        if not user or user.username in EXCLUDED_USERNAMES:
            continue
        solved = stats["solved"]
        if solved <= 0:
            continue
        first_try = stats["first_try"]
        xp = int(xp_by_user.get(user_id, 0))
        topics_mastered = stats["topics_mastered"]
        accuracy = round(first_try / solved * 100) if solved else 0
        specialty_id = None
        topic_solved = stats["topic_solved"]
        if topic_solved:
            best_id, best_count = max(topic_solved.items(), key=lambda item: item[1])
            if best_count >= 4:
                specialty_id = best_id
        activity = _activity_key(stats["last_solved"])
        ranked.append(
            {
                "user_id": user_id,
                "username": user.username,
                "initial": user.username[:1].upper(),
                "hue": _avatar_hue(user.username),
                "solved": solved,
                "first_try": first_try,
                "accuracy": accuracy,
                "topics_mastered": topics_mastered,
                "topics_total": len(_TOPIC_TOTALS),
                "xp": xp,
                "score": _compute_score(solved, first_try, topics_mastered, xp),
                "title": _title_for(solved),
                "specialty_topic_id": specialty_id,
                "activity": activity,
                "badges": _badges_for(solved, first_try, accuracy, topics_mastered),
                "is_me": current_user_id is not None and user_id == current_user_id,
            }
        )

    ranked.sort(key=lambda row: _sort_key(row, sort), reverse=True)
    for index, row in enumerate(ranked, start=1):
        row["rank"] = index

    me = next((row for row in ranked if row["is_me"]), None)
    if me:
        total = len(ranked)
        percentile = max(1, round(me["rank"] / total * 100)) if total else 100
        me = {
            **me,
            "chase": _chase_info(ranked, me),
            "percentile": percentile,
            "total_ranked": total,
        }

    visible = [dict(row) for row in ranked[: max(1, limit)]]
    if me and me["rank"] > limit:
        visible_ids = {row["user_id"] for row in visible}
        if me["user_id"] not in visible_ids:
            visible.append(dict(me))

    return {
        "sort": sort,
        "period": period,
        "rows": visible,
        "podium": ranked[:3],
        "highlights": _highlights(ranked),
        "me": me,
        "total_ranked": len(ranked),
        "min_accuracy_solved": MIN_ACCURACY_SOLVED,
    }


def _chase_info(ranked: list[dict], me: dict) -> dict | None:
    if me["rank"] <= 1:
        return None
    above = ranked[me["rank"] - 2]
    delta = max(0, above["score"] - me["score"])
    tasks_needed = max(1, ceil(delta / SCORE_SOLVED)) if delta else 1
    ratio = min(99, round(me["score"] / max(above["score"], 1) * 100))
    return {
        "username": above["username"],
        "rank": above["rank"],
        "delta": delta,
        "tasks_needed": tasks_needed,
        "ratio": ratio,
    }

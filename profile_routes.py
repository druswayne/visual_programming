"""Личный кабинет пользователя."""

from datetime import datetime, timezone

from flask import Blueprint, abort, render_template, url_for
from flask_login import current_user, login_required

from data.registry import get_task_with_tests, get_tasks_public, get_topics
from models import TaskAttempt, TaskProgress
from skills_service import build_skills_profile

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")

ACHIEVEMENT_CATEGORIES = [
    ("tasks", "Задачи"),
    ("topics", "Темы"),
    ("practice", "Практика"),
    ("skills", "Навыки"),
]

TIER_LABELS = {
    "bronze": "Бронза",
    "silver": "Серебро",
    "gold": "Золото",
    "special": "Особое",
}


def _prog_value(current: int | float, target: int | float, unit: str = "") -> dict:
    target = max(1, int(target))
    current = min(max(0, int(current)), target)
    label = f"{current}/{target}"
    if unit:
        label = f"{label} {unit}"
    return {
        "current": current,
        "target": target,
        "percent": round(current / target * 100),
        "label": label,
    }


def _prog_bool(unlocked: bool) -> dict:
    return _prog_value(1 if unlocked else 0, 1)


def _prog_sharpshooter(stats: dict) -> dict:
    attempts = stats["total_attempts"]
    rate = stats["success_rate"]
    if attempts >= 10 and rate >= 80:
        return {"current": 80, "target": 80, "percent": 100, "label": f"{rate}% успеха"}
    if attempts < 10:
        return _prog_value(attempts, 10, "попыток")
    return _prog_value(rate, 80, "% успеха")


def _prog_perfectionist(stats: dict) -> dict:
    attempts = stats["total_attempts"]
    rate = stats["success_rate"]
    if attempts >= 20 and rate >= 95:
        return {"current": 95, "target": 95, "percent": 100, "label": f"{rate}% успеха"}
    if attempts < 20:
        return _prog_value(attempts, 20, "попыток")
    return _prog_value(rate, 95, "% успеха")


ACHIEVEMENT_DEFS = [
    {
        "id": "first_task",
        "title": "Первый шаг",
        "icon": "🎯",
        "description": "Решить первую задачу",
        "category": "tasks",
        "tier": "bronze",
        "check": lambda s: s["total_completed"] >= 1,
        "progress": lambda s: _prog_value(s["total_completed"], 1, "задача"),
    },
    {
        "id": "tasks_10",
        "title": "Десятка",
        "icon": "🔟",
        "description": "Решить 10 задач",
        "category": "tasks",
        "tier": "bronze",
        "check": lambda s: s["total_completed"] >= 10,
        "progress": lambda s: _prog_value(s["total_completed"], 10, "задач"),
    },
    {
        "id": "tasks_25",
        "title": "Четверть сотни",
        "icon": "📈",
        "description": "Решить 25 задач",
        "category": "tasks",
        "tier": "silver",
        "check": lambda s: s["total_completed"] >= 25,
        "progress": lambda s: _prog_value(s["total_completed"], 25, "задач"),
    },
    {
        "id": "tasks_50",
        "title": "Полсотни",
        "icon": "🏅",
        "description": "Решить 50 задач",
        "category": "tasks",
        "tier": "silver",
        "check": lambda s: s["total_completed"] >= 50,
        "progress": lambda s: _prog_value(s["total_completed"], 50, "задач"),
    },
    {
        "id": "tasks_100",
        "title": "Сотня",
        "icon": "💯",
        "description": "Решить 100 задач",
        "category": "tasks",
        "tier": "gold",
        "check": lambda s: s["total_completed"] >= 100,
        "progress": lambda s: _prog_value(s["total_completed"], 100, "задач"),
    },
    {
        "id": "half_way",
        "title": "На полпути",
        "icon": "🛤️",
        "description": "Решить половину всех задач курса",
        "category": "tasks",
        "tier": "gold",
        "check": lambda s: s["total_tasks"] > 0 and s["total_completed"] >= s["total_tasks"] // 2,
        "progress": lambda s: _prog_value(
            s["total_completed"],
            max(1, s["total_tasks"] // 2),
            "задач",
        ),
    },
    {
        "id": "topic_master",
        "title": "Мастер темы",
        "icon": "📚",
        "description": "Полностью пройти любую тему",
        "category": "topics",
        "tier": "silver",
        "check": lambda s: s["topics_mastered"] >= 1,
        "progress": lambda s: _prog_value(s["topics_mastered"], 1, "тема"),
    },
    {
        "id": "all_topics",
        "title": "Покоритель курса",
        "icon": "👑",
        "description": "Пройти все темы курса",
        "category": "topics",
        "tier": "gold",
        "check": lambda s: s["topics_total"] > 0 and s["topics_mastered"] >= s["topics_total"],
        "progress": lambda s: _prog_value(s["topics_mastered"], max(1, s["topics_total"]), "тем"),
    },
    {
        "id": "explorer",
        "title": "Исследователь",
        "icon": "🧭",
        "description": "Начать 3 разные темы",
        "category": "topics",
        "tier": "bronze",
        "check": lambda s: s["topics_started"] >= 3,
        "progress": lambda s: _prog_value(s["topics_started"], 3, "тем"),
    },
    {
        "id": "explorer_all",
        "title": "Картограф",
        "icon": "🗺️",
        "description": "Открыть все темы курса",
        "category": "topics",
        "tier": "gold",
        "check": lambda s: s["topics_total"] > 0 and s["topics_started"] >= s["topics_total"],
        "progress": lambda s: _prog_value(s["topics_started"], max(1, s["topics_total"]), "тем"),
    },
    {
        "id": "persistent",
        "title": "Упорство",
        "icon": "💪",
        "description": "Сделать 25 попыток",
        "category": "practice",
        "tier": "bronze",
        "check": lambda s: s["total_attempts"] >= 25,
        "progress": lambda s: _prog_value(s["total_attempts"], 25, "попыток"),
    },
    {
        "id": "marathon",
        "title": "Марафон",
        "icon": "🏃",
        "description": "Сделать 100 попыток",
        "category": "practice",
        "tier": "gold",
        "check": lambda s: s["total_attempts"] >= 100,
        "progress": lambda s: _prog_value(s["total_attempts"], 100, "попыток"),
    },
    {
        "id": "sharpshooter",
        "title": "Меткий стрелок",
        "icon": "🎪",
        "description": "80% успешных попыток (от 10)",
        "category": "practice",
        "tier": "silver",
        "check": lambda s: s["total_attempts"] >= 10 and s["success_rate"] >= 80,
        "progress": _prog_sharpshooter,
    },
    {
        "id": "perfectionist",
        "title": "Без ошибок",
        "icon": "✨",
        "description": "95% успешных попыток (от 20)",
        "category": "practice",
        "tier": "gold",
        "check": lambda s: s["total_attempts"] >= 20 and s["success_rate"] >= 95,
        "progress": _prog_perfectionist,
    },
    {
        "id": "skill_starter",
        "title": "На пути инженера",
        "icon": "⚙️",
        "description": "Набрать 50 XP в дереве навыков",
        "category": "skills",
        "tier": "bronze",
        "check": lambda s: s.get("skills_total_xp", 0) >= 50,
        "progress": lambda s: _prog_value(s.get("skills_total_xp", 0), 50, "XP"),
    },
    {
        "id": "debugger_medal",
        "title": "Охотник за багами",
        "icon": "🔧",
        "description": "10+ задач «Исправь код»",
        "category": "skills",
        "tier": "silver",
        "check": lambda s: s.get("medal_fix_master", 0) >= 10,
        "progress": lambda s: _prog_value(s.get("medal_fix_master", 0), 10, "исправлений"),
    },
    {
        "id": "skill_crystal",
        "title": "Кристальный ум",
        "icon": "💎",
        "description": "Полностью освоить любую тему курса",
        "category": "skills",
        "tier": "gold",
        "check": lambda s: s.get("skills_crystals", 0) >= 1,
        "progress": lambda s: _prog_value(s.get("skills_crystals", 0), 1, "кристалл"),
    },
    {
        "id": "time_traveler",
        "title": "Путешественник во времени",
        "icon": "⏱️",
        "description": "Открыть Машину времени (★★ в «Условиях»)",
        "category": "skills",
        "tier": "special",
        "check": lambda s: s.get("time_machine_unlocked", False),
        "progress": lambda s: _prog_bool(s.get("time_machine_unlocked", False)),
    },
]


def _learn_url(topic_id: str, task_id: str | None = None) -> str:
    base = url_for("learn")
    if not task_id:
        return f"{base}?topic={topic_id}"
    return f"{base}?topic={topic_id}&task={task_id}"


def _find_next_task(progress_map: dict, topics: list, user_id: int) -> dict | None:
    from topic_unlock_service import is_topic_unlocked

    for topic in topics:
        if not is_topic_unlocked(user_id, topic["id"]):
            continue
        tid = topic["id"]
        tasks = get_tasks_public(tid)
        for task in tasks:
            key = (tid, task["id"])
            row = progress_map.get(key)
            if not row or not row.completed:
                return {
                    "topic_id": tid,
                    "topic_title": topic["title"],
                    "task_id": task["id"],
                    "task_title": task["title"],
                    "learn_url": _learn_url(tid, task["id"]),
                    "in_progress": bool(row and row.attempts_count > 0),
                }
    return None


def _normalize_code(code: str | None) -> str | None:
    if code is None:
        return None
    return code.strip()


def _build_achievements(stats: dict) -> list:
    items = []
    for ach in ACHIEVEMENT_DEFS:
        unlocked = ach["check"](stats)
        progress = ach["progress"](stats)
        if unlocked:
            progress = {**progress, "percent": 100}
        items.append(
            {
                "id": ach["id"],
                "title": ach["title"],
                "icon": ach["icon"],
                "description": ach["description"],
                "category": ach["category"],
                "tier": ach["tier"],
                "tier_label": TIER_LABELS[ach["tier"]],
                "unlocked": unlocked,
                "progress": progress,
                "in_progress": not unlocked and progress["percent"] > 0,
            }
        )
    items.sort(key=lambda a: (not a["unlocked"], -a["progress"]["percent"], a["title"]))
    return items


def _group_achievements(achievements: list) -> list[dict]:
    groups = []
    for cat_id, cat_label in ACHIEVEMENT_CATEGORIES:
        cat_items = [a for a in achievements if a["category"] == cat_id]
        if not cat_items:
            continue
        unlocked = sum(1 for a in cat_items if a["unlocked"])
        groups.append(
            {
                "id": cat_id,
                "label": cat_label,
                "achievements": cat_items,
                "unlocked": unlocked,
                "total": len(cat_items),
            }
        )
    return groups


def _build_dashboard_data(user):
    topics_meta = get_topics()
    topics_by_id = {t["id"]: t for t in topics_meta}

    progress_rows = (
        TaskProgress.query.filter_by(user_id=user.id)
        .order_by(TaskProgress.topic_id, TaskProgress.task_id)
        .all()
    )
    progress_map = {(p.topic_id, p.task_id): p for p in progress_rows}

    total_tasks = sum(len(get_tasks_public(t["id"])) for t in topics_meta)
    total_completed = sum(1 for p in progress_rows if p.completed)
    total_attempts = TaskAttempt.query.filter_by(user_id=user.id).count()
    successful_attempts = TaskAttempt.query.filter_by(user_id=user.id, success=True).count()

    topic_stats = []
    topics_mastered = 0
    topics_started = 0

    for topic in topics_meta:
        tid = topic["id"]
        tasks_public = get_tasks_public(tid)
        total_in_topic = len(tasks_public)
        rows = [progress_map.get((tid, t["id"])) for t in tasks_public]
        rows = [r for r in rows if r is not None]

        completed_rows = [r for r in rows if r.completed]
        completed_count = len(completed_rows)
        attempts_total = sum(r.attempts_count for r in rows)
        in_progress_count = sum(1 for r in rows if r.attempts_count > 0 and not r.completed)

        if attempts_total > 0:
            topics_started += 1
        if total_in_topic and completed_count >= total_in_topic:
            topics_mastered += 1

        percent = round(completed_count / total_in_topic * 100) if total_in_topic else 0
        if completed_count >= total_in_topic and total_in_topic:
            status = "completed"
        elif attempts_total > 0:
            status = "in_progress"
        else:
            status = "not_started"

        task_items = []
        completed_tasks = []
        for task in tasks_public:
            row = progress_map.get((tid, task["id"]))
            if not row:
                continue
            if row.completed or row.attempts_count > 0:
                task_items.append(
                    {
                        "id": task["id"],
                        "title": task["title"],
                        "attempts_count": row.attempts_count,
                        "completed": row.completed,
                        "completed_at": row.completed_at,
                        "learn_url": _learn_url(tid, task["id"]),
                    }
                )
            if row.completed:
                completed_tasks.append(
                    {
                        "id": task["id"],
                        "title": task["title"],
                        "attempts_count": row.attempts_count,
                        "completed_at": row.completed_at,
                        "learn_url": _learn_url(tid, task["id"]),
                    }
                )

        first_open = next(
            (t for t in tasks_public if not progress_map.get((tid, t["id"])) or not progress_map[(tid, t["id"])].completed),
            None,
        )

        topic_stats.append(
            {
                "id": tid,
                "title": topic["title"],
                "description": topic["description"],
                "total_tasks": total_in_topic,
                "completed_count": completed_count,
                "in_progress_count": in_progress_count,
                "attempts_total": attempts_total,
                "percent": percent,
                "status": status,
                "tasks": task_items,
                "completed_tasks": completed_tasks,
                "learn_url": _learn_url(tid, first_open["id"] if first_open else None),
            }
        )

    success_rate = round(successful_attempts / total_attempts * 100) if total_attempts else 0
    overall_percent = round(total_completed / total_tasks * 100) if total_tasks else 0

    stats = {
        "total_completed": total_completed,
        "total_tasks": total_tasks,
        "total_attempts": total_attempts,
        "topics_started": topics_started,
        "topics_mastered": topics_mastered,
        "topics_total": len(topics_meta),
        "success_rate": success_rate,
    }
    skills = build_skills_profile(user.id)
    stats.update(
        {
            "skills_total_xp": skills["total_xp"],
            "skills_crystals": skills["crystals"],
            "time_machine_unlocked": skills["time_machine_unlocked"],
            "medal_fix_master": next(
                (m["points"] for m in skills["medals"] if m["id"] == "fix_master"), 0
            ),
        }
    )
    achievements_list = _build_achievements(stats)

    recent_attempts_raw = (
        TaskAttempt.query.filter_by(user_id=user.id)
        .order_by(TaskAttempt.created_at.desc())
        .limit(12)
        .all()
    )

    recent_activity = []
    for attempt in recent_attempts_raw:
        topic = topics_by_id.get(attempt.topic_id, {"title": attempt.topic_id})
        task_public = next(
            (t for t in get_tasks_public(attempt.topic_id) if t["id"] == attempt.task_id),
            {"title": attempt.task_id},
        )
        recent_activity.append(
            {
                "success": attempt.success,
                "created_at": attempt.created_at,
                "topic_id": attempt.topic_id,
                "topic_title": topic["title"],
                "task_id": attempt.task_id,
                "task_title": task_public["title"],
                "learn_url": _learn_url(attempt.topic_id, attempt.task_id),
            }
        )

    last_activity_at = recent_attempts_raw[0].created_at if recent_attempts_raw else None

    member_since = user.created_at
    days_learning = 0
    if member_since:
        now = datetime.now(timezone.utc)
        if member_since.tzinfo is None:
            member_since = member_since.replace(tzinfo=timezone.utc)
        days_learning = max(1, (now - member_since).days + 1)

    return {
        "topics": topic_stats,
        "total_completed": total_completed,
        "total_tasks": total_tasks,
        "total_attempts": total_attempts,
        "successful_attempts": successful_attempts,
        "success_rate": success_rate,
        "overall_percent": overall_percent,
        "topics_started": topics_started,
        "topics_mastered": topics_mastered,
        "topics_total": len(topics_meta),
        "recent_activity": recent_activity,
        "last_activity_at": last_activity_at,
        "next_task": _find_next_task(progress_map, topics_meta, user.id),
        "achievements": achievements_list,
        "achievement_groups": _group_achievements(achievements_list),
        "achievements_unlocked": sum(1 for a in achievements_list if a["unlocked"]),
        "achievements_in_progress": sum(1 for a in achievements_list if a["in_progress"]),
        "achievements_total": len(ACHIEVEMENT_DEFS),
        "days_learning": days_learning,
        "member_since": user.created_at,
        "skills": skills,
    }


@profile_bp.route("/")
@login_required
def dashboard():
    data = _build_dashboard_data(current_user)
    return render_template("profile/dashboard.html", **data)


@profile_bp.route("/solution/<topic_id>/<task_id>")
@login_required
def solution(topic_id, task_id):
    progress = TaskProgress.query.filter_by(
        user_id=current_user.id,
        topic_id=topic_id,
        task_id=task_id,
    ).first()

    if not progress:
        abort(404)

    task = get_task_with_tests(topic_id, task_id)
    if not task:
        abort(404)

    topics = {t["id"]: t for t in get_topics()}
    attempts = (
        TaskAttempt.query.filter_by(
            user_id=current_user.id,
            topic_id=topic_id,
            task_id=task_id,
        )
        .order_by(TaskAttempt.created_at.desc())
        .all()
    )

    return render_template(
        "profile/solution.html",
        topic=topics.get(topic_id, {"id": topic_id, "title": topic_id}),
        task=task,
        progress=progress,
        attempts=attempts,
        learn_url=_learn_url(topic_id, task_id),
        solution_code=_normalize_code(progress.solution_code),
    )

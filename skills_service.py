"""Дерево навыков по темам курса (XP хранится в БД)."""

from __future__ import annotations

import json
from dataclasses import dataclass

from data.registry import get_task_with_tests, get_tasks_public, get_topics
from data.skills_config import (
    LEGACY_BRANCH_IDS,
    LEGACY_MEDAL_IDS,
    LEVEL_NAMES,
    MEDAL_DEFS,
    STAR_THRESHOLDS,
    TIME_MACHINE_MIN_LEVEL,
    TIME_MACHINE_TOPIC,
    TOPIC_ORDER,
    build_skill_branches,
)
from topic_unlock_service import get_unlock_info, is_topic_unlocked
from extensions import db
from models import SkillBranchXp, SkillMedalPoints, SkillXpAward, TaskProgress

SKILL_BRANCHES = build_skill_branches()
BRANCH_IDS = tuple(TOPIC_ORDER)
MEDAL_IDS = tuple(m["id"] for m in MEDAL_DEFS)


@dataclass
class TaskXpResult:
    xp_by_branch: dict[str, int]
    medals: dict[str, int]


def _is_fix_task(topic_id: str, task_id: str) -> bool:
    task = get_task_with_tests(topic_id, task_id)
    return bool(task and task.get("starter_xml"))


def calc_xp_for_completed_task(topic_id: str, task_id: str, attempts_count: int) -> TaskXpResult:
    """XP начисляется в ветку темы, где решена задача."""
    if topic_id not in BRANCH_IDS:
        topic_id = "io"

    is_fix = _is_fix_task(topic_id, task_id)
    base = 12 if is_fix else 10
    if attempts_count == 1:
        base += 4
    elif attempts_count <= 2:
        base += 2

    medals: dict[str, int] = {}
    if is_fix:
        medals["fix_master"] = 1
    if attempts_count == 1:
        medals["clean_solve"] = 1

    return TaskXpResult(xp_by_branch={topic_id: base}, medals=medals)


def _level_from_ratio(ratio: float) -> int:
    if ratio <= 0:
        return 0
    level = 1
    for idx in range(1, len(STAR_THRESHOLDS)):
        if ratio >= STAR_THRESHOLDS[idx]:
            level = idx
    return min(level, 5)


def _level_from_xp_in_topic(completed: int, total: int) -> int:
    if total == 0:
        return 0
    return _level_from_ratio(completed / total)


def _progress_to_next_star(completed: int, total: int, level: int) -> tuple[int, int, int]:
    """Сколько задач сделано и нужно до следующей звезды."""
    if total == 0 or level >= 5:
        return completed, total, 100
    next_threshold = STAR_THRESHOLDS[level + 1]
    needed_total = max(1, round(total * next_threshold))
    prev_threshold = STAR_THRESHOLDS[level] if level > 0 else 0.0
    prev_total = round(total * prev_threshold) if level > 0 else 0
    span = max(1, needed_total - prev_total)
    progress = max(0, completed - prev_total)
    percent = min(100, round(progress / span * 100))
    return progress, span, percent


def _unlock_hint(user_id: int, topic_id: str) -> str | None:
    return get_unlock_info(user_id, topic_id).get("unlock_hint")


def _next_level_hint(
    completed: int,
    total: int,
    level: int,
    locked: bool,
    fix_completed: int,
    fix_total: int,
) -> str:
    if locked:
        return ""
    if level >= 5:
        return f"Тема освоена · {fix_completed}/{fix_total} исправлений"
    _, span, _ = _progress_to_next_star(completed, total, level)
    next_name = LEVEL_NAMES[level + 1]
    remaining = max(0, span - _progress_to_next_star(completed, total, level)[0])
    return f"До «{next_name}»: ещё ~{remaining} задач · исправления {fix_completed}/{fix_total}"


def _collect_topic_stats(user_id: int) -> dict[str, dict]:
    stats: dict[str, dict] = {}
    for topic in get_topics():
        tid = topic["id"]
        tasks = get_tasks_public(tid)
        total = len(tasks)
        fix_total = sum(1 for t in tasks if t.get("starter_xml"))

        rows = TaskProgress.query.filter_by(user_id=user_id, topic_id=tid, completed=True).all()
        completed_ids = {r.task_id for r in rows}
        completed = len(completed_ids)
        fix_completed = sum(1 for t in tasks if t.get("starter_xml") and t["id"] in completed_ids)

        level = _level_from_xp_in_topic(completed, total)
        prog, span, percent = _progress_to_next_star(completed, total, level)

        stats[tid] = {
            "total_tasks": total,
            "completed_count": completed,
            "fix_total": fix_total,
            "fix_completed": fix_completed,
            "level": level,
            "percent": round(completed / total * 100) if total else 0,
            "xp_progress": prog,
            "xp_needed": span,
            "level_percent": percent,
        }
    return stats


def _build_recommendation(user_id: int, topic_stats: dict[str, dict]) -> dict | None:
    titles = {t["id"]: t["title"] for t in get_topics()}

    for tid in TOPIC_ORDER:
        if not is_topic_unlocked(user_id, tid):
            info = get_unlock_info(user_id, tid)
            return {
                "topic_id": info["requires_topic_id"],
                "text": info["unlock_hint"] or f"Продолжайте тему «{titles.get(tid, tid)}».",
            }

    candidates = [
        tid
        for tid in TOPIC_ORDER
        if is_topic_unlocked(user_id, tid) and topic_stats[tid]["level"] < 5
    ]
    if not candidates:
        return None

    tid = min(candidates, key=lambda x: topic_stats[x]["percent"])
    stats = topic_stats[tid]
    if stats["fix_completed"] < stats["fix_total"]:
        text = (
            f"В теме «{titles[tid]}» остались задачи «Исправь код» "
            f"({stats['fix_completed']}/{stats['fix_total']}). Они идут сразу после обычных заданий."
        )
    else:
        text = (
            f"Продолжайте тему «{titles[tid]}»: решено {stats['completed_count']}"
            f"/{stats['total_tasks']} задач."
        )
    return {"topic_id": tid, "text": text}


def _load_branch_xp(user_id: int) -> dict[str, int]:
    rows = SkillBranchXp.query.filter_by(user_id=user_id).all()
    xp_map = {bid: 0 for bid in BRANCH_IDS}
    for row in rows:
        if row.branch_id in xp_map:
            xp_map[row.branch_id] = row.xp
    return xp_map


def _load_medals(user_id: int) -> dict[str, int]:
    rows = SkillMedalPoints.query.filter_by(user_id=user_id).all()
    medals = {mid: 0 for mid in MEDAL_IDS}
    for row in rows:
        if row.medal_id in medals:
            medals[row.medal_id] = row.points
    return medals


def _add_branch_xp(user_id: int, xp_by_branch: dict[str, int]) -> None:
    for branch_id, amount in xp_by_branch.items():
        if amount <= 0 or branch_id not in BRANCH_IDS:
            continue
        row = SkillBranchXp.query.filter_by(user_id=user_id, branch_id=branch_id).first()
        if row:
            row.xp += amount
        else:
            db.session.add(SkillBranchXp(user_id=user_id, branch_id=branch_id, xp=amount))


def _add_medals(user_id: int, medals: dict[str, int]) -> None:
    for medal_id, amount in medals.items():
        if amount <= 0:
            continue
        if medal_id not in MEDAL_IDS:
            continue
        row = SkillMedalPoints.query.filter_by(user_id=user_id, medal_id=medal_id).first()
        if row:
            row.points += amount
        else:
            db.session.add(SkillMedalPoints(user_id=user_id, medal_id=medal_id, points=amount))


def _migrate_legacy_skills_if_needed(user_id: int) -> bool:
    """Пересчитать XP после смены схемы веток (абстрактные → темы)."""
    legacy_branch = SkillBranchXp.query.filter(
        SkillBranchXp.user_id == user_id,
        SkillBranchXp.branch_id.in_(LEGACY_BRANCH_IDS),
    ).first()
    legacy_medal = SkillMedalPoints.query.filter(
        SkillMedalPoints.user_id == user_id,
        SkillMedalPoints.medal_id.in_(LEGACY_MEDAL_IDS),
    ).first()
    legacy_award = SkillXpAward.query.filter(
        SkillXpAward.user_id == user_id,
        SkillXpAward.primary_branch.in_(LEGACY_BRANCH_IDS),
    ).first()

    if not (legacy_branch or legacy_medal or legacy_award):
        return False

    SkillBranchXp.query.filter_by(user_id=user_id).delete()
    SkillMedalPoints.query.filter_by(user_id=user_id).delete()
    SkillXpAward.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    backfill_skills_from_progress(user_id)
    return True


def award_task_skills_xp(
    user_id: int,
    topic_id: str,
    task_id: str,
    attempts_count: int,
) -> TaskXpResult | None:
    existing = SkillXpAward.query.filter_by(
        user_id=user_id,
        topic_id=topic_id,
        task_id=task_id,
    ).first()
    if existing:
        return None

    result = calc_xp_for_completed_task(topic_id, task_id, attempts_count)
    xp_total = sum(result.xp_by_branch.values())
    primary_branch = topic_id if topic_id in BRANCH_IDS else max(
        result.xp_by_branch.items(), key=lambda x: x[1]
    )[0]

    db.session.add(
        SkillXpAward(
            user_id=user_id,
            topic_id=topic_id,
            task_id=task_id,
            xp_total=xp_total,
            primary_branch=primary_branch,
            xp_breakdown=json.dumps(result.xp_by_branch),
            medals_breakdown=json.dumps(result.medals) if result.medals else None,
        )
    )
    _add_branch_xp(user_id, result.xp_by_branch)
    _add_medals(user_id, result.medals)
    return result


def backfill_skills_from_progress(user_id: int) -> int:
    completed = TaskProgress.query.filter_by(user_id=user_id, completed=True).all()
    awarded = 0
    for progress in completed:
        if award_task_skills_xp(user_id, progress.topic_id, progress.task_id, progress.attempts_count):
            awarded += 1
    if awarded:
        db.session.commit()
    return awarded


def _sync_derived_medals(user_id: int) -> None:
    """Пересчитать медали, зависящие от агрегированного прогресса."""
    topic_stats = _collect_topic_stats(user_id)
    topics_done = sum(1 for stats in topic_stats.values() if stats["level"] >= 5)
    row = SkillMedalPoints.query.filter_by(user_id=user_id, medal_id="topics_done").first()
    if row:
        row.points = topics_done
    elif topics_done:
        db.session.add(
            SkillMedalPoints(user_id=user_id, medal_id="topics_done", points=topics_done)
        )
    db.session.commit()


def ensure_skills_synced(user_id: int) -> None:
    _migrate_legacy_skills_if_needed(user_id)
    completed_count = TaskProgress.query.filter_by(user_id=user_id, completed=True).count()
    awards_count = SkillXpAward.query.filter_by(user_id=user_id).count()
    if completed_count > awards_count:
        backfill_skills_from_progress(user_id)
    _sync_derived_medals(user_id)


def build_skills_profile(user_id: int) -> dict:
    ensure_skills_synced(user_id)

    topic_stats = _collect_topic_stats(user_id)
    branch_xp = _load_branch_xp(user_id)
    medals = _load_medals(user_id)
    total_xp = sum(branch_xp.values())
    crystals = sum(1 for tid in BRANCH_IDS if topic_stats[tid]["level"] >= 5)

    titles = {t["id"]: t["title"] for t in get_topics()}
    branches = []
    for index, meta in enumerate(SKILL_BRANCHES):
        tid = meta["id"]
        stats = topic_stats[tid]
        level = stats["level"]
        locked = not is_topic_unlocked(user_id, tid)
        display_level = level if not locked else 0
        stars = level if not locked else 0

        branches.append(
            {
                **meta,
                "order": index + 1,
                "xp": branch_xp.get(tid, 0),
                "level": display_level,
                "display_level": level,
                "locked": locked,
                "stars_filled": stars,
                "level_name": (
                    LEVEL_NAMES[level]
                    if not locked and level > 0
                    else ("Открыта" if not locked else "Закрыта")
                ),
                "next_level_name": (
                    LEVEL_NAMES[level + 1] if level < 5 and not locked else None
                ),
                "completed_count": stats["completed_count"],
                "total_tasks": stats["total_tasks"],
                "fix_completed": stats["fix_completed"],
                "fix_total": stats["fix_total"],
                "topic_percent": stats["percent"],
                "xp_progress": stats["xp_progress"],
                "xp_needed": stats["xp_needed"],
                "level_percent": stats["level_percent"],
                "unlock_hint": _unlock_hint(user_id, tid),
                "next_hint": _next_level_hint(
                    stats["completed_count"],
                    stats["total_tasks"],
                    level,
                    locked,
                    stats["fix_completed"],
                    stats["fix_total"],
                ),
            }
        )

    conditions_level = topic_stats[TIME_MACHINE_TOPIC]["level"]
    time_machine_unlocked = conditions_level >= TIME_MACHINE_MIN_LEVEL

    recent_gains = []
    for award in (
        SkillXpAward.query.filter_by(user_id=user_id)
        .order_by(SkillXpAward.awarded_at.desc())
        .limit(5)
        .all()
    ):
        task_public = next(
            (t for t in get_tasks_public(award.topic_id) if t["id"] == award.task_id),
            {"title": award.task_id},
        )
        recent_gains.append(
            {
                "task_title": task_public["title"],
                "topic_title": titles.get(award.topic_id, award.topic_id),
                "xp_total": award.xp_total,
                "branch_title": titles.get(award.primary_branch, award.primary_branch),
                "completed_at": award.awarded_at,
            }
        )

    return {
        "branches": branches,
        "topic_order": TOPIC_ORDER,
        "total_xp": total_xp,
        "crystals": crystals,
        "medals": [{**m, "points": medals.get(m["id"], 0)} for m in MEDAL_DEFS],
        "time_machine_unlocked": time_machine_unlocked,
        "time_machine_topic": titles[TIME_MACHINE_TOPIC],
        "time_machine_level": conditions_level,
        "time_machine_required_level": TIME_MACHINE_MIN_LEVEL,
        "recommendation": _build_recommendation(user_id, topic_stats),
        "recent_gains": recent_gains,
        "level_names": LEVEL_NAMES,
    }

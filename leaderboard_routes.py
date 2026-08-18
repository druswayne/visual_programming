"""Публичная страница рейтинга пользователей."""

from flask import Blueprint, render_template, request
from flask_login import current_user

from data.registry import get_topics
from i18n import ngettext
from leaderboard_service import PERIODS, SCORE_SOLVED, SORTS, build_leaderboard

leaderboard_bp = Blueprint("leaderboard", __name__)


def _topic_titles() -> dict[str, str]:
    return {topic["id"]: topic["title"] for topic in get_topics()}


@leaderboard_bp.route("/leaderboard")
def ranking():
    sort = request.args.get("sort", "score")
    period = request.args.get("period", "all")
    if sort not in SORTS:
        sort = "score"
    if period not in PERIODS:
        period = "all"

    current_id = current_user.id if current_user.is_authenticated else None
    data = build_leaderboard(sort=sort, period=period, current_user_id=current_id)
    if data["me"] and data["me"].get("chase"):
        chase = data["me"]["chase"]
        word = ngettext("profile.task", "profile.tasks_2_4", chase["tasks_needed"])
        chase["tasks_label"] = f"{chase['tasks_needed']} {word}"
    titles = _topic_titles()
    for row in data["rows"]:
        topic_id = row.get("specialty_topic_id")
        row["specialty"] = titles.get(topic_id) if topic_id else None
    if data["me"]:
        topic_id = data["me"].get("specialty_topic_id")
        data["me"]["specialty"] = titles.get(topic_id) if topic_id else None
    for row in data["podium"]:
        topic_id = row.get("specialty_topic_id")
        row["specialty"] = titles.get(topic_id) if topic_id else None

    return render_template(
        "leaderboard.html",
        **data,
        sorts=SORTS,
        periods=PERIODS,
        score_solved=SCORE_SOLVED,
    )

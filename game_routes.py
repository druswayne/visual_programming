"""API игрового режима: линейки, миссии, запуск и проверка."""

from __future__ import annotations

import random

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from data.game.registry import (
    get_mission,
    is_mission_track_unlocked,
    list_missions_public,
    list_tracks_for_user,
    public_mission,
    public_world,
    resolve_worlds,
    sample_world,
)
from game.checker import check_mission
from game.runtime import run_robot_program
from game.unlock import TRACK_TOPIC_IDS, get_unlock_info
from data.game.registry import track_titles, track_totals
from i18n import _
from limits import rate_limit_execution
from models import TaskProgress
from progress_service import maybe_record_check

game_bp = Blueprint("game", __name__, url_prefix="/api/game")


def _user_id() -> int | None:
    if current_user.is_authenticated:
        return current_user.id
    return None


def _progress_map(user_id: int, topic_id: str) -> dict[str, TaskProgress]:
    rows = TaskProgress.query.filter_by(user_id=user_id, topic_id=topic_id).all()
    return {row.task_id: row for row in rows}


def _enrich_missions(track_id: str) -> list[dict]:
    topic_id = TRACK_TOPIC_IDS[track_id]
    progress_by_id = {}
    if current_user.is_authenticated:
        progress_by_id = _progress_map(current_user.id, topic_id)
    result = []
    for item in list_missions_public(track_id):
        progress = progress_by_id.get(item["id"])
        result.append(
            {
                **item,
                "completed": bool(progress and progress.completed),
                "has_solution": bool(
                    progress and (progress.solution_xml or progress.solution_code)
                ),
            }
        )
    return result


@game_bp.route("/tracks", methods=["GET"])
@login_required
def list_tracks():
    return jsonify({"tracks": list_tracks_for_user(_user_id())})


@game_bp.route("/tracks/<track_id>/missions", methods=["GET"])
@login_required
def list_missions(track_id):
    tracks = {item["id"] for item in list_tracks_for_user(_user_id())}
    if track_id not in tracks:
        return jsonify({"error": _("game.track_not_found")}), 404
    if not is_mission_track_unlocked(_user_id(), track_id):
        info = get_unlock_info(_user_id(), track_id, track_totals(), track_titles())
        return jsonify({"error": info.get("unlock_hint"), "locked": True, **info}), 403
    return jsonify({"missions": _enrich_missions(track_id)})


@game_bp.route("/missions/<mission_id>", methods=["GET"])
@login_required
def mission_detail(mission_id):
    mission = get_mission(mission_id)
    if not mission:
        return jsonify({"error": _("game.mission_not_found")}), 404
    track_id = mission["track"]
    if not is_mission_track_unlocked(_user_id(), track_id):
        info = get_unlock_info(_user_id(), track_id, track_totals(), track_titles())
        return jsonify({"error": info.get("unlock_hint"), "locked": True, **info}), 403
    seed = request.args.get("seed", type=int)
    spec = mission.get("generator") or {}
    count = max(1, int(spec.get("count") or 1))
    if seed is None:
        seed = random.randint(1, count)
    world = sample_world(mission, seed)
    payload = public_mission(mission)
    if current_user.is_authenticated:
        topic_id = TRACK_TOPIC_IDS[track_id]
        progress = TaskProgress.query.filter_by(
            user_id=current_user.id,
            topic_id=topic_id,
            task_id=mission_id,
        ).first()
        payload["completed"] = bool(progress and progress.completed)
        payload["has_solution"] = bool(
            progress and (progress.solution_xml or progress.solution_code)
        )
    else:
        payload["completed"] = False
        payload["has_solution"] = False
    return jsonify(
        {
            "mission": payload,
            "world": public_world(world),
            "seed": seed,
        }
    )


@game_bp.route("/run", methods=["POST"])
@login_required
@rate_limit_execution()
def run_mission():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "")
    mission_id = data.get("mission_id", "")
    mission = get_mission(mission_id)
    if not mission:
        return jsonify({"success": False, "error": _("game.mission_not_found")}), 404
    if not is_mission_track_unlocked(_user_id(), mission["track"]):
        return jsonify({"success": False, "error": _("game.track_locked")}), 403
    world = data.get("world")
    if not isinstance(world, dict):
        world = sample_world(mission, int(data.get("seed") or 1))
    result = run_robot_program(code, world, mission.get("goal"))
    status = 503 if result.get("overloaded") else 200
    return jsonify(result), status


@game_bp.route("/check", methods=["POST"])
@login_required
@rate_limit_execution()
def check_mission_view():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "")
    mission_id = data.get("mission_id", "")
    blocks_xml = data.get("blocks_xml", "")
    mission = get_mission(mission_id)
    if not mission:
        return jsonify({"success": False, "message": _("game.mission_not_found")}), 404
    track_id = mission["track"]
    if not is_mission_track_unlocked(_user_id(), track_id):
        return jsonify({"success": False, "message": _("game.track_locked")}), 403
    if not (code or "").strip():
        return jsonify({"success": False, "message": _("api.build_program_first")}), 400

    worlds = resolve_worlds(mission)
    result = check_mission(code, worlds, mission.get("goal"))
    if result.get("overloaded"):
        return jsonify(result), 503

    topic_id = TRACK_TOPIC_IDS[track_id]
    progress = maybe_record_check(
        topic_id,
        mission_id,
        code,
        bool(result.get("success")),
        blocks_xml=blocks_xml or None,
    )
    if progress:
        result["progress"] = progress
    return jsonify(result)

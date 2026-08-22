"""Проверка решения миссии на всех вариантах карты."""

from __future__ import annotations

from typing import Any

from i18n import _

from game.runtime import run_robot_program


def check_mission(code: str, worlds: list[dict], goal: dict | list | None) -> dict[str, Any]:
    if not worlds:
        return {
            "success": False,
            "message": _("game.check.no_worlds"),
            "passed": 0,
            "total": 0,
        }

    last_ok = None
    for index, world in enumerate(worlds):
        result = run_robot_program(code, world, goal)
        if result.get("overloaded"):
            return {
                "success": False,
                "message": result.get("error"),
                "overloaded": True,
                "passed": index,
                "total": len(worlds),
                "result": result,
            }
        if not result.get("success"):
            return {
                "success": False,
                "message": result.get("error") or _("game.check.failed"),
                "passed": index,
                "total": len(worlds),
                "failed_index": index,
                "failed_world": world,
                "result": result,
            }
        if not result.get("goal_met"):
            return {
                "success": False,
                "message": _("game.check.goal_failed"),
                "passed": index,
                "total": len(worlds),
                "failed_index": index,
                "failed_world": world,
                "result": result,
            }
        last_ok = result

    return {
        "success": True,
        "message": _("game.check.ok"),
        "passed": len(worlds),
        "total": len(worlds),
        "result": last_ok,
        "world": worlds[-1],
    }

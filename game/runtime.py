"""Запуск программы ученика в мире робота (subprocess + prelude)."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from i18n import _
from runner.pool import ExecutionPoolBusy, execution_slot
from runner.sandbox import (
    EXECUTION_TIMEOUT,
    FORBIDDEN_PATTERNS,
    resolve_python_executable,
    validate_code,
)

from game.world import World, check_goal

RESULT_MARKER = "__PYBLOCKS_GAME__"
_GAME_IMPORT_FORBIDDEN = ("import ", "from ")


def translate_robot_error(error: dict | str | None) -> str | None:
    if not error:
        return None
    if isinstance(error, str):
        return error
    code = error.get("code") or "runtime"
    key = f"game.error.{code}"
    text = _(key)
    if text == key:
        message = (error.get("params") or {}).get("message")
        return message or _("game.error.runtime")
    return text


def _student_forbidden(code: str) -> str | None:
    lowered = code.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.lower() in lowered:
            return _("runner.forbidden_pattern", pattern=pattern)
    for line in code.splitlines():
        stripped = line.strip().lower()
        if stripped.startswith("#"):
            continue
        if stripped.startswith(_GAME_IMPORT_FORBIDDEN):
            return _("runner.forbidden_pattern", pattern="import")
    return None


def _write_runner(directory: Path, world_data: dict, goal: dict | list | None) -> None:
    src = Path(__file__).resolve().parent / "world.py"
    shutil.copy(src, directory / "world.py")
    payload = {
        "world": world_data,
        "goal": goal,
    }
    (directory / "payload.json").write_text(
        json.dumps(payload, ensure_ascii=False),
        encoding="utf-8",
    )
    (directory / "runner.py").write_text(
        f"""# -*- coding: utf-8 -*-
import json
import traceback
from pathlib import Path
from world import Robot, RobotError, World, check_goal

MARKER = {RESULT_MARKER!r}

def dump(result):
    print(MARKER + json.dumps(result, ensure_ascii=False))

payload = json.loads(Path("payload.json").read_text(encoding="utf-8"))
world = World(payload["world"])
robot = Robot(world)
error = None
try:
    student = Path("student.py").read_text(encoding="utf-8")
    exec(compile(student, "student.py", "exec"), {{"robot": robot, "__name__": "__main__"}})
except RobotError as exc:
    error = {{"code": exc.code, "params": exc.params}}
except Exception as exc:
    error = {{"code": "runtime", "params": {{"message": str(exc), "trace": traceback.format_exc()}}}}

goal_met = False if error else check_goal(world, payload.get("goal"))
dump({{
    "ok": error is None,
    "error": error,
    "steps": world.steps,
    "final": world.snapshot(),
    "goal_met": goal_met,
}})
""",
        encoding="utf-8",
    )


def _parse_result(stdout: str) -> dict[str, Any] | None:
    if not stdout:
        return None
    marker_at = stdout.rfind(RESULT_MARKER)
    if marker_at < 0:
        return None
    raw = stdout[marker_at + len(RESULT_MARKER) :].strip().splitlines()[0]
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def run_robot_program(code: str, world_data: dict, goal: dict | list | None = None) -> dict:
    """Выполнить код ученика в мире. Возвращает шаги, ошибку и goal_met."""
    if not (code or "").strip():
        return {
            "success": False,
            "error": _("api.code_empty"),
            "steps": [],
            "final": None,
            "goal_met": False,
        }

    forbidden = _student_forbidden(code) or validate_code(code)
    if forbidden:
        return {
            "success": False,
            "error": forbidden,
            "steps": [],
            "final": None,
            "goal_met": False,
        }

    try:
        World(world_data)
    except (TypeError, ValueError, KeyError):
        return {
            "success": False,
            "error": _("game.error.bad_world"),
            "steps": [],
            "final": None,
            "goal_met": False,
        }

    tmp = tempfile.mkdtemp(prefix="pyblocks_game_")
    tmp_path = Path(tmp)
    try:
        _write_runner(tmp_path, world_data, goal)
        (tmp_path / "student.py").write_text(code, encoding="utf-8")
        with execution_slot():
            completed = subprocess.run(
                [resolve_python_executable(), str(tmp_path / "runner.py")],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=EXECUTION_TIMEOUT,
                cwd=str(tmp_path),
                env={
                    "PYTHONIOENCODING": "utf-8",
                    "PYTHONUTF8": "1",
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
            )
        parsed = _parse_result(completed.stdout)
        if parsed is None:
            output = (completed.stdout or "") + ("\n" if completed.stderr else "") + (completed.stderr or "")
            return {
                "success": False,
                "error": _("runner.exec_error"),
                "output": output.strip(),
                "steps": [],
                "final": None,
                "goal_met": False,
            }
        error = parsed.get("error")
        return {
            "success": bool(parsed.get("ok")) and error is None,
            "error": translate_robot_error(error),
            "error_code": error.get("code") if isinstance(error, dict) else None,
            "steps": parsed.get("steps") or [],
            "final": parsed.get("final"),
            "goal_met": bool(parsed.get("goal_met")),
        }
    except ExecutionPoolBusy as exc:
        return {
            "success": False,
            "error": str(exc),
            "steps": [],
            "final": None,
            "goal_met": False,
            "overloaded": True,
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": _("runner.timeout", seconds=EXECUTION_TIMEOUT),
            "steps": [],
            "final": None,
            "goal_met": False,
        }
    except Exception as exc:
        return {
            "success": False,
            "error": str(exc),
            "steps": [],
            "final": None,
            "goal_met": False,
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def goal_met_in_process(world_data: dict, goal: dict | list | None, code_result_final: dict | None) -> bool:
    """Запасная проверка цели по финальному снимку (без повторного запуска)."""
    if not code_result_final:
        return False
    merged = dict(world_data)
    merged["start"] = [code_result_final.get("x", 0), code_result_final.get("y", 0)]
    merged["facing"] = code_result_final.get("facing") or merged.get("facing") or "right"
    merged["carrying"] = bool(code_result_final.get("carrying"))
    merged["painted"] = code_result_final.get("painted") or []
    merged["items"] = code_result_final.get("items") or []
    merged["boxes"] = code_result_final.get("boxes") or []
    try:
        world = World(merged)
    except (TypeError, ValueError, KeyError):
        return False
    world.steps = []
    return check_goal(world, goal)

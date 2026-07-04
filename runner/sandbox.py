"""Безопасный запуск Python-кода для учебных целей."""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from runner.pool import ExecutionPoolBusy, execution_slot

FORBIDDEN_PATTERNS = [
    "import os",
    "import sys",
    "import subprocess",
    "import shutil",
    "import socket",
    "import pathlib",
    "__import__",
    "eval(",
    "exec(",
    "open(",
    "compile(",
    "globals(",
    "locals(",
    "getattr(",
    "setattr(",
    "delattr(",
    "breakpoint(",
]

MAX_OUTPUT_CHARS = 8000
EXECUTION_TIMEOUT = 5

_NON_PYTHON_EXECUTABLE_MARKERS = ("uwsgi", "gunicorn")


def resolve_python_executable() -> str:
    """Возвращает путь к интерпретатору Python (не uWSGI/gunicorn)."""
    override = os.environ.get("SANDBOX_PYTHON")
    if override:
        return override

    candidates = []
    base = getattr(sys, "_base_executable", None)
    if base:
        candidates.append(base)
    candidates.append(sys.executable)

    for exe in candidates:
        name = os.path.basename(exe).lower()
        if "python" in name and not any(marker in name for marker in _NON_PYTHON_EXECUTABLE_MARKERS):
            return exe

    for name in ("python3", "python"):
        found = shutil.which(name)
        if found:
            return found

    return sys.executable


def validate_code(code: str):
    """Проверяет код на запрещённые конструкции. Возвращает сообщение об ошибке или None."""
    lowered = code.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.lower() in lowered:
            return f"Запрещённая конструкция: {pattern}"
    return None


def run_python_code(code: str, stdin_text: str = "") -> dict:
    """Выполняет Python-код в изолированном subprocess с ограничением по времени."""
    validation_error = validate_code(code)
    if validation_error:
        return {"success": False, "output": "", "error": validation_error}

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        with execution_slot():
            result = subprocess.run(
                [resolve_python_executable(), tmp_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                input=stdin_text or None,
                timeout=EXECUTION_TIMEOUT,
                cwd=tempfile.gettempdir(),
                env={
                    "PYTHONIOENCODING": "utf-8",
                    "PYTHONUTF8": "1",
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
            )

        output = result.stdout
        if result.stderr:
            output += ("\n" if output else "") + result.stderr

        if len(output) > MAX_OUTPUT_CHARS:
            output = output[:MAX_OUTPUT_CHARS] + "\n… (вывод обрезан)"

        if result.returncode != 0:
            error = "Ошибка выполнения программы"
            if "EOFError" in output or "EOF when reading a line" in output:
                error = (
                    "Не хватило введённых данных для всех блоков input(). "
                    "Если ввод в цикле — укажите значение для каждого шага."
                )
            return {
                "success": False,
                "output": output.strip(),
                "error": error,
            }

        return {"success": True, "output": output.strip(), "error": None}

    except ExecutionPoolBusy as exc:
        return {"success": False, "output": "", "error": str(exc), "overloaded": True}
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": f"Превышено время выполнения ({EXECUTION_TIMEOUT} сек.)",
        }
    except Exception as exc:
        return {"success": False, "output": "", "error": str(exc)}
    finally:
        Path(tmp_path).unlink(missing_ok=True)

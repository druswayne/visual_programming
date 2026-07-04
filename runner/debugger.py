"""Пошаговая трассировка Python-кода для PyBlocks."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from runner.pool import ExecutionPoolBusy, execution_slot
from runner.sandbox import (
    EXECUTION_TIMEOUT,
    MAX_OUTPUT_CHARS,
    resolve_python_executable,
    validate_code,
)

MAX_STEPS = 500

TRACE_RUNNER = r'''
import json
import math
import random
import sys
import io
from contextlib import redirect_stdout

USER_CODE = __CODE__

MAX_LIST_ITEMS = 24
MAX_DICT_ITEMS = 20
MAX_STR_LEN = 120
MAX_HEAP_DEPTH = 5


def _truncate_str(value):
    if len(value) <= MAX_STR_LEN:
        return value
    return value[:MAX_STR_LEN] + "…"


def _legacy_value(value):
  """Плоское значение для обратной совместимости."""
  try:
    if value is None or isinstance(value, (bool, int, float)):
      return value
    if isinstance(value, str):
      return _truncate_str(value)
    if isinstance(value, (list, tuple)):
      items = [_legacy_value(v) for v in list(value)[:40]]
      if len(value) > 40:
        items.append("…")
      return items
    if isinstance(value, dict):
      return {str(k): _legacy_value(v) for k, v in list(value.items())[:30]}
    return repr(value)[:300]
  except Exception:
    return "?"


class MemoryTracer:
  def __init__(self):
    self._obj_ids = {}
    self._obj_store = {}
    self._next_id = 0
    self._prev_top_vars = {}

  def _register(self, obj):
    key = id(obj)
    if key not in self._obj_ids:
      self._next_id += 1
      oid = f"obj_{self._next_id}"
      self._obj_ids[key] = oid
      self._obj_store[oid] = obj
    return self._obj_ids[key]

  def _value_cell(self, value, depth=0):
    if depth > MAX_HEAP_DEPTH:
      return {"kind": "value", "type": "…", "value": "…"}
    if value is None:
      return {"kind": "value", "type": "NoneType", "value": None}
    if isinstance(value, bool):
      return {"kind": "value", "type": "bool", "value": value}
    if isinstance(value, int) and not isinstance(value, bool):
      return {"kind": "value", "type": "int", "value": value}
    if isinstance(value, float):
      return {"kind": "value", "type": "float", "value": value}
    if isinstance(value, str):
      return {"kind": "value", "type": "str", "value": _truncate_str(value)}
    oid = self._register(value)
    return {"kind": "ref", "type": type(value).__name__, "id": oid}

  def _frame_vars(self, frame):
    skip = {"math", "random"}
    result = {}
    for name, val in frame.f_locals.items():
      if name.startswith("_") or name in skip:
        continue
      result[name] = self._value_cell(val)
    return result

  def _frame_name(self, frame):
    name = frame.f_code.co_name
    if name == "<module>":
      return "программа"
    return name

  def _build_stack(self, frame):
    frames = []
    current = frame
    while current:
      if current.f_code.co_filename == "<user_code>":
        frames.append({
          "name": self._frame_name(current),
          "line": current.f_lineno,
          "vars": self._frame_vars(current),
        })
      current = current.f_back
    frames.reverse()
    return frames

  def _heap_entry(self, obj, depth=0):
    if depth > MAX_HEAP_DEPTH:
      return {"kind": "value", "type": type(obj).__name__, "value": "…"}

    if isinstance(obj, list):
      items = [self._value_cell(v, depth + 1) for v in obj[:MAX_LIST_ITEMS]]
      return {
        "kind": "list",
        "length": len(obj),
        "items": items,
        "truncated": len(obj) > MAX_LIST_ITEMS,
      }

    if isinstance(obj, tuple):
      items = [self._value_cell(v, depth + 1) for v in obj[:MAX_LIST_ITEMS]]
      return {
        "kind": "tuple",
        "length": len(obj),
        "items": items,
        "truncated": len(obj) > MAX_LIST_ITEMS,
      }

    if isinstance(obj, dict):
      entries = []
      for index, (key, val) in enumerate(obj.items()):
        if index >= MAX_DICT_ITEMS:
          break
        entries.append({
          "key": self._value_cell(key, depth + 1),
          "value": self._value_cell(val, depth + 1),
        })
      return {
        "kind": "dict",
        "length": len(obj),
        "entries": entries,
        "truncated": len(obj) > MAX_DICT_ITEMS,
      }

    if isinstance(obj, set):
      items = [self._value_cell(v, depth + 1) for v in list(obj)[:MAX_LIST_ITEMS]]
      return {
        "kind": "set",
        "length": len(obj),
        "items": items,
        "truncated": len(obj) > MAX_LIST_ITEMS,
      }

    return {
      "kind": "value",
      "type": type(obj).__name__,
      "value": _truncate_str(repr(obj)),
    }

  def _collect_refs(self, cell, bucket):
    if not isinstance(cell, dict):
      return
    if cell.get("kind") == "ref":
      oid = cell.get("id")
      if oid and oid not in bucket:
        bucket.add(oid)
    for key in ("items", "key", "value"):
      child = cell.get(key)
      if isinstance(child, dict):
        self._collect_refs(child, bucket)
      elif isinstance(child, list):
        for item in child:
          if isinstance(item, dict):
            if "key" in item and "value" in item:
              self._collect_refs(item["key"], bucket)
              self._collect_refs(item["value"], bucket)
            else:
              self._collect_refs(item, bucket)

  def _collect_refs_from_entry(self, entry, bucket):
    if not isinstance(entry, dict):
      return
    if entry.get("kind") == "ref":
      oid = entry.get("id")
      if oid:
        bucket.add(oid)
    for item in entry.get("items") or []:
      self._collect_refs_from_entry(item, bucket)
    for pair in entry.get("entries") or []:
      self._collect_refs_from_entry(pair.get("key"), bucket)
      self._collect_refs_from_entry(pair.get("value"), bucket)

  def _build_heap(self, stack):
    refs = set()
    for frame in stack:
      for cell in frame.get("vars", {}).values():
        self._collect_refs(cell, refs)

    expanded = set(refs)
    changed = True
    while changed:
      changed = False
      for oid in list(expanded):
        obj = self._obj_store.get(oid)
        if obj is None:
          continue
        entry = self._heap_entry(obj)
        nested = set()
        self._collect_refs_from_entry(entry, nested)
        for nid in nested:
          if nid not in expanded:
            expanded.add(nid)
            changed = True

    heap = {}
    for oid in sorted(expanded, key=lambda x: int(x.split("_")[1])):
      obj = self._obj_store.get(oid)
      if obj is not None:
        heap[oid] = self._heap_entry(obj)
    return heap

  def _changed_vars(self, stack):
    top_vars = stack[-1]["vars"] if stack else {}
    changed = []
    for name, cell in top_vars.items():
      if self._prev_top_vars.get(name) != cell:
        changed.append(name)
    for name in self._prev_top_vars:
      if name not in top_vars:
        changed.append(name)
    self._prev_top_vars = dict(top_vars)
    return sorted(set(changed))

  def _legacy_vars(self, frame):
    skip = {"math", "random"}
    result = {}
    for name, val in frame.f_locals.items():
      if name.startswith("_") or name in skip:
        continue
      result[name] = _legacy_value(val)
    return result

  def make_step(self, frame, event, line_blocks, stdout_capture):
    line_no = frame.f_lineno
    block_id = line_blocks.get(line_no)
    if not block_id:
      for ln in range(line_no, 0, -1):
        if ln in line_blocks:
          block_id = line_blocks[ln]
          break

    stack = self._build_stack(frame)
    heap = self._build_heap(stack)
    changed = self._changed_vars(stack)

    return {
      "line": line_no,
      "block_id": block_id,
      "event": event,
      "vars": self._legacy_vars(frame),
      "stack": stack,
      "heap": heap,
      "changed": changed,
      "output": stdout_capture.getvalue(),
    }


def main():
    stdout_capture = io.StringIO()
    steps = []
    pending_block = None
    line_blocks = {}
    src_lines = USER_CODE.splitlines()
    memory = MemoryTracer()

    for idx, line in enumerate(src_lines, start=1):
        stripped = line.strip()
        if stripped.startswith("# @block:"):
            pending_block = stripped[9:].strip().strip("'\"")
        elif pending_block and stripped and not stripped.startswith("#"):
            line_blocks[idx] = pending_block
            pending_block = None

    def trace(frame, event, arg):
        if frame.f_code.co_filename != "<user_code>":
            return trace
        if event not in ("line", "call", "return"):
            return trace
        if event == "call" and frame.f_code.co_name == "<module>":
            return trace

        steps.append(memory.make_step(frame, event, line_blocks, stdout_capture))
        if len(steps) >= __MAX_STEPS__:
            raise SystemExit("MAX_STEPS")
        return trace

    globals_env = {
        "__name__": "__main__",
        "__builtins__": __builtins__,
        "math": math,
        "random": random,
    }

    error = None
    finished = False
    sys.settrace(trace)
    try:
        with redirect_stdout(stdout_capture):
            exec(compile(USER_CODE, "<user_code>", "exec"), globals_env)
        finished = True
    except SystemExit as exc:
        if str(exc) != "MAX_STEPS":
            error = str(exc)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    finally:
        sys.settrace(None)

    if finished and steps:
        last = steps[-1]
        if last.get("output") != stdout_capture.getvalue():
            steps.append({
                **last,
                "output": stdout_capture.getvalue(),
                "finished": True,
                "changed": [],
            })
    elif finished and not steps:
        steps.append({
            "line": 1,
            "block_id": None,
            "event": "line",
            "vars": {},
            "stack": [{"name": "программа", "line": 1, "vars": {}}],
            "heap": {},
            "changed": [],
            "output": stdout_capture.getvalue(),
            "finished": True,
        })

    print(json.dumps({"steps": steps, "error": error, "finished": finished}, ensure_ascii=False))

if __name__ == "__main__":
    main()
'''


def debug_python_code(code: str, stdin_text: str = "") -> dict:
    """Собирает шаги выполнения программы."""
    validation_error = validate_code(code)
    if validation_error:
        return {"success": False, "steps": [], "error": validation_error}

    runner_source = (
        TRACE_RUNNER.replace("__CODE__", repr(code)).replace("__MAX_STEPS__", str(MAX_STEPS))
    )

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        tmp.write(runner_source)
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

        raw = result.stdout.strip()
        if not raw:
            err = result.stderr.strip() or "Пустой ответ трассировщика"
            return {"success": False, "steps": [], "error": err}

        if len(raw) > MAX_OUTPUT_CHARS:
            raw = raw[:MAX_OUTPUT_CHARS]

        try:
            payload = json.loads(raw.splitlines()[-1])
        except json.JSONDecodeError:
            return {
                "success": False,
                "steps": [],
                "error": "Ошибка разбора трассировки",
                "output": raw,
            }

        if payload.get("error"):
            return {
                "success": False,
                "steps": payload.get("steps", []),
                "error": payload["error"],
                "output": payload.get("steps", [{}])[-1].get("output", "") if payload.get("steps") else "",
            }

        if result.returncode != 0 and not payload.get("steps"):
            return {
                "success": False,
                "steps": [],
                "error": result.stderr.strip() or "Ошибка трассировки",
            }

        return {
            "success": True,
            "steps": payload.get("steps", []),
            "error": None,
            "finished": payload.get("finished", True),
        }

    except ExecutionPoolBusy as exc:
        return {"success": False, "steps": [], "error": str(exc), "overloaded": True}
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "steps": [],
            "error": f"Превышено время выполнения ({EXECUTION_TIMEOUT} сек.)",
        }
    except Exception as exc:
        return {"success": False, "steps": [], "error": str(exc)}
    finally:
        Path(tmp_path).unlink(missing_ok=True)

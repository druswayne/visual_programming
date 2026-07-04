"""Генерация starter_xml для задач «исправь код» из сломанного Python."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from data.fix_tasks_defs import FIX_TASK_DEFS
from data.tasks.conditions import TASKS as CONDITIONS_TASKS
from data.tasks.for_loop import TASKS as FOR_TASKS
from data.tasks.io import TASKS as IO_TASKS
from data.tasks.lists import TASKS as LISTS_TASKS
from data.tasks.numbers import TASKS as NUMBERS_TASKS
from data.tasks.strings import TASKS as STRINGS_TASKS
from data.tasks.while_loop import TASKS as WHILE_TASKS
from runner.checker import check_solution
from runner.python_to_blocks import python_to_blocks
from scripts.task_references import REFERENCE_SOLUTIONS

BASE_TASKS = {
    "io": IO_TASKS,
    "numbers": NUMBERS_TASKS,
    "conditions": CONDITIONS_TASKS,
    "while": WHILE_TASKS,
    "for": FOR_TASKS,
    "strings": STRINGS_TASKS,
    "lists": LISTS_TASKS,
}


def _find_task(topic_id: str, task_id: str) -> dict:
    for item in BASE_TASKS[topic_id]:
        if item["id"] == task_id:
            return item
    raise KeyError(f"task not found: {topic_id}/{task_id}")


def build_starters() -> dict[str, str]:
  errors: list[str] = []
  starters: dict[str, str] = {}

  for topic_id, defs in FIX_TASK_DEFS.items():
    for item in defs:
      fix_id = item["id"]
      base_id = item["based_on"]
      buggy = item["buggy_code"]
      correct = REFERENCE_SOLUTIONS.get(base_id)
      if not correct:
        errors.append(f"{fix_id}: нет эталона для {base_id}")
        continue

      base_task = _find_task(topic_id, base_id)
      tests = base_task["tests"]

      buggy_result = check_solution(buggy, tests)
      if buggy_result["success"]:
        errors.append(f"{fix_id}: сломанный код проходит тесты — нужна другая ошибка")

      correct_result = check_solution(correct, tests)
      if not correct_result["success"]:
        errors.append(
          f"{fix_id}: эталон {base_id} не проходит тесты — {correct_result['message']}"
        )
        continue

      try:
        xml = python_to_blocks(buggy)["xml"]
      except Exception as exc:
        errors.append(f"{fix_id}: не удалось собрать XML — {exc}")
        continue

      starters[fix_id] = xml

  if errors:
    print("ОШИБКИ:")
    for err in errors:
      print(" ", err)
    raise SystemExit(1)

  return starters


def write_task_starters(starters: dict[str, str]) -> None:
  out = ROOT / "data" / "task_starters.py"
  lines = [
    '"""Стартовые Blockly XML для задач «исправь код». Сгенерировано build_fix_tasks.py."""',
    "",
    "STARTER_XML = {",
  ]
  for fix_id in sorted(starters):
    xml = starters[fix_id]
    lines.append(f'    "{fix_id}": """{xml}""",')
  lines.append("}")
  lines.append("")
  out.write_text("\n".join(lines), encoding="utf-8")
  print(f"Записано {len(starters)} стартовых XML в {out}")


if __name__ == "__main__":
  write_task_starters(build_starters())

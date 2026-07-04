"""Полная проверка всех задач по эталонным решениям."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from data.registry import TASKS_BY_TOPIC, get_topics
from runner.checker import check_solution
from scripts.task_references import REFERENCE_SOLUTIONS


def main():
    errors = []
    missing = []
    total = 0

    for topic in get_topics():
        for task in TASKS_BY_TOPIC[topic["id"]]:
            total += 1
            tid = task["id"]
            code = REFERENCE_SOLUTIONS.get(tid)
            if not code:
                missing.append(tid)
                continue
            result = check_solution(code, task["tests"])
            if not result["success"]:
                errors.append({"id": tid, "title": task["title"], "result": result})

    print(f"Всего задач: {total}")
    print(f"Эталонов: {len(REFERENCE_SOLUTIONS)}")
    print(f"Без эталона: {len(missing)}")
    print(f"Ошибок проверки: {len(errors)}")
    print()

    for e in errors:
        print(f"FAIL {e['id']}: {e['title']}")
        for d in e["result"].get("details", []):
            if not d.get("passed"):
                print(f"  test {d['index']}: {d.get('message')}")
                if "expected" in d:
                    print(f"    expected: {d['expected']!r}")
                    print(f"    actual:   {d['actual']!r}")
        print()

    return 1 if errors or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

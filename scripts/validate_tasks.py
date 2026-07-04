"""Проверка задач: структура, тесты и эталонные решения."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from data.registry import TASKS_BY_TOPIC, get_topics
from runner.checker import check_solution, normalize_output
from runner.sandbox import run_python_code

# Эталонные решения (минимальный Python, эквивалент блоков)
REFERENCE = {
    "io-01": 'print("Привет, мир!")',
    "io-02": 'print("Аня")',
    "io-03": 'print("Школа")',
    "io-04": 'предмет = "информатика"\nprint(предмет)',
    "io-05": 'город = "Казань"\nprint(город)',
    "io-06": 'print("Привет!")\nprint("Как дела?")',
    "io-07": 'print("Раз")\nprint("Два")\nprint("Три")',
    "io-08": 'print("Я учу Python")',
    "io-09": 'имя = input()\nprint("Привет, " + имя)',
    "io-10": 'print(input())',
    "io-11": 'город = input()\nprint(город)',
    "io-12": 'print(input())\nprint(input())',
    "io-13": 'x = input()\nprint(x)\nprint(x)',
    "io-14": 'print(input())\nprint(input())',
    "io-15": 'слово = input()\nprint(слово)',
    "io-16": 'print("Беги!")\nprint("Беги!")',
    "io-17": 'print("— Привет!")\nprint("— Привет!")\nprint("— Пойдём гулять?")',
    "io-18": 'print("Герой")\nprint("смелый")',
    "io-19": 'имя = input()\nprint("Рад тебя видеть, " + имя + "!")',
    "io-20": 'print(input())\nprint(input())\nprint("Удачи в учёбе!")',
}


def validate_structure():
    errors = []
    for topic in get_topics():
        tid = topic["id"]
        tasks = TASKS_BY_TOPIC.get(tid, [])
        if len(tasks) < 15:
            errors.append(f"{tid}: мало задач ({len(tasks)})")
        for task in tasks:
            if not task.get("id"):
                errors.append(f"{tid}: задача без id")
            if not task.get("title"):
                errors.append(f"{tid}: {task.get('id')} без title")
            if not task.get("condition"):
                errors.append(f"{tid}: {task.get('id')} без condition")
            tests = task.get("tests") or []
            if not tests:
                errors.append(f"{tid}: {task.get('id')} без тестов")
            for i, test in enumerate(tests):
                if "expected_output" not in test:
                    errors.append(f"{tid}: {task.get('id')} тест {i+1} без expected_output")
    return errors


def validate_references():
    errors = []
    missing = []
    for topic_id, tasks in TASKS_BY_TOPIC.items():
        for task in tasks:
            tid = task["id"]
            code = REFERENCE.get(tid)
            if not code:
                missing.append(tid)
                continue
            result = check_solution(code, task["tests"])
            if not result["success"]:
                errors.append(
                    f"{tid} ({task['title']}): эталон не прошёл — {result['message']}"
                )
                for d in result.get("details", []):
                    if not d.get("passed"):
                        errors.append(
                            f"  тест {d['index']}: expected={d.get('expected')!r} actual={d.get('actual')!r} err={d.get('message')}"
                        )
    return errors, missing


def smoke_test_outputs():
    """Проверка, что expected_output сам по себе достижим через print."""
    errors = []
    for topic_id, tasks in TASKS_BY_TOPIC.items():
        for task in tasks:
            for i, test in enumerate(task["tests"]):
                expected = test["expected_output"]
                lines = expected.split("\n")
                code = "\n".join(f'print({line!r})' for line in lines)
                result = run_python_code(code, stdin_text=test.get("stdin", ""))
                actual = normalize_output(result.get("output", ""))
                exp_norm = normalize_output(expected)
                if actual != exp_norm:
                    errors.append(
                        f"{task['id']} test {i+1}: print-smoke failed {exp_norm!r} vs {actual!r}"
                    )
    return errors


if __name__ == "__main__":
    print("=== Структура ===")
    struct_errs = validate_structure()
    print(f"Ошибок: {len(struct_errs)}")
    for e in struct_errs[:20]:
        print(" ", e)

    print("\n=== Smoke print ===")
    smoke = smoke_test_outputs()
    print(f"Ошибок: {len(smoke)}")
    for e in smoke[:20]:
        print(" ", e)

    print("\n=== Эталоны (частично) ===")
    ref_errs, missing = validate_references()
    print(f"Эталонов: {len(REFERENCE)}, без эталона: {len(missing)}, ошибок: {len(ref_errs)}")
    for e in ref_errs[:30]:
        print(" ", e)

"""Общие хелперы для описания задач."""

import re

DIFFICULTY_EASY = "easy"
DIFFICULTY_MEDIUM = "medium"
DIFFICULTY_HARD = "hard"
VALID_DIFFICULTIES = (DIFFICULTY_EASY, DIFFICULTY_MEDIUM, DIFFICULTY_HARD)

# Нумерация обычных задач в теме: 01–10 легко, 11–22 средне, 23+ сложно.
_EASY_MAX = 10
_MEDIUM_MAX = 22
_TASK_NUMBER = re.compile(r"(\d+)$")


def infer_difficulty(task_id: str, based_on: str | None = None) -> str:
    """Уровень сложности по номеру задачи в теме."""
    source = based_on or task_id or ""
    match = _TASK_NUMBER.search(source)
    number = int(match.group(1)) if match else 1
    if number <= _EASY_MAX:
        return DIFFICULTY_EASY
    if number <= _MEDIUM_MAX:
        return DIFFICULTY_MEDIUM
    return DIFFICULTY_HARD


def task(
    task_id,
    title,
    condition,
    tests,
    hint=None,
    starter_xml=None,
    difficulty=None,
    based_on=None,
):
    item = {
        "id": task_id,
        "title": title,
        "condition": condition,
        "tests": tests,
        "difficulty": difficulty or infer_difficulty(task_id, based_on),
    }
    if hint:
        item["hint"] = hint
    if starter_xml:
        item["starter_xml"] = starter_xml
    return item

"""Общие хелперы для описания задач."""

from data.task_difficulty import (
    DIFFICULTY_EASY,
    DIFFICULTY_HARD,
    DIFFICULTY_MEDIUM,
    VALID_DIFFICULTIES,
    infer_difficulty,
)

__all__ = [
    "DIFFICULTY_EASY",
    "DIFFICULTY_HARD",
    "DIFFICULTY_MEDIUM",
    "VALID_DIFFICULTIES",
    "infer_difficulty",
    "task",
]


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

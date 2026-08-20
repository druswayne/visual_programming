"""Сборка задач «исправь код» для подключения к темам."""

from __future__ import annotations

from data.fix_tasks_defs import FIX_TASK_DEFS
from data.task_starters import STARTER_XML
from data.tasks.common import task


def merge_fix_tasks(topic_id: str, base_tasks: list[dict]) -> list[dict]:
    """Вставляет fix-задачи сразу перед связанными обычными задачами."""
    fix_by_base = {
        item["based_on"]: item for item in FIX_TASK_DEFS.get(topic_id, [])
    }
    merged: list[dict] = []
    for base in base_tasks:
        fix_def = fix_by_base.get(base["id"])
        if fix_def:
            starter = STARTER_XML.get(fix_def["id"])
            if not starter:
                raise KeyError(f"starter_xml not found: {fix_def['id']}")
            merged.append(
                task(
                    fix_def["id"],
                    fix_def["title"],
                    fix_def["condition"],
                    base["tests"],
                    hint=fix_def["hint"],
                    starter_xml=starter,
                    difficulty=base.get("difficulty"),
                    based_on=fix_def["based_on"],
                )
            )
        merged.append(base)
    return merged

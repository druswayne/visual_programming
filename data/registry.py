"""Реестр тем и задач PyBlocks."""

import re

from data.fix_tasks import merge_fix_tasks
from data.task_difficulty import sort_tasks_by_difficulty
from data.tasks.io import TASKS as IO_TASKS
from data.tasks.numbers import TASKS as NUMBERS_TASKS
from data.tasks.conditions import TASKS as CONDITIONS_TASKS
from data.tasks.while_loop import TASKS as WHILE_TASKS
from data.tasks.for_loop import TASKS as FOR_TASKS
from data.tasks.strings import TASKS as STRINGS_TASKS
from data.tasks.lists import TASKS as LISTS_TASKS

TOPICS = [
    {
        "id": "io",
        "title": "Ввод и вывод",
        "description": (
            "Ввод и вывод данных, сохранение в переменные и использование "
            "значений из переменных."
        ),
    },
    {
        "id": "numbers",
        "title": "Числа и операции",
        "description": (
            "Целые и дробные числа, сложение, вычитание, умножение, деление, "
            "степень, остаток и целочисленное деление."
        ),
    },
    {
        "id": "conditions",
        "title": "Условные конструкции",
        "description": (
            "if…else, if…elif…else, простые и составные условия, "
            "логические величины."
        ),
    },
    {
        "id": "while",
        "title": "Цикл while",
        "description": "Цикл «пока»: повторение, пока условие истинно.",
    },
    {
        "id": "for",
        "title": "Цикл for",
        "description": "Перебор последовательностей, функция range для чисел.",
    },
    {
        "id": "strings",
        "title": "Строки",
        "description": "Строковые величины и базовые методы работы с ними.",
    },
    {
        "id": "lists",
        "title": "Списки",
        "description": "Списки и базовые методы работы с ними.",
    },
]

TASKS_BY_TOPIC = {
    "io": sort_tasks_by_difficulty(merge_fix_tasks("io", IO_TASKS)),
    "numbers": sort_tasks_by_difficulty(merge_fix_tasks("numbers", NUMBERS_TASKS)),
    "conditions": sort_tasks_by_difficulty(merge_fix_tasks("conditions", CONDITIONS_TASKS)),
    "while": sort_tasks_by_difficulty(merge_fix_tasks("while", WHILE_TASKS)),
    "for": sort_tasks_by_difficulty(merge_fix_tasks("for", FOR_TASKS)),
    "strings": sort_tasks_by_difficulty(merge_fix_tasks("strings", STRINGS_TASKS)),
    "lists": sort_tasks_by_difficulty(merge_fix_tasks("lists", LISTS_TASKS)),
}


def get_topics():
    from data.localized import get_localized_topics

    return get_localized_topics()


def plain_text(value: str) -> str:
    if not value:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"</?code>", "", text, flags=re.IGNORECASE)
    return re.sub(r"<[^>]+>", "", text).strip()


def get_tasks_public(topic_id: str):
    """Список задач без тестов (для клиента)."""
    from data.localized import get_localized_tasks_public

    return get_localized_tasks_public(topic_id)


def get_task_with_tests(topic_id: str, task_id: str):
    from data.localized import get_localized_task_with_tests

    return get_localized_task_with_tests(topic_id, task_id)

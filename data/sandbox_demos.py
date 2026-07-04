"""Готовые примеры для быстрого старта в песочнице."""

from data.guide_xml import HELLO_WORLD, LANDING_DEMO, NUMS_ADD

SANDBOX_DEMOS = {
    "hello": {
        "id": "hello",
        "title": "Hello, world!",
        "description": "Самая первая программа — один блок «вывести»",
        "xml": HELLO_WORLD,
    },
    "greet": {
        "id": "greet",
        "title": "Приветствие",
        "description": "Переменная и вывод текста",
        "xml": LANDING_DEMO,
    },
    "calc": {
        "id": "calc",
        "title": "Сложение",
        "description": "Математика: 7 + 5",
        "xml": NUMS_ADD,
    },
}

LANDING_TOPIC_META = {
    "io": {"icon": "⌨️", "level": "для начинающих", "highlight": False},
    "numbers": {"icon": "🔢", "level": "для начинающих", "highlight": False},
    "conditions": {"icon": "🔀", "level": "базовый уровень", "highlight": False},
    "while": {"icon": "🔁", "level": "базовый уровень", "highlight": False},
    "for": {"icon": "🔄", "level": "средний уровень", "highlight": False},
    "strings": {"icon": "📝", "level": "средний уровень", "highlight": False},
    "lists": {"icon": "📋", "level": "продвинутый", "highlight": True},
}


def get_sandbox_demo(demo_id: str) -> dict | None:
    return SANDBOX_DEMOS.get(demo_id)


def get_sandbox_demos_public() -> list[dict]:
    return [
        {key: value for key, value in demo.items() if key != "xml"}
        for demo in SANDBOX_DEMOS.values()
    ]

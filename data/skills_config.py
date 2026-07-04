"""Конфигурация дерева навыков, привязанного к темам курса PyBlocks."""

from data.registry import TOPICS

# Порядок прохождения курса (совпадает с редактором)
TOPIC_ORDER = [t["id"] for t in TOPICS]

TOPIC_META: dict[str, dict] = {
    "io": {
        "icon": "📥",
        "color": "#3b82f6",
        "skill_label": "Основы ввода-вывода",
    },
    "numbers": {
        "icon": "🔢",
        "color": "#6366f1",
        "skill_label": "Числа и вычисления",
    },
    "conditions": {
        "icon": "🔀",
        "color": "#8b5cf6",
        "skill_label": "Ветвление программы",
    },
    "while": {
        "icon": "🔁",
        "color": "#a855f7",
        "skill_label": "Циклы «пока»",
    },
    "for": {
        "icon": "🔄",
        "color": "#d946ef",
        "skill_label": "Перебор и range",
    },
    "strings": {
        "icon": "📝",
        "color": "#ec4899",
        "skill_label": "Работа со строками",
    },
    "lists": {
        "icon": "📋",
        "color": "#f43f5e",
        "skill_label": "Списки и коллекции",
    },
}

# Пороги звёзд — доля решённых задач в теме
STAR_THRESHOLDS = [0.0, 0.06, 0.25, 0.50, 0.80, 1.0]

# Разблокировка тем между разделами — topic_unlock_service (50% предыдущей темы)

# Машина времени: ★★ в «Условиях» (~7 задач, база для трассировки ветвлений)
TIME_MACHINE_TOPIC = "conditions"
TIME_MACHINE_MIN_LEVEL = 2

LEGACY_BRANCH_IDS = frozenset(
    {
        "algorithms",
        "code_reading",
        "debugging",
        "refactoring",
        "flow_design",
        "metacognition",
    }
)

LEGACY_MEDAL_IDS = frozenset({"debugger", "style", "design", "clarity"})

MEDAL_DEFS = [
    {
        "id": "fix_master",
        "title": "Исправления",
        "icon": "🔧",
        "description": "Задачи «Исправь код»",
    },
    {
        "id": "clean_solve",
        "title": "С первой попытки",
        "icon": "⚡",
        "description": "Решено без ошибок с первого раза",
    },
    {
        "id": "topics_done",
        "title": "Темы освоены",
        "icon": "👑",
        "description": "Темы пройдены на 100%",
    },
]

LEVEL_NAMES = ["", "Новичок", "Практик", "Эксперт", "Мастер", "Гуру"]


def build_skill_branches() -> list[dict]:
    """Ветки дерева — одна на каждую тему курса."""
    branches = []
    for topic in TOPICS:
        meta = TOPIC_META[topic["id"]]
        branches.append(
            {
                "id": topic["id"],
                "title": topic["title"],
                "description": topic["description"],
                "skill_label": meta["skill_label"],
                "icon": meta["icon"],
                "color": meta["color"],
            }
        )
    return branches

"""English translations for skills tree configuration."""

from __future__ import annotations

LEVEL_NAMES = ["", "Novice", "Practitioner", "Expert", "Master", "Guru"]

TOPIC_META_EN: dict[str, dict] = {
    "io": {"skill_label": "Input/output basics"},
    "numbers": {"skill_label": "Numbers and calculations"},
    "conditions": {"skill_label": "Program branching"},
    "while": {"skill_label": "while loops"},
    "for": {"skill_label": "Iteration and range"},
    "strings": {"skill_label": "Working with strings"},
    "lists": {"skill_label": "Lists and collections"},
}

MEDAL_DEFS_EN: dict[str, dict] = {
    "fix_master": {
        "title": "Fixes",
        "description": "«Fix the code» tasks",
    },
    "clean_solve": {
        "title": "First try",
        "description": "Solved without errors on the first attempt",
    },
    "topics_done": {
        "title": "Topics mastered",
        "description": "Topics completed at 100%",
    },
}

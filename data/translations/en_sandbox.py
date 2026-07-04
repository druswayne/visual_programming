"""English translations for sandbox demos and landing topic meta."""

from __future__ import annotations

from data.guide_xml import LANDING_DEMO_EN

SANDBOX_EN: dict[str, dict] = {
    "hello": {
        "title": "Hello, world!",
        "description": "The very first program — a single «print» block",
    },
    "greet": {
        "title": "Greeting",
        "description": "A variable and text output",
        "xml": LANDING_DEMO_EN,
    },
    "calc": {
        "title": "Addition",
        "description": "Math: 7 + 5",
    },
}

LANDING_META_EN: dict[str, dict] = {
    "io": {"level": "for beginners"},
    "numbers": {"level": "for beginners"},
    "conditions": {"level": "basic level"},
    "while": {"level": "basic level"},
    "for": {"level": "intermediate level"},
    "strings": {"level": "intermediate level"},
    "lists": {"level": "advanced"},
}

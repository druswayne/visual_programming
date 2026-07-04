"""Локализованный доступ к темам, задачам и материалам."""

from __future__ import annotations

from copy import deepcopy

from i18n import get_locale

from data.registry import TASKS_BY_TOPIC, TOPICS, plain_text
from data.translations.en_tasks import TASKS_EN
from data.translations.en_topics import TOPICS_EN
from data.translations.en_guides import GUIDES_EN
from data.sandbox_demos import LANDING_TOPIC_META, SANDBOX_DEMOS
from data.translations.en_sandbox import SANDBOX_EN, LANDING_META_EN


def _pick_text(value, locale: str):
    if isinstance(value, dict) and ("ru" in value or "en" in value):
        return value.get(locale) or value.get("ru") or value.get("en") or ""
    return value


def localize_topic(topic: dict, locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc == "en":
        overlay = TOPICS_EN.get(topic["id"], {})
        meta = LANDING_META_EN.get(topic["id"], LANDING_TOPIC_META.get(topic["id"], {}))
    else:
        overlay = {}
        meta = LANDING_TOPIC_META.get(topic["id"], {})
    result = {**topic, **overlay}
    if meta:
        result["level"] = meta.get("level", result.get("level", ""))
        result["icon"] = meta.get("icon", result.get("icon", "📘"))
        result["highlight"] = meta.get("highlight", result.get("highlight", False))
    return result


def get_localized_topics(locale: str | None = None) -> list[dict]:
    return [localize_topic(topic, locale) for topic in TOPICS]


def localize_task(task: dict, locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc != "en":
        return task
    overlay = TASKS_EN.get(task["id"])
    if not overlay:
        return task
    merged = {**task, **overlay}
    if "tests" in overlay:
        merged["tests"] = overlay["tests"]
    return merged


def get_localized_tasks_public(topic_id: str, locale: str | None = None) -> list[dict]:
    tasks = TASKS_BY_TOPIC.get(topic_id, [])
    loc = locale or get_locale()
    starter_xml_en = None
    if loc == "en":
        from data.task_starters_en import STARTER_XML_EN

        starter_xml_en = STARTER_XML_EN
    result = []
    for task in tasks:
        localized = localize_task(task, loc)
        starter_xml = task.get("starter_xml")
        if starter_xml and starter_xml_en is not None:
            starter_xml = starter_xml_en.get(task["id"], starter_xml)
        result.append(
            {
                "id": task["id"],
                "title": localized["title"],
                "condition": plain_text(localized["condition"]),
                "hint": plain_text(localized.get("hint") or "") or None,
                "starter_xml": starter_xml,
            }
        )
    return result


def get_localized_task_with_tests(topic_id: str, task_id: str, locale: str | None = None):
    for task in TASKS_BY_TOPIC.get(topic_id, []):
        if task["id"] == task_id:
            return localize_task(task, locale)
    return None


def get_localized_topic_guide(topic_id: str, locale: str | None = None):
    from data.topic_guides import TOPIC_GUIDES

    guide = TOPIC_GUIDES.get(topic_id)
    if not guide:
        return None
    loc = locale or get_locale()
    if loc == "en":
        overlay = GUIDES_EN.get(topic_id)
        if overlay:
            return {"id": topic_id, **overlay}
    return {"id": topic_id, **guide}


def get_localized_sandbox_demo(demo_id: str, locale: str | None = None) -> dict | None:
    demo = SANDBOX_DEMOS.get(demo_id)
    if not demo:
        return None
    loc = locale or get_locale()
    if loc == "en":
        overlay = SANDBOX_EN.get(demo_id, {})
        return {**demo, **overlay}
    return demo

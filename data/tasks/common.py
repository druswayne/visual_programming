"""Общие хелперы для описания задач."""


def task(task_id, title, condition, tests, hint=None, starter_xml=None):
    item = {
        "id": task_id,
        "title": title,
        "condition": condition,
        "tests": tests,
    }
    if hint:
        item["hint"] = hint
    if starter_xml:
        item["starter_xml"] = starter_xml
    return item

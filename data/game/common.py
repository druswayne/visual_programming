"""Хелпер описания игровой миссии."""

from game.world import world_dict

__all__ = ["mission", "world_dict"]


def mission(
    mission_id: str,
    track: str,
    title: str,
    condition: str,
    goal: dict | list,
    hint: str | None = None,
    worlds: list[dict] | None = None,
    generator: dict | None = None,
    toolbox: str | None = None,
):
    item = {
        "id": mission_id,
        "track": track,
        "title": title,
        "condition": condition,
        "goal": goal,
        "toolbox": toolbox or track,
    }
    if hint:
        item["hint"] = hint
    if worlds:
        item["worlds"] = worlds
    if generator:
        item["generator"] = generator
    return item

"""Реестр линеек и миссий игрового режима."""

from __future__ import annotations

from copy import deepcopy

from data.game.missions_conditions import MISSIONS as CONDITIONS_MISSIONS
from data.game.missions_linear import MISSIONS as LINEAR_MISSIONS
from data.game.missions_loops import MISSIONS as LOOPS_MISSIONS
from game.generators import generate_world, generate_worlds
from game.unlock import TRACK_ORDER, TRACK_TOPIC_IDS, get_unlock_info, is_track_unlocked
from game.world import World
from i18n import get_locale

TRACKS = [
    {
        "id": "linear",
        "title": "Последовательность",
        "description": "Соберите цепочку команд: ходы, закраска, предметы и коробки.",
    },
    {
        "id": "conditions",
        "title": "Условия",
        "description": "Карта каждый раз другая — нужны if и датчики робота.",
    },
    {
        "id": "loops",
        "title": "Циклы",
        "description": "Повторяйте действия через for и while, пока не выполнена цель.",
    },
]

MISSIONS_BY_TRACK = {
    "linear": LINEAR_MISSIONS,
    "conditions": CONDITIONS_MISSIONS,
    "loops": LOOPS_MISSIONS,
}

_MISSIONS_BY_ID = {item["id"]: item for items in MISSIONS_BY_TRACK.values() for item in items}


def get_track(track_id: str) -> dict | None:
    for track in TRACKS:
        if track["id"] == track_id:
            return track
    return None


def get_mission(mission_id: str) -> dict | None:
    mission = _MISSIONS_BY_ID.get(mission_id)
    return deepcopy(mission) if mission else None


def localize_track(track: dict, locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc != "en":
        return dict(track)
    from data.translations.en_game import TRACKS_EN

    overlay = TRACKS_EN.get(track["id"], {})
    return {**track, **overlay}


def localize_mission(mission: dict, locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc != "en":
        return deepcopy(mission)
    from data.translations.en_game import MISSIONS_EN

    overlay = MISSIONS_EN.get(mission["id"], {})
    merged = {**mission, **overlay}
    return deepcopy(merged)


def track_totals() -> dict[str, int]:
    return {track_id: len(items) for track_id, items in MISSIONS_BY_TRACK.items()}


def track_titles(locale: str | None = None) -> dict[str, str]:
    return {track["id"]: localize_track(track, locale)["title"] for track in TRACKS}


def list_tracks_for_user(user_id: int | None) -> list[dict]:
    totals = track_totals()
    titles = track_titles()
    result = []
    for track in TRACKS:
        info = get_unlock_info(user_id, track["id"], totals, titles)
        localized = localize_track(track)
        result.append(
            {
                **localized,
                "mission_count": totals.get(track["id"], 0),
                "topic_id": TRACK_TOPIC_IDS[track["id"]],
                **info,
            }
        )
    return result


def public_mission(mission: dict) -> dict:
    localized = localize_mission(mission)
    return {
        "id": localized["id"],
        "track": localized["track"],
        "title": localized["title"],
        "condition": localized["condition"],
        "hint": localized.get("hint"),
        "toolbox": localized.get("toolbox") or localized["track"],
        "goal": localized["goal"],
        "has_generator": bool(localized.get("generator")),
    }


def list_missions_public(track_id: str) -> list[dict]:
    items = MISSIONS_BY_TRACK.get(track_id) or []
    return [public_mission(item) for item in items]


def resolve_worlds(mission: dict) -> list[dict]:
    if mission.get("generator"):
        return generate_worlds(mission["generator"])
    return [deepcopy(world) for world in (mission.get("worlds") or [])]


def sample_world(mission: dict, seed: int = 1) -> dict:
    if mission.get("generator"):
        return generate_world(mission["generator"], seed)
    worlds = mission.get("worlds") or []
    if not worlds:
        raise ValueError("mission has no worlds")
    index = (max(seed, 1) - 1) % len(worlds)
    return deepcopy(worlds[index])


def public_world(data: dict) -> dict:
    return World(data).to_public_dict()


def is_mission_track_unlocked(user_id: int | None, track_id: str) -> bool:
    return is_track_unlocked(user_id, track_id, track_totals())

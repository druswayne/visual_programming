"""Генераторы вариантов карт: каждый seed — отдельный тип, без «пустых» карт."""

from __future__ import annotations

from typing import Any, Callable

from game.world import world_dict

GeneratorFn = Callable[[dict, int], dict[str, Any]]


def _variant(seed: int, count: int) -> int:
    return (max(int(seed), 1) - 1) % max(count, 1)


def gen_detour(params: dict, seed: int) -> dict[str, Any]:
    """Вперёд стена — обход сверху; вперёд свободно — сверху тупик. Край карты — невидимая стена."""
    if _variant(seed, 2) == 0:
        return world_dict(5, 2, (0, 1), finish=(4, 1), walls=[[1, 1]])
    return world_dict(5, 2, (0, 1), finish=(4, 1), walls=[[0, 0], [1, 0], [2, 0], [3, 0]])


def gen_finish_side(params: dict, seed: int) -> dict[str, Any]:
    if _variant(seed, 2) == 0:
        return world_dict(5, 1, (2, 0), finish=(4, 0), walls=[[1, 0]])
    return world_dict(5, 1, (2, 0), finish=(0, 0), walls=[[3, 0]])


def gen_open_vertical(params: dict, seed: int) -> dict[str, Any]:
    if _variant(seed, 2) == 0:
        return world_dict(1, 5, (0, 2), finish=(0, 0), walls=[[0, 3]])
    return world_dict(1, 5, (0, 2), finish=(0, 4), walls=[[0, 1]])


def gen_item_one_of_two(params: dict, seed: int) -> dict[str, Any]:
    cells = [[1, 0], [3, 0]]
    chosen = cells[_variant(seed, 2)]
    return world_dict(5, 1, (0, 0), items=[chosen], paint_targets=[chosen])


def gen_item_maybe(params: dict, seed: int) -> dict[str, Any]:
    items = [[1, 0]] if _variant(seed, 2) == 0 else []
    return world_dict(5, 1, (0, 0), finish=(4, 0), items=items)


def gen_box_or_around(params: dict, seed: int) -> dict[str, Any]:
    if _variant(seed, 2) == 0:
        return world_dict(
            5,
            2,
            (0, 1),
            finish=(4, 1),
            boxes=[[1, 1]],
            walls=[[2, 1]],
        )
    return world_dict(5, 2, (0, 1), finish=(4, 1), walls=[[0, 0], [1, 0], [2, 0], [3, 0]])


def gen_item_and_wall(params: dict, seed: int) -> dict[str, Any]:
    idx = _variant(seed, 4)
    has_item = idx in (0, 1)
    has_wall = idx in (0, 2)
    items = [[1, 1]] if has_item else []
    if has_wall:
        walls = [[2, 1]]
    else:
        walls = [[1, 0], [2, 0], [3, 0], [4, 0]]
    return world_dict(6, 2, (0, 1), finish=(5, 1), walls=walls, items=items)


def gen_paint_signal(params: dict, seed: int) -> dict[str, Any]:
    if _variant(seed, 2) == 0:
        return world_dict(6, 1, (0, 0), painted=[[1, 0]], paint_targets=[[3, 0]])
    return world_dict(6, 1, (0, 0), paint_targets=[[1, 0]])


def gen_alcove_gem(params: dict, seed: int) -> dict[str, Any]:
    """Кристалл в верхней или нижней нише — взять и дойти до финиша."""
    if _variant(seed, 2) == 0:
        return world_dict(
            5,
            3,
            (0, 1),
            finish=(4, 1),
            items=[[2, 0]],
            walls=[[2, 2], [1, 2], [3, 2]],
        )
    return world_dict(
        5,
        3,
        (0, 1),
        finish=(4, 1),
        items=[[2, 2]],
        walls=[[2, 0], [1, 0], [3, 0]],
    )


def _corridor_length(params: dict, seed: int) -> int:
    min_len = int(params.get("min", 3))
    max_len = int(params.get("max", 7))
    choices = [min_len, max_len]
    mid = (min_len + max_len) // 2
    if mid not in choices:
        choices.append(mid)
    extra = min_len + 1
    if extra not in choices and extra < max_len:
        choices.append(extra)
    return choices[_variant(seed, len(choices))]


def gen_corridor_length(params: dict, seed: int) -> dict[str, Any]:
    """Один ряд: край карты справа — невидимая стена."""
    length = _corridor_length(params, seed)
    return world_dict(length, 1, (0, 0), finish=(length - 1, 0))


def gen_paint_corridor(params: dict, seed: int) -> dict[str, Any]:
    world = gen_corridor_length(params, seed)
    start_x, start_y = world["start"]
    finish = world["finish"]
    world["paint_targets"] = [[x, start_y] for x in range(start_x + 1, finish[0] + 1)]
    return world


def gen_item_at_end(params: dict, seed: int) -> dict[str, Any]:
    world = gen_corridor_length(params, seed)
    finish = world["finish"]
    world["items"] = [list(finish)]
    world["finish"] = None
    return world


def gen_finish_along_row(params: dict, seed: int) -> dict[str, Any]:
    return gen_corridor_length(params, seed)


def gen_paint_gaps(params: dict, seed: int) -> dict[str, Any]:
    world = gen_paint_corridor(params, seed)
    cells = [list(p) for p in world["paint_targets"]]
    idx = _variant(seed, 4)
    if idx == 0:
        already = cells[1:-1]
    elif idx == 1:
        already = cells[::2]
    elif idx == 2:
        already = []
    else:
        already = cells[:-1]
    if already == cells and cells:
        already = cells[:-1]
    world["painted"] = already
    return world


def gen_stairs_width(params: dict, seed: int) -> dict[str, Any]:
    """Лесенка вправо-вниз: число ступенек 3 или 4 — нужен цикл, фиксированный путь ломается."""
    steps = 3 if _variant(seed, 2) == 0 else 4
    start = (0, 0)
    origin = (1, 0)
    walls = []
    paint_targets = []
    x, y = origin
    for i in range(steps):
        paint_targets.append([x, y])
        paint_targets.append([x + 1, y])
        if i < steps - 1:
            walls.append([x + 2, y])
        x += 1
        y += 1
    finish = (origin[0] + steps, origin[1] + steps - 1)
    return world_dict(
        origin[0] + steps + 1,
        origin[1] + steps,
        start,
        finish=finish,
        walls=walls,
        paint_targets=paint_targets,
    )


def gen_vertical_corridor(params: dict, seed: int) -> dict[str, Any]:
    length = _corridor_length(params, seed)
    return world_dict(1, length, (0, 0), finish=(0, length - 1))


GENERATORS: dict[str, GeneratorFn] = {
    "optional_wall_ahead": gen_detour,
    "detour": gen_detour,
    "finish_side": gen_finish_side,
    "item_one_of_two": gen_item_one_of_two,
    "item_maybe": gen_item_maybe,
    "box_or_around": gen_box_or_around,
    "item_and_wall": gen_item_and_wall,
    "paint_signal": gen_paint_signal,
    "open_vertical": gen_open_vertical,
    "alcove_gem": gen_alcove_gem,
    "corridor_length": gen_corridor_length,
    "paint_corridor": gen_paint_corridor,
    "item_at_end": gen_item_at_end,
    "finish_along_row": gen_finish_along_row,
    "paint_gaps": gen_paint_gaps,
    "stairs_width": gen_stairs_width,
    "vertical_corridor": gen_vertical_corridor,
}


def generate_world(spec: dict, seed: int) -> dict[str, Any]:
    gen_id = spec.get("id")
    fn = GENERATORS.get(gen_id or "")
    if not fn:
        raise KeyError(f"unknown generator: {gen_id}")
    return fn(spec.get("params") or {}, seed)


def generate_worlds(spec: dict) -> list[dict[str, Any]]:
    count = max(2, int(spec.get("count") or 2))
    return [generate_world(spec, seed) for seed in range(1, count + 1)]

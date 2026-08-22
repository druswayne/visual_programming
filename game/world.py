"""Клетчатый мир робота: ходы, закраска, предметы, коробки."""

from __future__ import annotations

from typing import Any, Iterable

DIRS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

MAX_STEPS = 400
MAX_SIZE = 20


class RobotError(Exception):
    """Ошибка действия робота (удар о стену, неверный pick/put)."""

    def __init__(self, code: str, **params: Any):
        self.code = code
        self.params = params
        super().__init__(code)


def _pairs(values: Iterable | None) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    if not values:
        return result
    for item in values:
        if item is None:
            continue
        result.add((int(item[0]), int(item[1])))
    return result


def _list_points(points: set[tuple[int, int]]) -> list[list[int]]:
    return [[x, y] for x, y in sorted(points)]


def border_cells(width: int, height: int) -> list[tuple[int, int]]:
    cells: list[tuple[int, int]] = []
    for x in range(width):
        cells.append((x, 0))
        cells.append((x, height - 1))
    for y in range(1, height - 1):
        cells.append((0, y))
        cells.append((width - 1, y))
    return cells


def _as_point_list(values: Iterable | None) -> list[list[int]]:
    result: list[list[int]] = []
    seen: set[tuple[int, int]] = set()
    for item in values or []:
        point = (int(item[0]), int(item[1]))
        if point in seen:
            continue
        seen.add(point)
        result.append([point[0], point[1]])
    return result


def world_dict(
    width: int,
    height: int,
    start: tuple[int, int] | list[int],
    finish: tuple[int, int] | list[int] | None = None,
    walls: Iterable | None = None,
    paint_targets: Iterable | None = None,
    painted: Iterable | None = None,
    items: Iterable | None = None,
    item_targets: Iterable | None = None,
    boxes: Iterable | None = None,
    box_targets: Iterable | None = None,
    facing: str = "right",
    carrying: bool = False,
    frame: bool = False,
) -> dict[str, Any]:
    """Собрать словарь мира для раннера и клиента."""
    wall_cells: list = list(walls or [])
    if frame:
        wall_cells = list(border_cells(width, height)) + wall_cells
    data: dict[str, Any] = {
        "width": int(width),
        "height": int(height),
        "start": [int(start[0]), int(start[1])],
        "facing": facing,
        "carrying": bool(carrying),
        "walls": _as_point_list(wall_cells),
        "paint_targets": _as_point_list(paint_targets),
        "painted": _as_point_list(painted),
        "items": _as_point_list(items),
        "item_targets": _as_point_list(item_targets),
        "boxes": _as_point_list(boxes),
        "box_targets": _as_point_list(box_targets),
        "finish": [int(finish[0]), int(finish[1])] if finish is not None else None,
    }
    return data


class World:
    def __init__(self, data: dict[str, Any]):
        width = int(data.get("width") or 0)
        height = int(data.get("height") or 0)
        if width < 1 or height < 1 or width > MAX_SIZE or height > MAX_SIZE:
            raise ValueError("invalid world size")
        self.width = width
        self.height = height
        start = data.get("start") or [0, 0]
        self.robot_x = int(start[0])
        self.robot_y = int(start[1])
        facing = data.get("facing") or "right"
        self.facing = facing if facing in DIRS else "right"
        self.carrying = bool(data.get("carrying"))
        self.walls = _pairs(data.get("walls"))
        self.painted = _pairs(data.get("painted"))
        self.paint_targets = _pairs(data.get("paint_targets"))
        self.items = _pairs(data.get("items"))
        self.item_targets = _pairs(data.get("item_targets"))
        self.boxes = _pairs(data.get("boxes"))
        self.box_targets = _pairs(data.get("box_targets"))
        finish = data.get("finish")
        self.finish = (int(finish[0]), int(finish[1])) if finish else None
        self.steps: list[dict[str, Any]] = []
        self._action_count = 0
        if not self.in_bounds(self.robot_x, self.robot_y) or self.is_wall(
            self.robot_x, self.robot_y
        ):
            raise ValueError("invalid robot start")
        self._record(
            {
                "t": "start",
                "x": self.robot_x,
                "y": self.robot_y,
                "facing": self.facing,
                "carrying": self.carrying,
            }
        )

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, x: int, y: int) -> bool:
        return not self.in_bounds(x, y) or (x, y) in self.walls

    def to_dict(self) -> dict[str, Any]:
        return world_dict(
            self.width,
            self.height,
            (self.robot_x, self.robot_y),
            finish=self.finish,
            walls=self.walls,
            paint_targets=self.paint_targets,
            painted=self.painted,
            items=self.items,
            item_targets=self.item_targets,
            boxes=self.boxes,
            box_targets=self.box_targets,
            facing=self.facing,
            carrying=self.carrying,
            frame=False,
        )

    def to_public_dict(self) -> dict[str, Any]:
        data = self.to_dict()
        data["start"] = [self.robot_x, self.robot_y]
        return data

    def snapshot(self) -> dict[str, Any]:
        return {
            "x": self.robot_x,
            "y": self.robot_y,
            "facing": self.facing,
            "carrying": self.carrying,
            "painted": _list_points(self.painted),
            "items": _list_points(self.items),
            "boxes": _list_points(self.boxes),
        }

    def _bump(self, direction: str, code: str) -> None:
        self.steps.append(
            {
                "t": "bump",
                "dir": direction,
                "x": self.robot_x,
                "y": self.robot_y,
                "facing": direction,
                "carrying": self.carrying,
            }
        )
        raise RobotError(code, dir=direction)

    def _count_action(self) -> None:
        self._action_count += 1
        if self._action_count > MAX_STEPS:
            raise RobotError("too_many_steps")

    def _record(self, step: dict[str, Any]) -> None:
        self.steps.append(step)

    def move(self, direction: str) -> None:
        if direction not in DIRS:
            raise RobotError("bump_wall", dir=direction)
        self._count_action()
        dx, dy = DIRS[direction]
        self.facing = direction
        nx, ny = self.robot_x + dx, self.robot_y + dy
        if self.is_wall(nx, ny):
            self._bump(direction, "bump_wall")
        if (nx, ny) in self.boxes:
            bx, by = nx + dx, ny + dy
            if self.is_wall(bx, by) or (bx, by) in self.boxes or (bx, by) in self.items:
                self._bump(direction, "bump_box")
            self.boxes.remove((nx, ny))
            self.boxes.add((bx, by))
            self.robot_x, self.robot_y = nx, ny
            self._record(
                {
                    "t": "push",
                    "dir": direction,
                    "from": [nx, ny],
                    "to": [bx, by],
                    "x": nx,
                    "y": ny,
                    "facing": direction,
                    "carrying": self.carrying,
                }
            )
            return
        self.robot_x, self.robot_y = nx, ny
        self._record(
            {
                "t": "move",
                "dir": direction,
                "x": nx,
                "y": ny,
                "facing": direction,
                "carrying": self.carrying,
            }
        )

    def paint(self) -> None:
        self._count_action()
        self.painted.add((self.robot_x, self.robot_y))
        self._record({"t": "paint", "x": self.robot_x, "y": self.robot_y})

    def pick(self) -> None:
        self._count_action()
        pos = (self.robot_x, self.robot_y)
        if self.carrying:
            self._record({"t": "fail", "action": "pick", "x": self.robot_x, "y": self.robot_y})
            raise RobotError("pick_carrying")
        if pos not in self.items:
            self._record({"t": "fail", "action": "pick", "x": self.robot_x, "y": self.robot_y})
            raise RobotError("pick_empty")
        self.items.remove(pos)
        self.carrying = True
        self._record(
            {
                "t": "pick",
                "x": self.robot_x,
                "y": self.robot_y,
                "carrying": True,
            }
        )

    def put(self) -> None:
        self._count_action()
        pos = (self.robot_x, self.robot_y)
        if not self.carrying:
            self._record({"t": "fail", "action": "put", "x": self.robot_x, "y": self.robot_y})
            raise RobotError("put_empty")
        if pos in self.items or pos in self.boxes:
            self._record({"t": "fail", "action": "put", "x": self.robot_x, "y": self.robot_y})
            raise RobotError("put_occupied")
        self.items.add(pos)
        self.carrying = False
        self._record(
            {
                "t": "put",
                "x": self.robot_x,
                "y": self.robot_y,
                "carrying": False,
            }
        )

    def wall_dir(self, direction: str) -> bool:
        dx, dy = DIRS[direction]
        return self.is_wall(self.robot_x + dx, self.robot_y + dy)

    def box_dir(self, direction: str) -> bool:
        dx, dy = DIRS[direction]
        return (self.robot_x + dx, self.robot_y + dy) in self.boxes

    def painted_here(self) -> bool:
        return (self.robot_x, self.robot_y) in self.painted

    def has_item(self) -> bool:
        return (self.robot_x, self.robot_y) in self.items

    def on_finish(self) -> bool:
        return self.finish is not None and (self.robot_x, self.robot_y) == self.finish


class Robot:
    """API ученика: robot.up(), robot.paint(), датчики."""

    def __init__(self, world: World):
        self._world = world

    def up(self) -> None:
        self._world.move("up")

    def down(self) -> None:
        self._world.move("down")

    def left(self) -> None:
        self._world.move("left")

    def right(self) -> None:
        self._world.move("right")

    def paint(self) -> None:
        self._world.paint()

    def pick(self) -> None:
        self._world.pick()

    def put(self) -> None:
        self._world.put()

    def wall_up(self) -> bool:
        return self._world.wall_dir("up")

    def wall_down(self) -> bool:
        return self._world.wall_dir("down")

    def wall_left(self) -> bool:
        return self._world.wall_dir("left")

    def wall_right(self) -> bool:
        return self._world.wall_dir("right")

    def box_up(self) -> bool:
        return self._world.box_dir("up")

    def box_down(self) -> bool:
        return self._world.box_dir("down")

    def box_left(self) -> bool:
        return self._world.box_dir("left")

    def box_right(self) -> bool:
        return self._world.box_dir("right")

    def painted(self) -> bool:
        return self._world.painted_here()

    def has_item(self) -> bool:
        return self._world.has_item()

    def carrying(self) -> bool:
        return self._world.carrying

    def finish(self) -> bool:
        return self._world.on_finish()


def check_goal(world: World, goal: dict | list | None) -> bool:
    if not goal:
        return world.on_finish() if world.finish else True
    if isinstance(goal, list):
        return all(check_goal(world, part) for part in goal)
    gtype = goal.get("type")
    if gtype == "combo":
        return all(check_goal(world, part) for part in goal.get("parts") or [])
    if gtype == "reach":
        cell = goal.get("cell")
        if cell:
            return (world.robot_x, world.robot_y) == (int(cell[0]), int(cell[1]))
        return world.on_finish()
    if gtype == "paint":
        return world.paint_targets == world.painted
    if gtype == "collect":
        return not world.items
    if gtype == "place":
        return (not world.carrying) and world.item_targets <= world.items
    if gtype == "boxes":
        return world.box_targets <= world.boxes
    return False

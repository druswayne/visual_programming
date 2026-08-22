"""Тесты мира робота, генераторов, раннера и миссий."""

from app import create_app
from game.checker import check_mission
from game.generators import generate_world, generate_worlds
from game.world import Robot, RobotError, World, check_goal, world_dict
from runner.python_to_blocks import python_to_blocks


def test_move_and_bump():
    world = World(world_dict(5, 3, (1, 1), walls=[[3, 1]]))
    robot = Robot(world)
    robot.right()
    assert (world.robot_x, world.robot_y) == (2, 1)
    try:
        robot.right()
        assert False, "expected bump"
    except RobotError as exc:
        assert exc.code == "bump_wall"
    assert (world.robot_x, world.robot_y) == (2, 1)


def test_paint_goal():
    world = World(world_dict(4, 3, (1, 1), paint_targets=[[1, 1], [2, 1]]))
    robot = Robot(world)
    robot.paint()
    robot.right()
    robot.paint()
    assert check_goal(world, {"type": "paint"})


def test_pick_put_and_place_goal():
    world = World(world_dict(5, 3, (1, 1), items=[[1, 1]], item_targets=[[3, 1]]))
    robot = Robot(world)
    robot.pick()
    assert world.carrying
    robot.right()
    robot.right()
    robot.put()
    assert check_goal(world, {"type": "place"})


def test_push_box_onto_target():
    world = World(world_dict(6, 3, (1, 1), boxes=[[2, 1]], box_targets=[[3, 1]]))
    robot = Robot(world)
    robot.right()
    assert (3, 1) in world.boxes
    assert check_goal(world, {"type": "boxes"})


def test_cannot_push_box_into_wall():
    world = World(world_dict(5, 3, (1, 1), boxes=[[2, 1]], walls=[[3, 1]]))
    robot = Robot(world)
    try:
        robot.right()
        assert False, "expected bump_box"
    except RobotError as exc:
        assert exc.code == "bump_box"


def test_sensors():
    world = World(world_dict(5, 3, (2, 1), walls=[[3, 1]], items=[[2, 1]], finish=(2, 1)))
    robot = Robot(world)
    assert robot.wall_right() is True
    assert robot.wall_left() is False
    assert robot.has_item() is True
    assert robot.finish() is True
    assert robot.painted() is False


def test_map_edge_is_invisible_wall():
    world = World(world_dict(3, 1, (0, 0)))
    robot = Robot(world)
    assert robot.wall_left() is True
    assert robot.wall_up() is True
    assert robot.wall_down() is True
    assert robot.wall_right() is False
    robot.right()
    robot.right()
    assert (world.robot_x, world.robot_y) == (2, 0)
    assert robot.wall_right() is True
    try:
        robot.right()
        assert False, "expected bump at map edge"
    except RobotError as exc:
        assert exc.code == "bump_wall"


def test_generator_is_deterministic():
    spec = {"id": "optional_wall_ahead", "count": 4}
    first = generate_worlds(spec)
    second = generate_worlds(spec)
    assert first == second
    walls = {tuple(tuple(p) for p in world["walls"]) for world in first}
    assert len(walls) >= 2


def test_corridor_length_varies():
    spec = {"id": "corridor_length", "params": {"min": 3, "max": 6}}
    widths = {generate_world(spec, seed)["width"] for seed in range(1, 8)}
    assert len(widths) > 1


def _run_ctx(fn):
    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    with app.app_context():
        with app.test_request_context():
            return fn()


def test_runtime_reach_finish():
    def inner():
        from game.runtime import run_robot_program

        world = world_dict(8, 5, (1, 2), finish=(4, 2))
        code = "robot.right()\nrobot.right()\nrobot.right()\n"
        result = run_robot_program(code, world, {"type": "reach"})
        assert result["success"] is True
        assert result["goal_met"] is True
        kinds = [step["t"] for step in result["steps"]]
        assert kinds.count("move") == 3

    _run_ctx(inner)


def test_runtime_bump_is_error():
    def inner():
        from game.runtime import run_robot_program

        world = world_dict(4, 3, (1, 1), walls=[[2, 1]])
        result = run_robot_program("robot.right()\n", world, {"type": "reach"})
        assert result["success"] is False
        assert result["error_code"] == "bump_wall"
        assert result["steps"]

    _run_ctx(inner)


def test_check_walk_3_mission():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission = get_mission("walk_3")
        worlds = resolve_worlds(mission)
        ok = check_mission(
            "robot.right()\nrobot.right()\nrobot.right()\n",
            worlds,
            mission["goal"],
        )
        assert ok["success"] is True
        bad = check_mission("robot.left()\n", worlds, mission["goal"])
        assert bad["success"] is False

    _run_ctx(inner)


def test_check_conditions_all_variants():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission = get_mission("finish_side")
        worlds = resolve_worlds(mission)
        assert len(worlds) >= 2
        code = (
            "if robot.wall_left():\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "else:\n"
            "    robot.left()\n"
            "    robot.left()\n"
        )
        result = check_mission(code, worlds, mission["goal"])
        assert result["success"] is True

    _run_ctx(inner)


def test_python_to_blocks_robot():
    result = python_to_blocks("robot.up()\nrobot.paint()\nif robot.wall_right():\n    robot.left()\n")
    chain = result["program"]["chain"]
    assert chain[0]["type"] == "py_robot_up"
    assert chain[1]["type"] == "py_robot_paint"
    assert chain[2]["type"] in ("py_if", "py_ifelse")


def test_game_tracks_api_requires_auth():
    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    client = app.test_client()
    assert client.get("/api/game/tracks").status_code == 401
    assert client.get("/api/game/missions/walk_3").status_code == 401
    run = client.post("/api/game/run", json={"code": "robot.right()", "mission_id": "walk_3"})
    assert run.status_code == 401


def test_game_tracks_api():
    from extensions import db
    from models import User

    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    with app.app_context():
        db.create_all()
        user = User.query.filter_by(username="__game_api__").first()
        if not user:
            user = User(username="__game_api__", email="game_api@test.local")
            user.set_password("test-password")
            db.session.add(user)
            db.session.commit()
        user_id = user.id

        client = app.test_client()
        with client.session_transaction() as sess:
            sess["_user_id"] = str(user_id)
            sess["_fresh"] = True

        resp = client.get("/api/game/tracks")
        assert resp.status_code == 200
        data = resp.get_json()
        ids = [track["id"] for track in data["tracks"]]
        assert ids == ["linear", "conditions", "loops"]
        detail = client.get("/api/game/missions/walk_3")
        assert detail.status_code == 200
        body = detail.get_json()
        assert body["world"]["width"] == 9
        assert body["mission"]["id"] == "walk_3"


def test_detour_rejects_straight_line():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission = get_mission("detour")
        worlds = resolve_worlds(mission)
        assert len(worlds) >= 2
        walls_ahead = []
        for world in worlds:
            robot_x, robot_y = world["start"]
            wall_set = {tuple(p) for p in world["walls"]}
            walls_ahead.append((robot_x + 1, robot_y) in wall_set)
        assert True in walls_ahead and False in walls_ahead
        result = check_mission(
            "robot.right()\nrobot.right()\nrobot.right()\nrobot.right()\n",
            worlds,
            mission["goal"],
        )
        assert result["success"] is False
        ok = check_mission(
            "if robot.wall_right():\n"
            "    robot.up()\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "    robot.down()\n"
            "else:\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "    robot.right()\n"
            "    robot.right()\n",
            worlds,
            mission["goal"],
        )
        assert ok["success"] is True

    _run_ctx(inner)


def test_walk_until_wall_rejects_fixed_steps():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission = get_mission("walk_until_wall")
        worlds = resolve_worlds(mission)
        assert len(worlds) >= 2
        lengths = {world["finish"][0] - world["start"][0] for world in worlds}
        assert len(lengths) > 1
        result = check_mission(
            "robot.right()\nrobot.right()\nrobot.right()\nrobot.right()\n",
            worlds,
            mission["goal"],
        )
        assert result["success"] is False
        ok = check_mission(
            "while not robot.wall_right():\n    robot.right()\n",
            worlds,
            mission["goal"],
        )
        assert ok["success"] is True

    _run_ctx(inner)


def test_paint_stairs_needs_variable_length():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission = get_mission("paint_stairs")
        worlds = resolve_worlds(mission)
        assert len(worlds) >= 2
        fixed = check_mission(
            "robot.paint()\nrobot.right()\nrobot.paint()\nrobot.down()\n"
            "robot.paint()\nrobot.right()\nrobot.paint()\nrobot.down()\n"
            "robot.paint()\nrobot.right()\nrobot.paint()\n",
            worlds,
            mission["goal"],
        )
        assert fixed["success"] is False
        ok = check_mission(
            "robot.right()\n"
            "while not robot.finish():\n"
            "    robot.paint()\n"
            "    robot.right()\n"
            "    robot.paint()\n"
            "    if not robot.finish():\n"
            "        robot.down()\n",
            worlds,
            mission["goal"],
        )
        assert ok["success"] is True

    _run_ctx(inner)


def test_action_cells_are_not_on_spawn():
    def inner():
        from data.game.registry import get_mission, resolve_worlds

        mission_ids = (
            "paint_here",
            "paint_l",
            "pick_item",
            "deliver_item",
            "paint_and_pick",
            "pick_if_present",
            "nested_item_wall",
            "paint_row_for",
            "paint_column_for",
            "paint_until_wall",
            "paint_two_rows",
            "paint_gaps_while",
            "paint_stairs",
        )
        keys = ("paint_targets", "items", "item_targets", "boxes")
        for mission_id in mission_ids:
            mission = get_mission(mission_id)
            for world in resolve_worlds(mission):
                start = tuple(world["start"])
                for key in keys:
                    occupied = {tuple(p) for p in world.get(key) or []}
                    assert start not in occupied, f"{mission_id} {key} {start}"

    _run_ctx(inner)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(name, "ok")
    print("all ok")

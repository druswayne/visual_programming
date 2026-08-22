"""English overlays for game tracks and missions."""

TRACKS_EN = {
    "linear": {
        "title": "Sequence",
        "description": "Build a chain of commands: moves, painting, items, and boxes.",
    },
    "conditions": {
        "title": "Conditions",
        "description": "The map changes every time — you need if and robot sensors.",
    },
    "loops": {
        "title": "Loops",
        "description": "Repeat actions with for and while until the goal is met.",
    },
}

MISSIONS_EN = {
    "walk_3": {
        "title": "Three steps right",
        "condition": "Take the robot to the glowing finish cell. It is three cells to the right, inside the room.",
        "hint": "Use the “right” block three times.",
    },
    "maze_l": {
        "title": "L-shaped corridor",
        "condition": "The straight path is closed. Walk right to the end of the corridor, then down to the finish.",
        "hint": "Two steps right, then three steps down.",
    },
    "around_wall": {
        "title": "Around the pillar",
        "condition": "A pillar stands in the middle of the room. Go around it above and reach the finish on the right.",
        "hint": "Right, up, right, right, down, right.",
    },
    "paint_here": {
        "title": "Paint the cell",
        "condition": "To the right is a cell with a gold frame — that is the target. Walk onto it and paint it.",
        "hint": "Step right, then “paint”.",
    },
    "paint_l": {
        "title": "Paint an L",
        "condition": "An L of five cells sits to the right. Walk onto it and paint: three cells right, then two more down.",
        "hint": "Right → paint → right → paint → right → paint → down → paint → down → paint.",
    },
    "pick_item": {
        "title": "Crystal on the way",
        "condition": "A crystal lies to the right. Walk to it, pick it up, and take the robot to the finish.",
        "hint": "Two steps right, “pick”, then one more step right to the finish.",
    },
    "deliver_item": {
        "title": "Delivery",
        "condition": "A crystal lies to the right. Pick it up and put it on the cell with the blue mark.",
        "hint": "Two steps right → pick → one step right → put.",
    },
    "push_box": {
        "title": "Push the crate",
        "condition": "A crate stands to the right. Step into it — the robot pushes the crate if the next cell is free. The crate must end on the marked cell.",
        "hint": "One step right.",
    },
    "box_to_target": {
        "title": "Crate to the warehouse",
        "condition": "Push the crate right until it sits on the warehouse cell.",
        "hint": "Each step into a crate moves it one cell. You need two pushes.",
    },
    "paint_and_pick": {
        "title": "Mark and crystal",
        "condition": "A paint target is to the right, then a crystal. Paint the cell, pick up the crystal, and reach the finish.",
        "hint": "Right → paint → right → pick → one more step right to the finish.",
    },
    "detour": {
        "title": "Around or straight",
        "condition": "On some maps a wall blocks the way ahead — go around above. On others the top is a dead end and the way ahead is clear. The same program must pass both types.",
        "hint": "If there is a wall on the right: up, four steps right, down. Otherwise four steps right.",
    },
    "finish_side": {
        "title": "Finish left or right",
        "condition": "The finish is sometimes on the left, sometimes on the right. The closed side is blocked by a wall — go the open way.",
        "hint": "If there is a wall on the left, take two steps right; otherwise two steps left.",
    },
    "open_vertical": {
        "title": "Up or down",
        "condition": "The finish is either at the top of the room or at the bottom. The opposite path is blocked by a wall.",
        "hint": "If there is a wall above, take two steps down; otherwise two steps up.",
    },
    "paint_marked": {
        "title": "Only the crystal cell",
        "condition": "Two cells sit in a row. The crystal is only on one of them — paint that cell and leave the other blank.",
        "hint": "Walk to a cell: if there is an item, paint it. Then check the second cell.",
    },
    "pick_if_present": {
        "title": "Pick if present",
        "condition": "Sometimes a crystal lies one cell to the right. Step there: pick it up if it is there. Always reach the finish.",
        "hint": "Step right. if “item here”: pick. Then three more steps right.",
    },
    "box_or_around": {
        "title": "Crate or a dead end above",
        "condition": "Either a crate stands to the right and cannot be pushed (a wall is behind it) — go around above. Or there is no crate, but the top is blocked — walk straight. Both types are checked.",
        "hint": "If there is a box on the right, go around above. Otherwise four steps right.",
    },
    "paint_signal": {
        "title": "Paint the blank cell",
        "condition": "Two cells to the right. One is already painted — that is a hint. Paint only the cell that is still blank.",
        "hint": "Step right. If the cell is painted, take two more steps and paint. Otherwise paint immediately.",
    },
    "nested_item_wall": {
        "title": "Crystal and a fork",
        "condition": "Four map types: the crystal may or may not be there, and the way ahead may be blocked. Pick up the crystal if it is there and reach the finish, choosing a detour or the straight path.",
        "hint": "Step right. If there is an item, pick it up. Then an if with a wall on the right (same as “Around or straight”).",
    },
    "alcove_gem": {
        "title": "Alcove with a crystal",
        "condition": "The crystal is hidden in the upper alcove or the lower one. The opposite alcove is closed. Pick up the crystal and reach the finish on the right.",
        "hint": "Two steps right to the column. If there is a wall below: up, pick, down. Otherwise: down, pick, up. Then two steps right to the finish.",
    },
    "paint_row_for": {
        "title": "Paint a row",
        "condition": "Five cells to the right must be painted. The length is known — a for loop fits.",
        "hint": "for i in range(5): step right, paint.",
    },
    "paint_column_for": {
        "title": "Paint a column",
        "condition": "Four cells below the robot must be painted. Walk onto each and paint it.",
        "hint": "A for loop of 4: step down, paint.",
    },
    "walk_until_wall": {
        "title": "Walk until a wall",
        "condition": "The corridor is sometimes short, sometimes long — every length is checked. Walk right while there is no wall on the right. Stop at the wall: that is the finish.",
        "hint": "while not robot.wall_right(): right.",
    },
    "paint_until_wall": {
        "title": "Paint until a wall",
        "condition": "Paint the whole corridor. The length is different on each map, so you cannot count the steps in advance.",
        "hint": "While there is no wall on the right: step right and paint.",
    },
    "while_to_finish": {
        "title": "Until the finish",
        "condition": "The finish is at the end of a corridor of random length. Walk right until the robot is on the finish.",
        "hint": "Use the “finish” sensor in the while condition.",
    },
    "pick_at_end": {
        "title": "Crystal at the end",
        "condition": "The crystal lies at the end of a corridor of unknown length. Reach it and pick it up.",
        "hint": "While there is no item on the cell, step right. Then pick.",
    },
    "paint_two_rows": {
        "title": "Two rows",
        "condition": "Two rows of four cells sit to the right. First the top row going right, then step down and paint the bottom row going left.",
        "hint": "A for loop of 4: right and paint. Then down and a loop: paint and left.",
    },
    "paint_gaps_while": {
        "title": "Finish painting the corridor",
        "condition": "The corridor length changes, and some cells are already painted. Paint the rest — and only those.",
        "hint": "While there is no wall on the right: step right; if the cell is not painted, paint it.",
    },
    "walk_down_until_wall": {
        "title": "Down until a wall",
        "condition": "The corridor goes down, and the height is different every time. Walk down while there is no wall below — that is the finish.",
        "hint": "while not wall below: down. Same idea as “walk until a wall”, only vertical.",
    },
    "paint_stairs": {
        "title": "Stairs",
        "condition": "Paint the steps going right and down, then reach the finish. Some maps have three steps, others four — you cannot count them in advance.",
        "hint": "First step right onto the stairs. While not on the finish: paint, right, paint. If still not on the finish, step down.",
    },
}

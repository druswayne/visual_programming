/**
 * Панели блоков для игрового режима (по линейкам миссий).
 */
function gameRobotActionBlocks() {
  return [
    { kind: "block", type: "py_robot_up" },
    { kind: "block", type: "py_robot_down" },
    { kind: "block", type: "py_robot_left" },
    { kind: "block", type: "py_robot_right" },
    { kind: "block", type: "py_robot_paint" },
    { kind: "block", type: "py_robot_pick" },
    { kind: "block", type: "py_robot_put" },
  ];
}

function gameRobotSensorBlocks() {
  return [
    { kind: "block", type: "py_robot_wall_up" },
    { kind: "block", type: "py_robot_wall_down" },
    { kind: "block", type: "py_robot_wall_left" },
    { kind: "block", type: "py_robot_wall_right" },
    { kind: "block", type: "py_robot_box_up" },
    { kind: "block", type: "py_robot_box_down" },
    { kind: "block", type: "py_robot_box_left" },
    { kind: "block", type: "py_robot_box_right" },
    { kind: "block", type: "py_robot_painted" },
    { kind: "block", type: "py_robot_has_item" },
    { kind: "block", type: "py_robot_carrying" },
    { kind: "block", type: "py_robot_finish" },
  ];
}

function gameLoopBlocks() {
  return [
    { kind: "block", type: "py_for" },
    { kind: "block", type: "py_while", inputs: { COND: SH.b(true) } },
    { kind: "block", type: "py_break" },
    { kind: "block", type: "py_continue" },
  ];
}

function gameConditionBlocks() {
  return [
    { kind: "block", type: "py_if" },
    { kind: "block", type: "py_ifelse", inputs: { IF0: SH.b(true) } },
    {
      kind: "block",
      type: "py_if",
      extraState: { elseIfCount: 1, hasElse: true },
    },
  ];
}

function gameLogicBlocks() {
  return [
    { kind: "block", type: "logic_compare" },
    { kind: "block", type: "logic_operation" },
    { kind: "block", type: "logic_negate" },
    { kind: "block", type: "logic_boolean" },
  ];
}

function buildGameToolbox(kind) {
  const contents = [
    toolboxCat("robot", "Робот", "200", gameRobotActionBlocks()),
  ];

  if (kind === "conditions" || kind === "loops") {
    contents.push(toolboxCat("robot_sensors", "Датчики", "180", gameRobotSensorBlocks()));
    contents.push(toolboxCat("logic", "Логика", "210", gameLogicBlocks()));
    contents.push(toolboxCat("conditions", "Условия", "210", gameConditionBlocks()));
  }

  if (kind === "loops") {
    contents.push(toolboxCat("loops", "Циклы", "120", gameLoopBlocks()));
  } else {
    contents.push(
      toolboxCat("loops", "Циклы", "120", [
        { kind: "block", type: "py_for" },
      ])
    );
  }

  contents.push(
    toolboxCat("math", "Математика", "230", [
      { kind: "block", type: "math_number" },
      { kind: "block", type: "py_range", inputs: { FROM: SH.n(0), TO: SH.n(5), BY: SH.n(1) } },
    ])
  );
  contents.push(toolboxCat("variables", "Переменные", "330", "VARIABLE"));
  return { kind: "categoryToolbox", contents: contents };
}

const GAME_TOOLBOX_LINEAR = buildGameToolbox("linear");
const GAME_TOOLBOX_CONDITIONS = buildGameToolbox("conditions");
const GAME_TOOLBOX_LOOPS = buildGameToolbox("loops");

function getGameToolbox(kind) {
  if (kind === "conditions") return GAME_TOOLBOX_CONDITIONS;
  if (kind === "loops") return GAME_TOOLBOX_LOOPS;
  return GAME_TOOLBOX_LINEAR;
}

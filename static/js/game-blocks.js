/**
 * Блоки робота для игрового режима.
 */
function getGameRobotBlocks() {
  const actions = [
    ["up", "robot.up", "▲  вверх"],
    ["down", "robot.down", "▼  вниз"],
    ["left", "robot.left", "◀  влево"],
    ["right", "robot.right", "▶  вправо"],
    ["paint", "robot.paint", "закрасить"],
    ["pick", "robot.pick", "взять предмет"],
    ["put", "robot.put", "положить предмет"],
  ];
  const sensors = [
    ["wall_up", "robot.wall_up", "стена сверху?"],
    ["wall_down", "robot.wall_down", "стена снизу?"],
    ["wall_left", "robot.wall_left", "стена слева?"],
    ["wall_right", "robot.wall_right", "стена справа?"],
    ["box_up", "robot.box_up", "коробка сверху?"],
    ["box_down", "robot.box_down", "коробка снизу?"],
    ["box_left", "robot.box_left", "коробка слева?"],
    ["box_right", "robot.box_right", "коробка справа?"],
    ["painted", "robot.painted", "клетка закрашена?"],
    ["has_item", "robot.has_item", "здесь предмет?"],
    ["carrying", "robot.carrying", "несу предмет?"],
    ["finish", "robot.finish", "финиш?"],
  ];

  const blocks = actions.map(function (item) {
    return {
      type: "py_robot_" + item[0],
      message0: pbMsg(item[1], item[2]),
      previousStatement: null,
      nextStatement: null,
      style: "robot_blocks",
      tooltip: pbMsg("tooltip." + item[1], item[2]),
    };
  });

  sensors.forEach(function (item) {
    blocks.push({
      type: "py_robot_" + item[0],
      message0: pbMsg(item[1], item[2]),
      output: "Boolean",
      style: "robot_sensor_blocks",
      tooltip: pbMsg("tooltip." + item[1], item[2]),
    });
  });

  return blocks;
}

function registerGameBlocks() {
  if (typeof Blockly === "undefined") return;
  const defs = getGameRobotBlocks().filter(function (json) {
    return typeof isBlockTypeRegistered !== "function" || !isBlockTypeRegistered(json.type);
  });
  if (!defs.length) return;
  if (Blockly.common && Blockly.common.defineBlocks) {
    Blockly.common.defineBlocks(Blockly.common.createBlockDefinitionsFromJsonArray(defs));
  } else {
    defs.forEach(function (json) {
      Blockly.Blocks[json.type] = {
        init: function () {
          this.jsonInit(json);
        },
      };
    });
  }
}

function registerGameGenerators() {
  const gen = typeof getPythonGenerator === "function" ? getPythonGenerator() : null;
  if (!gen) return;
  const Order = (typeof python !== "undefined" && python.Order) || gen;
  const actions = ["up", "down", "left", "right", "paint", "pick", "put"];
  const sensors = [
    "wall_up",
    "wall_down",
    "wall_left",
    "wall_right",
    "box_up",
    "box_down",
    "box_left",
    "box_right",
    "painted",
    "has_item",
    "carrying",
    "finish",
  ];
  actions.forEach(function (name) {
    gen.forBlock["py_robot_" + name] = function () {
      return "robot." + name + "()\n";
    };
  });
  sensors.forEach(function (name) {
    gen.forBlock["py_robot_" + name] = function () {
      return ["robot." + name + "()", Order.FUNCTION_CALL];
    };
  });
}

registerGameBlocks();
registerGameGenerators();

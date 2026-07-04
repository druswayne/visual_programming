/**
 * Инженерная тема Blockly для PyBlocks — минимализм, строгие цвета
 * (в духе Unreal Engine Blueprints / Blender Node Editor).
 */
(function initPyblocksTheme() {
  if (typeof Blockly === "undefined") return;
  if (window.pyblocksTheme) return;

  /** Приглушённые цвета категорий: primary / secondary / tertiary */
  const C = {
    loop: ["#8B7340", "#6B5830", "#4A3D22"],
    logic: ["#4A6278", "#3A5065", "#283848"],
    math: ["#4A6B52", "#3A5540", "#283830"],
    text: ["#5A5278", "#4A4265", "#353048"],
    list: ["#6B5278", "#554065", "#3D2E48"],
    variable: ["#4A5A82", "#3A4868", "#283550"],
    procedure: ["#7A5260", "#604048", "#483038"],
    io: ["#4A6878", "#3A5260", "#283840"],
    start: ["#3D6B52", "#2E5540", "#1E3828"],
    end: ["#7A5238", "#604030", "#483020"],
  };

  window.pyblocksTheme = Blockly.Theme.defineTheme("pyblocks", {
    base: Blockly.Themes.Classic,
    fontStyle: {
      family: '"Segoe UI", system-ui, sans-serif',
      weight: "500",
      size: 11,
    },
    blockStyles: {
      program_start_blocks: {
        colourPrimary: C.start[0],
        colourSecondary: C.start[1],
        colourTertiary: C.start[2],
        hat: "cap",
      },
      program_end_blocks: {
        colourPrimary: C.end[0],
        colourSecondary: C.end[1],
        colourTertiary: C.end[2],
      },
      loop_blocks: {
        colourPrimary: C.loop[0],
        colourSecondary: C.loop[1],
        colourTertiary: C.loop[2],
      },
      logic_blocks: {
        colourPrimary: C.logic[0],
        colourSecondary: C.logic[1],
        colourTertiary: C.logic[2],
      },
      math_blocks: {
        colourPrimary: C.math[0],
        colourSecondary: C.math[1],
        colourTertiary: C.math[2],
      },
      text_blocks: {
        colourPrimary: C.text[0],
        colourSecondary: C.text[1],
        colourTertiary: C.text[2],
      },
      list_blocks: {
        colourPrimary: C.list[0],
        colourSecondary: C.list[1],
        colourTertiary: C.list[2],
      },
      variable_blocks: {
        colourPrimary: C.variable[0],
        colourSecondary: C.variable[1],
        colourTertiary: C.variable[2],
      },
      procedure_blocks: {
        colourPrimary: C.procedure[0],
        colourSecondary: C.procedure[1],
        colourTertiary: C.procedure[2],
      },
      colour_blocks: {
        colourPrimary: C.io[0],
        colourSecondary: C.io[1],
        colourTertiary: C.io[2],
      },
    },
    categoryStyles: {
      loop_category: { colour: C.loop[0] },
      logic_category: { colour: C.logic[0] },
      math_category: { colour: C.math[0] },
      text_category: { colour: C.text[0] },
      list_category: { colour: C.list[0] },
      variable_category: { colour: C.variable[0] },
      procedure_category: { colour: C.procedure[0] },
    },
    componentStyles: {
      workspaceBackgroundColour: "#141618",
      toolboxBackgroundColour: "#181a1e",
      toolboxForegroundColour: "#c8cdd4",
      flyoutBackgroundColour: "#1c1f24",
      flyoutForegroundColour: "#c8cdd4",
      flyoutOpacity: 1,
      scrollbarColour: "#4a6278",
      insertionMarkerColour: "#6a8298",
      insertionMarkerOpacity: 0.35,
    },
  });
})();

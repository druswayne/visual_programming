/**
 * Максимально компактный рендерер (на базе Thrasos/Geras — плоский, не Zelos).
 */
(function registerCompactRenderer() {
  if (!Blockly.blockRendering) return;

  const BaseRenderer =
    (Blockly.thrasos && Blockly.thrasos.Renderer) ||
    (Blockly.geras && Blockly.geras.Renderer) ||
    (Blockly.zelos && Blockly.zelos.Renderer);

  const BaseConstantProvider =
    (Blockly.thrasos && Blockly.thrasos.ConstantProvider) ||
    (Blockly.geras && Blockly.geras.ConstantProvider) ||
    (Blockly.zelos && Blockly.zelos.ConstantProvider);

  if (!BaseRenderer || !BaseConstantProvider) return;

  const BLOCK_SCALE = 1.1;
  function scale(value) {
    return Math.max(1, Math.round(value * BLOCK_SCALE));
  }

  class CompactConstantProvider extends BaseConstantProvider {
    constructor() {
      super();
      this.FIELD_TEXT_FONTSIZE = scale(10);
      this.FIELD_BORDER_RECT_X_PADDING = scale(5);
      this.FIELD_BORDER_RECT_Y_PADDING = scale(2);
      this.FIELD_BORDER_RECT_HEIGHT = scale(18);
      this.FIELD_DROPDOWN_BORDER_RECT_HEIGHT = scale(18);
      this.FIELD_BORDER_RECT_RADIUS = scale(3);
      this.FIELD_TEXT_BASELINE = scale(11);
      this.TAB_HEIGHT = scale(6);
      this.NOTCH_WIDTH = scale(8);
      this.NOTCH_HEIGHT = scale(2);
      this.CORNER_RADIUS = scale(2);
      this.MIN_BLOCK_HEIGHT = scale(14);
      this.DUMMY_INPUT_MIN_HEIGHT = scale(14);
      this.DUMMY_INPUT_SHADOW_MIN_HEIGHT = scale(14);
      this.EMPTY_INLINE_INPUT_HEIGHT = scale(14);
      this.EMPTY_INLINE_INPUT_PADDING = scale(5);
      this.EMPTY_STATEMENT_INPUT_HEIGHT = scale(14);
      this.START_HAT_HEIGHT = scale(8);
      this.EXTRA_STATEMENT_ROW_Y_HEIGHT = scale(2);
      this.BETWEEN_STATEMENT_PADDING_Y = scale(2);
      this.MEDIUM_PADDING = scale(2);
      this.LARGE_PADDING = scale(3);
      this.SMALL_PADDING = scale(1);
    }
  }

  class CompactRenderer extends BaseRenderer {
    constructor() {
      super("compact");
    }
    makeConstants_() {
      return new CompactConstantProvider();
    }
  }

  Blockly.blockRendering.register("compact", CompactRenderer);
})();

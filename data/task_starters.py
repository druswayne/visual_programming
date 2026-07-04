"""Стартовые Blockly XML для задач «исправь код». Сгенерировано build_fix_tasks.py."""

STARTER_XML = {
    "cond-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_число">число</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_число">число</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">15</field>
          </block>
        </value>
        <next>
          <block type="py_ifelse">
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">LT</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_число">число</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">10</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">да</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">нет</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_if">
            <mutation elseif="1" else="1"></mutation>
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">GT</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <value name="IF1">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">отрицательное</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="DO1">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">ноль</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">положительное</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_v">v</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_v">v</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_ifelse">
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">LT</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_v">v</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">18</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">взрослый</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">ребёнок</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_возраст">возраст</variable>
    <variable id="v_тепло">тепло</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_возраст">возраст</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">10</field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_тепло">тепло</field>
            <value name="VALUE">
              <block type="logic_boolean">
                <field name="BOOL">TRUE</field>
              </block>
            </value>
            <next>
              <block type="py_ifelse">
                <value name="IF0">
                  <block type="logic_operation">
                    <field name="OP">AND</field>
                    <value name="A">
                      <block type="logic_compare">
                        <field name="OP">GTE</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_возраст">возраст</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="math_number">
                            <field name="NUM">11</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <block type="variables_get">
                        <field name="VAR" id="v_тепло">тепло</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="text">
                        <field name="TEXT">можно гулять</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <statement name="ELSE">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="text">
                        <field name="TEXT">остаёмся дома</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_if">
            <mutation elseif="2" else="1"></mutation>
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="py_mod">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <value name="IF1">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="py_mod">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">5</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <value name="IF2">
              <block type="logic_operation">
                <field name="OP">AND</field>
                <value name="A">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A">
                      <block type="py_mod">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">3</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A">
                      <block type="py_mod">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">5</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">Fizz</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="DO1">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">Buzz</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="DO2">
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">FizzBuzz</field>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_x">x</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_x">x</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_a">a</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_b">b</field>
                <value name="VALUE">
                  <block type="py_convert">
                    <field name="TO">INT</field>
                    <value name="VALUE">
                      <block type="py_input">
                        <field name="PROMPT"></field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_ifelse">
                    <value name="IF0">
                      <block type="logic_compare">
                        <field name="OP">GTE</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_x">x</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">в диапазоне</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="ELSE">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">вне диапазона</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_c">c</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_c">c</field>
                <value name="VALUE">
                  <block type="py_convert">
                    <field name="TO">INT</field>
                    <value name="VALUE">
                      <block type="py_input">
                        <field name="PROMPT"></field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_ifelse">
                    <value name="IF0">
                      <block type="logic_compare">
                        <field name="OP">GT</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="variables_get">
                            <field name="VAR" id="v_b">b</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">первое</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="ELSE">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">второе</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_ifelse">
                <value name="IF0">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A">
                      <block type="py_floordiv">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_b">b</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="text">
                        <field name="TEXT">делится</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <statement name="ELSE">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="text">
                        <field name="TEXT">не делится</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_c">c</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_c">c</field>
                <value name="VALUE">
                  <block type="py_convert">
                    <field name="TO">INT</field>
                    <value name="VALUE">
                      <block type="py_input">
                        <field name="PROMPT"></field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_ifelse">
                    <value name="IF0">
                      <block type="logic_compare">
                        <field name="OP">GT</field>
                        <value name="A">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_b">b</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="variables_get">
                                <field name="VAR" id="v_c">c</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <value name="B">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">возможен</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="ELSE">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">невозможен</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "cond-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_d">d</variable>
    <variable id="v_o1">o1</variable>
    <variable id="v_o2">o2</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_o1">o1</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_o2">o2</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_ifelse">
                <value name="IF0">
                  <block type="logic_compare">
                    <field name="OP">GTE</field>
                    <value name="A">
                      <block type="variables_get">
                        <field name="VAR" id="v_o1">o1</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="variables_get">
                        <field name="VAR" id="v_o2">o2</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <block type="variables_set">
                    <field name="VAR" id="v_d">d</field>
                    <value name="VALUE">
                      <block type="py_sub">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_o1">o1</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_o2">o2</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </statement>
                <statement name="ELSE">
                  <block type="variables_set">
                    <field name="VAR" id="v_d">d</field>
                    <value name="VALUE">
                      <block type="py_sub">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_o2">o2</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_o1">o1</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="py_ifelse">
                    <value name="IF0">
                      <block type="logic_compare">
                        <field name="OP">GTE</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_d">d</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="math_number">
                            <field name="NUM">3</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">скачок</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="ELSE">
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="text">
                            <field name="TEXT">стабильно</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="py_for">
        <field name="VAR" id="v_i">i</field>
        <value name="SEQ">
          <block type="py_range">
            <value name="FROM">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="TO">
              <block type="math_number">
                <field name="NUM">5</field>
              </block>
            </value>
            <value name="BY">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO">
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get">
                <field name="VAR" id="v_i">i</field>
              </block>
            </value>
          </block>
        </statement>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_var">_</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="py_for">
        <field name="VAR" id="v_var">_</field>
        <value name="SEQ">
          <block type="py_range">
            <value name="FROM">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <value name="TO">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
            <value name="BY">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO">
          <block type="text_print">
            <value name="TEXT">
              <block type="text">
                <field name="TEXT">Python</field>
              </block>
            </value>
          </block>
        </statement>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">0</field>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_i">i</field>
            <value name="SEQ">
              <block type="py_range">
                <value name="FROM">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
                <value name="TO">
                  <block type="math_number">
                    <field name="NUM">11</field>
                  </block>
                </value>
                <value name="BY">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="variables_set">
                <field name="VAR" id="v_s">s</field>
                <value name="VALUE">
                  <block type="py_mul">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_s">s</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="variables_get">
                        <field name="VAR" id="v_i">i</field>
                      </block>
                    </value>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="py_for">
        <field name="VAR" id="v_i">i</field>
        <value name="SEQ">
          <block type="py_range">
            <value name="FROM">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="TO">
              <block type="math_number">
                <field name="NUM">6</field>
              </block>
            </value>
            <value name="BY">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO">
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get">
                <field name="VAR" id="v_i">i</field>
              </block>
            </value>
          </block>
        </statement>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_i">i</field>
            <value name="SEQ">
              <block type="py_range">
                <value name="FROM">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
                <value name="TO">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="BY">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_i">i</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_i">i</field>
            <value name="SEQ">
              <block type="py_range">
                <value name="FROM">
                  <block type="math_number">
                    <field name="NUM">2</field>
                  </block>
                </value>
                <value name="TO">
                  <block type="py_add">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="py_mul">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="math_number">
                            <field name="NUM">2</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">1</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="BY">
                  <block type="math_number">
                    <field name="NUM">2</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_i">i</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_k">k</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_k">k</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_for">
                <field name="VAR" id="v_i">i</field>
                <value name="SEQ">
                  <block type="py_range">
                    <value name="FROM">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                    <value name="TO">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">1</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="BY">
                      <block type="variables_get">
                        <field name="VAR" id="v_k">k</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_i">i</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_i">i</variable>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_s">s</field>
                <value name="VALUE">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
                <next>
                  <block type="py_for">
                    <field name="VAR" id="v_i">i</field>
                    <value name="SEQ">
                      <block type="py_range">
                        <value name="FROM">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="TO">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_b">b</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="math_number">
                                <field name="NUM">1</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <value name="BY">
                          <block type="math_number">
                            <field name="NUM">1</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO">
                      <block type="variables_set">
                        <field name="VAR" id="v_s">s</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_s">s</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="variables_get">
                                <field name="VAR" id="v_i">i</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <next>
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="variables_get">
                            <field name="VAR" id="v_s">s</field>
                          </block>
                        </value>
                        <next>
                          <block type="py_end"></block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_c">c</variable>
    <variable id="v_ch">ch</variable>
    <variable id="v_s">s</variable>
    <variable id="v_x">x</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_ch">ch</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_s">s</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_c">c</field>
                <value name="VALUE">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
                <next>
                  <block type="py_for">
                    <field name="VAR" id="v_x">x</field>
                    <value name="SEQ">
                      <block type="variables_get">
                        <field name="VAR" id="v_s">s</field>
                      </block>
                    </value>
                    <statement name="DO">
                      <block type="py_if">
                        <mutation elseif="0" else="0"></mutation>
                        <value name="IF0">
                          <block type="logic_compare">
                            <field name="OP">EQ</field>
                            <value name="A">
                              <block type="variables_get">
                                <field name="VAR" id="v_x">x</field>
                              </block>
                            </value>
                            <value name="B">
                              <block type="variables_get">
                                <field name="VAR" id="v_s">s</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO0">
                          <block type="variables_set">
                            <field name="VAR" id="v_c">c</field>
                            <value name="VALUE">
                              <block type="py_add">
                                <mutation items="2"></mutation>
                                <value name="ARG0">
                                  <block type="variables_get">
                                    <field name="VAR" id="v_c">c</field>
                                  </block>
                                </value>
                                <value name="ARG1">
                                  <block type="math_number">
                                    <field name="NUM">1</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                          </block>
                        </statement>
                      </block>
                    </statement>
                    <next>
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="variables_get">
                            <field name="VAR" id="v_c">c</field>
                          </block>
                        </value>
                        <next>
                          <block type="py_end"></block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "for-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_i">i</field>
            <value name="SEQ">
              <block type="py_range">
                <value name="FROM">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
                <value name="TO">
                  <block type="py_add">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">1</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="BY">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="py_if">
                <mutation elseif="0" else="0"></mutation>
                <value name="IF0">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A">
                      <block type="py_mod">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_i">i</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">2</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_i">i</field>
                      </block>
                    </value>
                  </block>
                </statement>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="py_start" x="48" y="48">
    <next>
      <block type="text_print">
        <value name="TEXT">
          <block type="text">
            <field name="TEXT">Привет, мир</field>
          </block>
        </value>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_предмет">предмет</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_предмет">предмет</field>
        <value name="VALUE">
          <block type="text">
            <field name="TEXT">математика</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get">
                <field name="VAR" id="v_предмет">предмет</field>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_имя">имя</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_имя">имя</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="text">
                <field name="TEXT">Привет!</field>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="py_start" x="48" y="48">
    <next>
      <block type="text_print">
        <value name="TEXT">
          <block type="text">
            <field name="TEXT">Как дела?</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="text">
                <field name="TEXT">Привет!</field>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_имя">имя</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_имя">имя</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_add">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="text">
                    <field name="TEXT">Рад тебя видеть, </field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="variables_get">
                    <field name="VAR" id="v_имя">имя</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_имя">имя</variable>
    <variable id="v_фам">фам</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_фам">фам</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_имя">имя</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_add">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="text">
                        <field name="TEXT">Потом: </field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="variables_get">
                        <field name="VAR" id="v_имя">имя</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="text">
                            <field name="TEXT">Сначала: </field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_фам">фам</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_c">c</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_c">c</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="py_sum">
                        <mutation items="5"></mutation>
                        <value name="ADD0">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="ADD1">
                          <block type="text">
                            <field name="TEXT"> </field>
                          </block>
                        </value>
                        <value name="ADD2">
                          <block type="variables_get">
                            <field name="VAR" id="v_b">b</field>
                          </block>
                        </value>
                        <value name="ADD3">
                          <block type="text">
                            <field name="TEXT"> </field>
                          </block>
                        </value>
                        <value name="ADD4">
                          <block type="variables_get">
                            <field name="VAR" id="v_c">c</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_блюдо">блюдо</variable>
    <variable id="v_цена">цена</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_блюдо">блюдо</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_цена">цена</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_sum">
                    <mutation items="4"></mutation>
                    <value name="ADD0">
                      <block type="text">
                        <field name="TEXT">Блюдо: </field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="variables_get">
                        <field name="VAR" id="v_блюдо">блюдо</field>
                      </block>
                    </value>
                    <value name="ADD2">
                      <block type="text">
                        <field name="TEXT">, цена: </field>
                      </block>
                    </value>
                    <value name="ADD3">
                      <block type="variables_get">
                        <field name="VAR" id="v_цена">цена</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_w1">w1</variable>
    <variable id="v_w2">w2</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_w1">w1</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_w2">w2</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_len">
                    <value name="OBJ">
                      <block type="variables_get">
                        <field name="VAR" id="v_w1">w1</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_w1">w1</field>
                      </block>
                    </value>
                    <next>
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="py_len">
                            <value name="OBJ">
                              <block type="variables_get">
                                <field name="VAR" id="v_w2">w2</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="text_print">
                            <value name="TEXT">
                              <block type="variables_get">
                                <field name="VAR" id="v_w2">w2</field>
                              </block>
                            </value>
                            <next>
                              <block type="py_end"></block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "io-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_название">название</variable>
    <variable id="v_номер">номер</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_название">название</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_номер">номер</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_sum">
                    <mutation items="5"></mutation>
                    <value name="ADD0">
                      <block type="text">
                        <field name="TEXT">Партия </field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="variables_get">
                        <field name="VAR" id="v_название">название</field>
                      </block>
                    </value>
                    <value name="ADD2">
                      <block type="text">
                        <field name="TEXT">: </field>
                      </block>
                    </value>
                    <value name="ADD3">
                      <block type="variables_get">
                        <field name="VAR" id="v_номер">номер</field>
                      </block>
                    </value>
                    <value name="ADD4">
                      <block type="text">
                        <field name="TEXT"> — OK</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_x">x</variable>
    <variable id="v_фрукты">фрукты</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_фрукты">фрукты</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="text">
                <field name="TEXT">яблоко</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="text">
                <field name="TEXT">банан</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="text">
                <field name="TEXT">груша</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_x">x</field>
            <value name="SEQ">
              <block type="variables_get">
                <field name="VAR" id="v_фрукты">фрукты</field>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_x">x</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_числа">числа</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_числа">числа</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_list_insert">
            <value name="OBJ">
              <block type="variables_get">
                <field name="VAR" id="v_числа">числа</field>
              </block>
            </value>
            <value name="INDEX">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">4</field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_числа">числа</field>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
    <variable id="v_x">x</variable>
    <variable id="v_числа">числа</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_числа">числа</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">10</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">20</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">30</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_s">s</field>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <next>
              <block type="py_for">
                <field name="VAR" id="v_x">x</field>
                <value name="SEQ">
                  <block type="variables_get">
                    <field name="VAR" id="v_числа">числа</field>
                  </block>
                </value>
                <statement name="DO">
                  <block type="variables_set">
                    <field name="VAR" id="v_s">s</field>
                    <value name="VALUE">
                      <block type="py_mul">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_s">s</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_x">x</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_s">s</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_числа">числа</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_числа">числа</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="4"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">4</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_list_reverse">
            <value name="OBJ">
              <block type="variables_get">
                <field name="VAR" id="v_числа">числа</field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_числа">числа</field>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">10</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">20</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_list_remove">
            <value name="OBJ">
              <block type="variables_get">
                <field name="VAR" id="v_a">a</field>
              </block>
            </value>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">10</field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_len">
                    <value name="OBJ">
                      <block type="variables_get">
                        <field name="VAR" id="v_a">a</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_rev">rev</variable>
    <variable id="v_x">x</variable>
    <variable id="v_числа">числа</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_числа">числа</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="4"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">4</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_rev">rev</field>
            <value name="VALUE">
              <block type="lists_create_empty">
              </block>
            </value>
            <next>
              <block type="py_for">
                <field name="VAR" id="v_x">x</field>
                <value name="SEQ">
                  <block type="variables_get">
                    <field name="VAR" id="v_числа">числа</field>
                  </block>
                </value>
                <statement name="DO">
                  <block type="py_list_append">
                    <value name="OBJ">
                      <block type="variables_get">
                        <field name="VAR" id="v_rev">rev</field>
                      </block>
                    </value>
                    <value name="VALUE">
                      <block type="variables_get">
                        <field name="VAR" id="v_x">x</field>
                      </block>
                    </value>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_rev">rev</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_big">big</variable>
    <variable id="v_nums">nums</variable>
    <variable id="v_x">x</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_nums">nums</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="5"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">8</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">5</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">11</field>
              </block>
            </value>
            <value name="ADD4">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_big">big</field>
            <value name="VALUE">
              <block type="lists_create_empty">
              </block>
            </value>
            <next>
              <block type="py_for">
                <field name="VAR" id="v_x">x</field>
                <value name="SEQ">
                  <block type="variables_get">
                    <field name="VAR" id="v_nums">nums</field>
                  </block>
                </value>
                <statement name="DO">
                  <block type="py_if">
                    <mutation elseif="0" else="0"></mutation>
                    <value name="IF0">
                      <block type="logic_compare">
                        <field name="OP">GT</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_x">x</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="math_number">
                            <field name="NUM">10</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="py_list_append">
                        <value name="OBJ">
                          <block type="variables_get">
                            <field name="VAR" id="v_big">big</field>
                          </block>
                        </value>
                        <value name="VALUE">
                          <block type="variables_get">
                            <field name="VAR" id="v_x">x</field>
                          </block>
                        </value>
                      </block>
                    </statement>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_big">big</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_nums">nums</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_nums">nums</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="5"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">10</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">20</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">30</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">40</field>
              </block>
            </value>
            <value name="ADD4">
              <block type="math_number">
                <field name="NUM">50</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_i">i</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="text">
                    <field name="TEXT">ошибка</field>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_nums">nums</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_nums">nums</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="5"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">3</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">4</field>
              </block>
            </value>
            <value name="ADD4">
              <block type="math_number">
                <field name="NUM">5</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_list_remove">
            <value name="OBJ">
              <block type="variables_get">
                <field name="VAR" id="v_nums">nums</field>
              </block>
            </value>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">5</field>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_nums">nums</field>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "list-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_nums">nums</variable>
    <variable id="v_x">x</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_nums">nums</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="5"></mutation>
            <value name="ADD0">
              <block type="math_number">
                <field name="NUM">10</field>
              </block>
            </value>
            <value name="ADD1">
              <block type="math_number">
                <field name="NUM">20</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="math_number">
                <field name="NUM">30</field>
              </block>
            </value>
            <value name="ADD3">
              <block type="math_number">
                <field name="NUM">40</field>
              </block>
            </value>
            <value name="ADD4">
              <block type="math_number">
                <field name="NUM">50</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_for">
            <field name="VAR" id="v_x">x</field>
            <value name="SEQ">
              <block type="variables_get">
                <field name="VAR" id="v_nums">nums</field>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_x">x</field>
                  </block>
                </value>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="py_start" x="48" y="48">
    <next>
      <block type="text_print">
        <value name="TEXT">
          <block type="py_add">
            <mutation items="2"></mutation>
            <value name="ARG0">
              <block type="math_number">
                <field name="NUM">8</field>
              </block>
            </value>
            <value name="ARG1">
              <block type="math_number">
                <field name="NUM">12</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_add">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="math_number">
                    <field name="NUM">10</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_div">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_b">b</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="py_start" x="48" y="48">
    <next>
      <block type="text_print">
        <value name="TEXT">
          <block type="py_mul">
            <mutation items="2"></mutation>
            <value name="ARG0">
              <block type="math_number">
                <field name="NUM">6</field>
              </block>
            </value>
            <value name="ARG1">
              <block type="math_number">
                <field name="NUM">2</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="py_start" x="48" y="48">
    <next>
      <block type="text_print">
        <value name="TEXT">
          <block type="py_floordiv">
            <mutation items="2"></mutation>
            <value name="ARG0">
              <block type="math_number">
                <field name="NUM">17</field>
              </block>
            </value>
            <value name="ARG1">
              <block type="math_number">
                <field name="NUM">5</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_end"></block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_км">км</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_км">км</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_sum">
                <mutation items="3"></mutation>
                <value name="ADD0">
                  <block type="math_number">
                    <field name="NUM">50</field>
                  </block>
                </value>
                <value name="ADD1">
                  <block type="math_number">
                    <field name="NUM">15</field>
                  </block>
                </value>
                <value name="ADD2">
                  <block type="variables_get">
                    <field name="VAR" id="v_км">км</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_м">м</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_м">м</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_div">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="variables_get">
                    <field name="VAR" id="v_м">м</field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="math_number">
                    <field name="NUM">60</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_mod">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_м">м</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">60</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">528</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_mod">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="math_number">
                    <field name="NUM">100</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_скидка">скидка</variable>
    <variable id="v_цена">цена</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_цена">цена</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_скидка">скидка</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_sub">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_цена">цена</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="variables_get">
                        <field name="VAR" id="v_скидка">скидка</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "numbers-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_sub">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_add">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">1</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_слово">слово</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_слово">слово</field>
        <value name="VALUE">
          <block type="text">
            <field name="TEXT">python</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_lower">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_слово">слово</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_с">с</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_с">с</field>
        <value name="VALUE">
          <block type="text">
            <field name="TEXT">  кот  </field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_upper">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_с">с</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_слово">слово</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_слово">слово</field>
        <value name="VALUE">
          <block type="text">
            <field name="TEXT">Привет</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_find">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_слово">слово</field>
                  </block>
                </value>
                <value name="SUB">
                  <block type="text">
                    <field name="TEXT">ри</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_слово">слово</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_слово">слово</field>
        <value name="VALUE">
          <block type="text">
            <field name="TEXT">кот</field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_replace">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_слово">слово</field>
                  </block>
                </value>
                <value name="OLD">
                  <block type="text">
                    <field name="TEXT">т</field>
                  </block>
                </value>
                <value name="NEW">
                  <block type="text">
                    <field name="TEXT">а</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_lower">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_c">c</variable>
    <variable id="v_ch">ch</variable>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_c">c</field>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <next>
              <block type="py_for">
                <field name="VAR" id="v_ch">ch</field>
                <value name="SEQ">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
                <statement name="DO">
                  <block type="py_if">
                    <mutation elseif="0" else="0"></mutation>
                    <value name="IF0">
                      <block type="logic_negate">
                        <value name="BOOL">
                          <block type="py_in">
                            <value name="NEEDLE">
                              <block type="variables_get">
                                <field name="VAR" id="v_ch">ch</field>
                              </block>
                            </value>
                            <value name="HAYSTACK">
                              <block type="text">
                                <field name="TEXT">аеиоуыэюя</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="variables_set">
                        <field name="VAR" id="v_c">c</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_c">c</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="math_number">
                                <field name="NUM">1</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </statement>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_c">c</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="text">
                <field name="TEXT">палиндром</field>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_add">
                <mutation items="2"></mutation>
                <value name="ARG0">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
                <value name="ARG1">
                  <block type="text">
                    <field name="TEXT">[]</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_sum">
                <mutation items="3"></mutation>
                <value name="ADD0">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
                <value name="ADD1">
                  <block type="text">
                    <field name="TEXT"> </field>
                  </block>
                </value>
                <value name="ADD2">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "str-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="py_input">
            <field name="PROMPT"></field>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="py_str_upper">
                <value name="OBJ">
                  <block type="variables_get">
                    <field name="VAR" id="v_s">s</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-01": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_i">i</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">1</field>
          </block>
        </value>
        <next>
          <block type="py_while">
            <value name="COND">
              <block type="logic_compare">
                <field name="OP">LTE</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_i">i</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">4</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_i">i</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set">
                    <field name="VAR" id="v_i">i</field>
                    <value name="VALUE">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_i">i</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">1</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-02": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_t">t</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_t">t</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">5</field>
          </block>
        </value>
        <next>
          <block type="py_while">
            <value name="COND">
              <block type="logic_compare">
                <field name="OP">GT</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_t">t</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_t">t</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set">
                    <field name="VAR" id="v_t">t</field>
                    <value name="VALUE">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_t">t</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">1</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-03": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_s">s</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_i">i</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">1</field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_s">s</field>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <next>
              <block type="py_while">
                <value name="COND">
                  <block type="logic_compare">
                    <field name="OP">LTE</field>
                    <value name="A">
                      <block type="variables_get">
                        <field name="VAR" id="v_i">i</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">5</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO">
                  <block type="variables_set">
                    <field name="VAR" id="v_s">s</field>
                    <value name="VALUE">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_s">s</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_i">i</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set">
                        <field name="VAR" id="v_i">i</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_i">i</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="math_number">
                                <field name="NUM">2</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_s">s</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-04": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">1</field>
          </block>
        </value>
        <next>
          <block type="py_while">
            <value name="COND">
              <block type="logic_compare">
                <field name="OP">LTE</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">10</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set">
                    <field name="VAR" id="v_n">n</field>
                    <value name="VALUE">
                      <block type="py_add">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">2</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-05": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_i">i</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_i">i</field>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">0</field>
              </block>
            </value>
            <next>
              <block type="py_while">
                <value name="COND">
                  <block type="logic_compare">
                    <field name="OP">LTE</field>
                    <value name="A">
                      <block type="variables_get">
                        <field name="VAR" id="v_i">i</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO">
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="text">
                        <field name="TEXT">шаг</field>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set">
                        <field name="VAR" id="v_i">i</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_i">i</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="math_number">
                                <field name="NUM">1</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="py_end"></block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-06": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="py_while">
            <value name="COND">
              <block type="logic_compare">
                <field name="OP">GT</field>
                <value name="A">
                  <block type="variables_get">
                    <field name="VAR" id="v_n">n</field>
                  </block>
                </value>
                <value name="B">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO">
              <block type="text_print">
                <value name="TEXT">
                  <block type="py_mod">
                    <mutation items="2"></mutation>
                    <value name="ARG0">
                      <block type="variables_get">
                        <field name="VAR" id="v_n">n</field>
                      </block>
                    </value>
                    <value name="ARG1">
                      <block type="math_number">
                        <field name="NUM">10</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="variables_set">
                    <field name="VAR" id="v_n">n</field>
                    <value name="VALUE">
                      <block type="py_floordiv">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="math_number">
                            <field name="NUM">10</field>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="py_end"></block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-07": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_s">s</variable>
    <variable id="v_x">x</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_s">s</field>
        <value name="VALUE">
          <block type="math_number">
            <field name="NUM">0</field>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_x">x</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_while">
                <value name="COND">
                  <block type="logic_compare">
                    <field name="OP">NEQ</field>
                    <value name="A">
                      <block type="variables_get">
                        <field name="VAR" id="v_x">x</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO">
                  <block type="variables_set">
                    <field name="VAR" id="v_x">x</field>
                    <value name="VALUE">
                      <block type="py_convert">
                        <field name="TO">INT</field>
                        <value name="VALUE">
                          <block type="py_input">
                            <field name="PROMPT"></field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set">
                        <field name="VAR" id="v_s">s</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_s">s</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="variables_get">
                                <field name="VAR" id="v_x">x</field>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_s">s</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-08": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_a">a</variable>
    <variable id="v_b">b</variable>
    <variable id="v_t">t</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_a">a</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_b">b</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="py_while">
                <value name="COND">
                  <block type="logic_compare">
                    <field name="OP">NEQ</field>
                    <value name="A">
                      <block type="variables_get">
                        <field name="VAR" id="v_b">b</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO">
                  <block type="variables_set">
                    <field name="VAR" id="v_t">t</field>
                    <value name="VALUE">
                      <block type="py_mod">
                        <mutation items="2"></mutation>
                        <value name="ARG0">
                          <block type="variables_get">
                            <field name="VAR" id="v_a">a</field>
                          </block>
                        </value>
                        <value name="ARG1">
                          <block type="variables_get">
                            <field name="VAR" id="v_b">b</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set">
                        <field name="VAR" id="v_a">a</field>
                        <value name="VALUE">
                          <block type="py_mod">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_a">a</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="variables_get">
                                <field name="VAR" id="v_b">b</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="variables_set">
                            <field name="VAR" id="v_b">b</field>
                            <value name="VALUE">
                              <block type="variables_get">
                                <field name="VAR" id="v_t">t</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="text_print">
                    <value name="TEXT">
                      <block type="variables_get">
                        <field name="VAR" id="v_a">a</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_end"></block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-09": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_base">base</variable>
    <variable id="v_exp">exp</variable>
    <variable id="v_i">i</variable>
    <variable id="v_result">result</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_base">base</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_exp">exp</field>
            <value name="VALUE">
              <block type="py_convert">
                <field name="TO">INT</field>
                <value name="VALUE">
                  <block type="py_input">
                    <field name="PROMPT"></field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_result">result</field>
                <value name="VALUE">
                  <block type="math_number">
                    <field name="NUM">1</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set">
                    <field name="VAR" id="v_i">i</field>
                    <value name="VALUE">
                      <block type="math_number">
                        <field name="NUM">0</field>
                      </block>
                    </value>
                    <next>
                      <block type="py_while">
                        <value name="COND">
                          <block type="logic_compare">
                            <field name="OP">LTE</field>
                            <value name="A">
                              <block type="variables_get">
                                <field name="VAR" id="v_i">i</field>
                              </block>
                            </value>
                            <value name="B">
                              <block type="variables_get">
                                <field name="VAR" id="v_exp">exp</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO">
                          <block type="variables_set">
                            <field name="VAR" id="v_result">result</field>
                            <value name="VALUE">
                              <block type="py_mul">
                                <mutation items="2"></mutation>
                                <value name="ARG0">
                                  <block type="variables_get">
                                    <field name="VAR" id="v_result">result</field>
                                  </block>
                                </value>
                                <value name="ARG1">
                                  <block type="variables_get">
                                    <field name="VAR" id="v_base">base</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="variables_set">
                                <field name="VAR" id="v_i">i</field>
                                <value name="VALUE">
                                  <block type="py_add">
                                    <mutation items="2"></mutation>
                                    <value name="ARG0">
                                      <block type="variables_get">
                                        <field name="VAR" id="v_i">i</field>
                                      </block>
                                    </value>
                                    <value name="ARG1">
                                      <block type="math_number">
                                        <field name="NUM">1</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <next>
                          <block type="text_print">
                            <value name="TEXT">
                              <block type="variables_get">
                                <field name="VAR" id="v_result">result</field>
                              </block>
                            </value>
                            <next>
                              <block type="py_end"></block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
    "while-fix-10": """<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="v_count">count</variable>
    <variable id="v_d">d</variable>
    <variable id="v_n">n</variable>
  </variables>
  <block type="py_start" x="48" y="48">
    <next>
      <block type="variables_set">
        <field name="VAR" id="v_n">n</field>
        <value name="VALUE">
          <block type="py_convert">
            <field name="TO">INT</field>
            <value name="VALUE">
              <block type="py_input">
                <field name="PROMPT"></field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="v_d">d</field>
            <value name="VALUE">
              <block type="math_number">
                <field name="NUM">1</field>
              </block>
            </value>
            <next>
              <block type="variables_set">
                <field name="VAR" id="v_count">count</field>
                <value name="VALUE">
                  <block type="math_number">
                    <field name="NUM">0</field>
                  </block>
                </value>
                <next>
                  <block type="py_while">
                    <value name="COND">
                      <block type="logic_compare">
                        <field name="OP">LTE</field>
                        <value name="A">
                          <block type="variables_get">
                            <field name="VAR" id="v_d">d</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="variables_get">
                            <field name="VAR" id="v_n">n</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO">
                      <block type="variables_set">
                        <field name="VAR" id="v_count">count</field>
                        <value name="VALUE">
                          <block type="py_add">
                            <mutation items="2"></mutation>
                            <value name="ARG0">
                              <block type="variables_get">
                                <field name="VAR" id="v_count">count</field>
                              </block>
                            </value>
                            <value name="ARG1">
                              <block type="math_number">
                                <field name="NUM">1</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="variables_set">
                            <field name="VAR" id="v_d">d</field>
                            <value name="VALUE">
                              <block type="py_add">
                                <mutation items="2"></mutation>
                                <value name="ARG0">
                                  <block type="variables_get">
                                    <field name="VAR" id="v_d">d</field>
                                  </block>
                                </value>
                                <value name="ARG1">
                                  <block type="math_number">
                                    <field name="NUM">1</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <next>
                      <block type="text_print">
                        <value name="TEXT">
                          <block type="variables_get">
                            <field name="VAR" id="v_count">count</field>
                          </block>
                        </value>
                        <next>
                          <block type="py_end"></block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>""",
}

/**
 * Уроки с готовыми примерами и заданиями.
 */

const LESSONS = [
  {
    id: "hello",
    title: "1. Первая программа",
    description: `
      <h3>Привет, Python!</h3>
      <p>Научитесь выводить текст на экран с помощью блока <strong>вывести</strong>.</p>
      <ul>
        <li>Подключите блок «вывести» между <strong>Начало</strong> и <strong>Конец</strong></li>
        <li>Вставьте в него текст, например «Привет, мир!»</li>
        <li>Нажмите «Запустить»</li>
      </ul>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="text_print" x="50" y="50">
        <value name="TEXT">
          <shadow type="text"><field name="TEXT">Привет, мир!</field></shadow>
        </value>
      </block>
    </xml>`,
  },
  {
    id: "variables",
    title: "2. Переменные",
    description: `
      <h3>Хранение данных</h3>
      <p>Переменные позволяют сохранять значения. Создайте переменную <strong>имя</strong> и выведите её.</p>
      <ul>
        <li>Используйте блок «задать переменной»</li>
        <li>Затем блок «получить переменную» внутри «вывести»</li>
      </ul>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="50" y="50">
        <field name="VAR">имя</field>
        <value name="VALUE">
          <shadow type="text"><field name="TEXT">Алексей</field></shadow>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get"><field name="VAR">имя</field></block>
            </value>
          </block>
        </next>
      </block>
    </xml>`,
  },
  {
    id: "math",
    title: "3. Математика",
    description: `
      <h3>Арифметические операции</h3>
      <p>Python умеет считать! Сложите два числа и выведите результат.</p>
      <ul>
        <li>Блок «задать переменной» → результат = 15 + 27</li>
        <li>Выведите переменную <strong>результат</strong></li>
      </ul>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="50" y="50">
        <field name="VAR">результат</field>
        <value name="VALUE">
          <block type="math_arithmetic">
            <field name="OP">ADD</field>
            <value name="A"><shadow type="math_number"><field name="NUM">15</field></shadow></value>
            <value name="B"><shadow type="math_number"><field name="NUM">27</field></shadow></value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get"><field name="VAR">результат</field></block>
            </value>
          </block>
        </next>
      </block>
    </xml>`,
  },
  {
    id: "conditions",
    title: "4. Условия if/else",
    description: `
      <h3>Ветвление программы</h3>
      <p>Программа может принимать решения. Если число больше 10 — выведите «большое», иначе «маленькое».</p>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="50" y="50">
        <field name="VAR">число</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">15</field></shadow></value>
        <next>
          <block type="py_ifelse">
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">GT</field>
                <value name="A"><block type="variables_get"><field name="VAR">число</field></block></value>
                <value name="B"><shadow type="math_number"><field name="NUM">10</field></shadow></value>
              </block>
            </value>
            <statement name="DO0">
              <block type="text_print">
                <value name="TEXT"><shadow type="text"><field name="TEXT">большое</field></shadow></value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="text_print">
                <value name="TEXT"><shadow type="text"><field name="TEXT">маленькое</field></shadow></value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </xml>`,
  },
  {
    id: "loops",
    title: "5. Цикл for",
    description: `
      <h3>Перебор элементов</h3>
      <p>Цикл <strong>for элемент in ...</strong> перебирает элементы списка, строки или диапазона <strong>range(...)</strong>.</p>
      <p>Выведите числа от 1 до 5, подключив блок «диапазон» ко второму входу цикла.</p>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="py_for" x="50" y="50">
        <field name="VAR">i</field>
        <value name="SEQ">
          <block type="py_range">
            <value name="FROM"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <value name="TO"><shadow type="math_number"><field name="NUM">6</field></shadow></value>
            <value name="BY"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
          </block>
        </value>
        <statement name="DO">
          <block type="text_print">
            <value name="TEXT"><block type="variables_get"><field name="VAR">i</field></block></value>
          </block>
        </statement>
      </block>
    </xml>`,
  },
  {
    id: "lists",
    title: "6. Списки",
    description: `
      <h3>Работа со списками</h3>
      <p>Списки хранят несколько значений. Создайте список фруктов и выведите первый элемент.</p>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="50" y="50">
        <field name="VAR">фрукты</field>
        <value name="VALUE">
          <block type="lists_create_with">
            <mutation items="3"></mutation>
            <value name="ADD0"><shadow type="text"><field name="TEXT">яблоко</field></shadow></value>
            <value name="ADD1"><shadow type="text"><field name="TEXT">банан</field></shadow></value>
            <value name="ADD2"><shadow type="text"><field name="TEXT">груша</field></shadow></value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="lists_getIndex">
                <mutation statement="false" at="true"></mutation>
                <field name="MODE">GET</field>
                <field name="WHERE">FROM_START</field>
                <value name="VALUE"><block type="variables_get"><field name="VAR">фрукты</field></block></value>
                <value name="AT"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
              </block>
            </value>
          </block>
        </next>
      </block>
    </xml>`,
  },
  {
    id: "random",
    title: "7. Случайное число",
    description: `
      <h3>Генератор случайных чисел</h3>
      <p>Блок <strong>случайное число</strong> из раздела «Математика» выбирает число в заданном диапазоне.</p>
      <ul>
        <li>Задайте диапазон от 1 до 6</li>
        <li>Выведите результат — как бросок кубика</li>
      </ul>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="40" y="40">
        <field name="VAR">кубик</field>
        <value name="VALUE">
          <block type="math_random_int">
            <value name="FROM"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <value name="TO"><shadow type="math_number"><field name="NUM">6</field></shadow></value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get"><field name="VAR">кубик</field></block>
            </value>
          </block>
        </next>
      </block>
    </xml>`,
  },
  {
    id: "text",
    title: "8. Работа с текстом",
    description: `
      <h3>Строки и операции</h3>
      <p>Соедините два слова и переведите результат в верхний регистр.</p>
    `,
    xml: `<xml xmlns="https://developers.google.com/blockly/xml">
      <block type="variables_set" x="40" y="40">
        <field name="VAR">фраза</field>
        <value name="VALUE">
          <block type="text_changeCase">
            <field name="CASE">UPPERCASE</field>
            <value name="TEXT">
              <block type="text_join">
                <mutation items="2"></mutation>
                <value name="ADD0"><shadow type="text"><field name="TEXT">Привет, </field></shadow></value>
                <value name="ADD1"><shadow type="text"><field name="TEXT">Python!</field></shadow></value>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="text_print">
            <value name="TEXT">
              <block type="variables_get"><field name="VAR">фраза</field></block>
            </value>
          </block>
        </next>
      </block>
    </xml>`,
  },
];

"""English translations for I/O tasks (io-01..io-35, io-fix-01..io-fix-10)."""

from __future__ import annotations

_FIX_INTRO = (
    "A program is already assembled in the workspace, but it behaves incorrectly when checked. "
    "Find the mistake in the blocks and fix it."
)

IO: dict[str, dict] = {
    "io-01": {
        "title": "Hello, world!",
        "condition": (
            "By tradition, the first program in any language greets the world. "
            "Print on screen: Hello, world!"
        ),
        "tests": [{"expected_output": "Hello, world!"}],
    },
    "io-02": {
        "title": "New student",
        "condition": (
            "A new student joined the class. Write her name on the door sign — "
            "print on screen: Anna"
        ),
        "tests": [{"expected_output": "Anna"}],
    },
    "io-03": {
        "title": "School poster",
        "condition": (
            "A poster on the wall has one big word. "
            "Help print the sign from the poster: School"
        ),
        "tests": [{"expected_output": "School"}],
    },
    "io-04": {
        "title": "Favorite subject",
        "condition": (
            "A student answers the question «Which subject do you like most?». "
            "Save the answer computer science in variable subject and show it on screen."
        ),
        "tests": [{"expected_output": "computer science"}],
    },
    "io-05": {
        "title": "City on a form",
        "condition": (
            "An olympiad registration form has a «City» field. "
            "Store London in variable city and print it."
        ),
        "tests": [{"expected_output": "London"}],
    },
    "io-06": {
        "title": "Two greetings",
        "condition": (
            "Two friends chat in a messenger. "
            "Print their lines in order: first Hello!, then How are you?"
        ),
        "tests": [{"expected_output": "Hello!\nHow are you?"}],
    },
    "io-07": {
        "title": "Countdown before start",
        "condition": (
            "Before a race the referee counts aloud. "
            "Print three lines: One, Two, Three"
        ),
        "tests": [{"expected_output": "One\nTwo\nThree"}],
    },
    "io-08": {
        "title": "Variable and text",
        "condition": (
            "You started learning a new language. Store it in variable language = Python, "
            "then print the phrase I am learning Python "
            "(you can build it with «join text» or print the variable separately)."
        ),
        "tests": [{"expected_output": "I am learning Python"}],
    },
    "io-09": {
        "title": "Introduction",
        "condition": (
            "A robot greets guests at the entrance. Ask for a name with an input block "
            "and reply: Hello,  with the entered name"
        ),
        "tests": [
            {"stdin": "Masha\n", "expected_output": "Hello, Masha"},
            {"stdin": "Peter\n", "expected_output": "Hello, Peter"},
        ],
    },
    "io-10": {
        "title": "Animal quiz",
        "condition": (
            "The quiz host asks: «Name your favorite animal!» "
            "Ask for an answer with an input block and repeat it on screen — "
            "as if confirming the contestant's answer."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "cat"},
            {"stdin": "dolphin\n", "expected_output": "dolphin"},
        ],
    },
    "io-11": {
        "title": "Postcard",
        "condition": (
            "A postcard needs the sender's city. "
            "Ask for the city with an input block, save it in variable city and print it."
        ),
        "tests": [
            {"stdin": "Paris\n", "expected_output": "Paris"},
            {"stdin": "Berlin\n", "expected_output": "Berlin"},
        ],
    },
    "io-12": {
        "title": "Friend's profile",
        "condition": (
            "Make a mini profile: ask for name and favorite color. "
            "Show both answers — each on a new line."
        ),
        "tests": [{"stdin": "Olivia\nblue\n", "expected_output": "Olivia\nblue"}],
    },
    "io-13": {
        "title": "Echo machine",
        "condition": (
            "An echo machine repeats everything you say — twice. "
            "Ask for a word and print it two times in a row (two «print» blocks)."
        ),
        "tests": [{"stdin": "Hello\n", "expected_output": "Hello\nHello"}],
    },
    "io-14": {
        "title": "Player profile",
        "condition": (
            "A game creates a character profile. "
            "Ask for name, then age (as text) and print both fields on separate lines."
        ),
        "tests": [{"stdin": "Igor\n12\n", "expected_output": "Igor\n12"}],
    },
    "io-15": {
        "title": "Secret word",
        "condition": (
            "An agent writes a code word in a notebook. "
            "Ask for the secret word, save it in variable word and print the notebook entry."
        ),
        "tests": [{"stdin": "Python\n", "expected_output": "Python"}],
    },
    "io-16": {
        "title": "Coach's command",
        "condition": (
            "The coach gives a short command to athletes. "
            "Set command = Run! and duplicate it on screen twice."
        ),
        "tests": [{"expected_output": "Run!\nRun!"}],
    },
    "io-17": {
        "title": "Mini story",
        "condition": (
            "Write a short three-line dialogue — each on a new line:\n"
            "— Hello!\n— Hello!\n— Shall we go for a walk?"
        ),
        "tests": [{"expected_output": "— Hello!\n— Hello!\n— Shall we go for a walk?"}],
    },
    "io-18": {
        "title": "Hero card",
        "condition": (
            "In a role-playing game a character has a name and a trait. "
            "Create name = Hero and title = brave, then print both lines."
        ),
        "tests": [{"expected_output": "Hero\nbrave"}],
    },
    "io-19": {
        "title": "Greeting by name",
        "condition": (
            "The host welcomes a guest at the door. Ask for a name "
            "and say: Glad to see you, NAME! (substitute the entered name)."
        ),
        "tests": [{"stdin": "Sam\n", "expected_output": "Glad to see you, Sam!"}],
    },
    "io-20": {
        "title": "Input-output marathon",
        "condition": (
            "Final student interview: ask for favorite school subject and dream. "
            "Show both answers, then print a wish: Good luck in school!"
        ),
        "tests": [
            {
                "stdin": "math\nbecome a programmer\n",
                "expected_output": "math\nbecome a programmer\nGood luck in school!",
            },
        ],
    },
    "io-21": {
        "title": "Business card",
        "condition": (
            "Build an electronic card: ask for name, grade (number as text) and city. "
            "Print three lines: Student: NAME, Grade: GRADE, City: CITY"
        ),
        "tests": [
            {
                "stdin": "Masha\n5\nLondon\n",
                "expected_output": "Student: Masha\nGrade: 5\nCity: London",
            },
        ],
    },
    "io-22": {
        "title": "Echo with label",
        "condition": (
            "A radio station repeats a listener's message with a label. "
            "Ask for a word and print You said: WORD twice."
        ),
        "tests": [
            {"stdin": "Python\n", "expected_output": "You said: Python\nYou said: Python"},
        ],
    },
    "io-23": {
        "title": "Three words with commas",
        "condition": (
            "Make a short list of three words: ask for them one by one "
            "and join into one string with comma and space."
        ),
        "tests": [{"stdin": "cat\nhouse\ngarden\n", "expected_output": "cat, house, garden"}],
        "hint": "Save each word in a variable and build the string with «join text».",
    },
    "io-24": {
        "title": "Password length",
        "condition": (
            "Password strength check: ask for a password (as text) "
            "and print on two lines the password itself and its length."
        ),
        "tests": [{"stdin": "abc123\n", "expected_output": "abc123\n6"}],
    },
    "io-25": {
        "title": "Reverse order",
        "condition": (
            "Two envelopes lie in a stack — «first» at the bottom, «second» on top. "
            "Ask for two strings, save in a and b, but print in reverse order: b first, then a."
        ),
        "tests": [{"stdin": "first\nsecond\n", "expected_output": "second\nfirst"}],
    },
    "io-26": {
        "title": "Shopping list",
        "condition": (
            "Mom gave a list of three products — ask the user for them "
            "and format a numbered list: 1) …, 2) …, 3) … (each item on a new line)."
        ),
        "tests": [
            {"stdin": "milk\nbread\ncheese\n", "expected_output": "1) milk\n2) bread\n3) cheese"},
        ],
    },
    "io-27": {
        "title": "Exclamation",
        "condition": (
            "A fan shouts a word with an exclamation mark. "
            "Ask for a word and add ! at the end when printing."
        ),
        "tests": [{"stdin": "Hooray\n", "expected_output": "Hooray!"}],
    },
    "io-28": {
        "title": "Two numbers as text",
        "condition": (
            "A stock ticker shows a range as text. "
            "Ask for two numbers (as text) and print them with spaces around a dash: num1 - num2"
        ),
        "tests": [{"stdin": "12\n34\n", "expected_output": "12 - 34"}],
    },
    "io-29": {
        "title": "Repeat three times",
        "condition": (
            "An exam mantra: ask for a phrase and print it three times — "
            "each time on a new line."
        ),
        "tests": [{"stdin": "study\n", "expected_output": "study\nstudy\nstudy"}],
    },
    "io-30": {
        "title": "Farewell program",
        "condition": (
            "The program says goodbye to the user. Ask for name and dream, "
            "then print three lines: Hello, NAME! — Your dream: DREAM — Good luck!"
        ),
        "tests": [
            {
                "stdin": "Kate\nscientist\n",
                "expected_output": "Hello, Kate!\nYour dream: scientist\nGood luck!",
            },
        ],
    },
    "io-31": {
        "title": "Field order",
        "condition": (
            "In a logbook the surname comes first, then the first name. "
            "Ask for both values and print two lines: "
            "First: SURNAME and Then: NAME — in that order."
        ),
        "tests": [
            {"stdin": "Smith\nPeter\n", "expected_output": "First: Smith\nThen: Peter"},
        ],
        "hint": "First save both inputs in variables, then plan the output.",
    },
    "io-32": {
        "title": "Code from letters",
        "condition": (
            "A cipher clerk builds a three-letter code with no spaces. "
            "Ask for three letters in a row and print them joined as one string."
        ),
        "tests": [{"stdin": "a\nb\nc\n", "expected_output": "abc"}],
    },
    "io-33": {
        "title": "Menu line",
        "condition": (
            "A cashier prints a receipt: ask for dish name and price (as text). "
            "Print one line: Dish: NAME, price: PRICE USD."
        ),
        "tests": [{"stdin": "soup\n150\n", "expected_output": "Dish: soup, price: 150 USD."}],
    },
    "io-34": {
        "title": "Compare lengths",
        "condition": (
            "A linguist compares two words. Ask for two words and print four lines: "
            "first word, its length, second word, its length."
        ),
        "tests": [{"stdin": "cat\nelephant\n", "expected_output": "cat\n3\nelephant\n8"}],
    },
    "io-35": {
        "title": "Batch label",
        "condition": (
            "A warehouse labels goods. Ask for product name and batch number (as text) "
            "and print: Batch NUMBER: NAME — OK"
        ),
        "tests": [{"stdin": "milk\n42\n", "expected_output": "Batch 42: milk — OK"}],
    },
}

IO_FIX: dict[str, dict] = {
    "io-fix-01": {
        "title": "Fix: Hello, world!",
        "condition": (
            "The first program on the course should greet the world, "
            "but the text appears without an exclamation mark. " + _FIX_INTRO
        ),
        "hint": "Check punctuation in the printed string.",
        "tests": [{"expected_output": "Hello, world!"}],
    },
    "io-fix-02": {
        "title": "Fix: subject variable",
        "condition": (
            "A student saved the answer in variable subject, "
            "but the wrong subject is shown when printing. " + _FIX_INTRO
        ),
        "hint": "Look at which value is assigned to the variable.",
        "tests": [{"expected_output": "computer science"}],
    },
    "io-fix-03": {
        "title": "Fix: introduction",
        "condition": (
            "A robot at the entrance asks for a name but replies only «Hello!» — "
            "without the guest's name. " + _FIX_INTRO
        ),
        "hint": "You need to print not just «Hello!», but «Hello, » and the entered name.",
        "tests": [
            {"stdin": "Masha\n", "expected_output": "Hello, Masha"},
            {"stdin": "Peter\n", "expected_output": "Hello, Peter"},
        ],
    },
    "io-fix-04": {
        "title": "Fix: two greetings",
        "condition": (
            "Two friends' chat is shown backwards: "
            "the second line appears before the first. " + _FIX_INTRO
        ),
        "hint": "Swap the «print» blocks or their texts.",
        "tests": [{"expected_output": "Hello!\nHow are you?"}],
    },
    "io-fix-05": {
        "title": "Fix: greeting by name",
        "condition": (
            "The host greets a guest with «Glad to see you, …», "
            "but the exclamation mark at the end is missing. " + _FIX_INTRO
        ),
        "hint": "The greeting should end with an exclamation mark.",
        "tests": [{"stdin": "Sam\n", "expected_output": "Glad to see you, Sam!"}],
    },
    "io-fix-06": {
        "title": "Fix: field order",
        "condition": (
            "A log entry prints first name, then surname — "
            "but the log uses the opposite order. " + _FIX_INTRO
        ),
        "hint": "The surname should come first, then the first name.",
        "tests": [
            {"stdin": "Smith\nPeter\n", "expected_output": "First: Smith\nThen: Peter"},
        ],
    },
    "io-fix-07": {
        "title": "Fix: code from letters",
        "condition": (
            "A cipher clerk joins three letters, but spaces appear between them — "
            "the code is longer than needed. " + _FIX_INTRO
        ),
        "hint": "The code should be continuous — no spaces between letters.",
        "tests": [{"stdin": "a\nb\nc\n", "expected_output": "abc"}],
    },
    "io-fix-08": {
        "title": "Fix: menu line",
        "condition": (
            "The receipt is almost correct, but after the price "
            "the currency unit is missing. " + _FIX_INTRO
        ),
        "hint": "After the price there should be «USD.».",
        "tests": [{"stdin": "soup\n150\n", "expected_output": "Dish: soup, price: 150 USD."}],
    },
    "io-fix-09": {
        "title": "Fix: compare lengths",
        "condition": (
            "A linguist compares words, but each word's length "
            "is printed before the word itself. " + _FIX_INTRO
        ),
        "hint": "First the word, then its length.",
        "tests": [{"stdin": "cat\nelephant\n", "expected_output": "cat\n3\nelephant\n8"}],
    },
    "io-fix-10": {
        "title": "Fix: batch label",
        "condition": (
            "Warehouse labeling swapped batch number and product name. " + _FIX_INTRO
        ),
        "hint": "After «Batch» should come the number, not the name.",
        "tests": [{"stdin": "milk\n42\n", "expected_output": "Batch 42: milk — OK"}],
    },
}

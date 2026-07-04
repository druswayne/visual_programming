"""English translations for conditions tasks (cond-01..cond-35, cond-fix-01..cond-fix-10)."""

from __future__ import annotations

_FIX_INTRO = (
    "A program is already assembled in the workspace, but it behaves incorrectly when checked. "
    "Find the mistake in the blocks and fix it."
)

CONDITIONS: dict[str, dict] = {
    "cond-01": {
        "title": "Greater than ten?",
        "condition": (
            "A thermometer reads 15 degrees — store it in variable number. "
            "If the value is greater than 10, print yes, otherwise — no. "
            "Use an if block and a comparison."
        ),
        "tests": [{"expected_output": "yes"}],
        "hint": "In the condition, use variable «number» and 10 with the «greater than» block.",
    },
    "cond-02": {
        "title": "Below zero",
        "condition": (
            "On a winter morning it is −4 °C outside — save this in variable temperature. "
            "If the temperature is below zero, print frost, otherwise — no frost."
        ),
        "tests": [{"expected_output": "frost"}],
    },
    "cond-03": {
        "title": "Same numbers",
        "condition": (
            "Two players scored the same number of points: a = 8 and b = 8. "
            "Compare the scores and print equal or different."
        ),
        "tests": [{"expected_output": "equal"}],
    },
    "cond-04": {
        "title": "Even or odd",
        "condition": (
            "There are 14 candies in a box — store this in n. "
            "Can they be split evenly between two people? "
            "If n divides by 2 with no remainder, print even, otherwise — odd."
        ),
        "tests": [{"expected_output": "even"}],
        "hint": "First find the remainder of 14 divided by 2, then compare it to zero.",
    },
    "cond-05": {
        "title": "Block «true»",
        "condition": (
            "Check how the logical constant works: "
            "put the true block in the if condition. "
            "When the condition is true — print true, otherwise — false."
        ),
        "tests": [{"expected_output": "true"}],
    },
    "cond-06": {
        "title": "Adult or child",
        "condition": (
            "Ask for age with an input block and convert the answer to an integer. "
            "If age is greater than or equal to 18, print adult, "
            "otherwise — child."
        ),
        "tests": [
            {"stdin": "20\n", "expected_output": "adult"},
            {"stdin": "12\n", "expected_output": "child"},
        ],
    },
    "cond-07": {
        "title": "Sign of a number",
        "condition": (
            "Ask for an integer. Print: "
            "positive if the number is greater than zero; "
            "zero if the number equals zero; "
            "negative if the number is less than zero. "
            "Use an if block with elif and else branches."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "positive"},
            {"stdin": "0\n", "expected_output": "zero"},
            {"stdin": "-3\n", "expected_output": "negative"},
        ],
    },
    "cond-08": {
        "title": "Passed the test",
        "condition": (
            "Ask for a test grade (integer from 1 to 5). "
            "If the grade is greater than or equal to 4, print passed, "
            "otherwise — failed."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "passed"},
            {"stdin": "3\n", "expected_output": "failed"},
        ],
    },
    "cond-09": {
        "title": "Word for a grade",
        "condition": (
            "Ask for a grade (integer). Print one word: "
            "5 → excellent "
            "4 → good "
            "3 → satisfactory "
            "any other → unsatisfactory "
            "Add elif branches in the condition block."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "excellent"},
            {"stdin": "4\n", "expected_output": "good"},
            {"stdin": "2\n", "expected_output": "unsatisfactory"},
        ],
    },
    "cond-10": {
        "title": "Time of day",
        "condition": (
            "Ask for the hour (integer from 0 to 23). Print: "
            "from 6 to 11 inclusive — morning "
            "from 12 to 17 inclusive — afternoon "
            "from 18 to 22 inclusive — evening "
            "otherwise — night"
        ),
        "tests": [
            {"stdin": "8\n", "expected_output": "morning"},
            {"stdin": "14\n", "expected_output": "afternoon"},
            {"stdin": "21\n", "expected_output": "evening"},
            {"stdin": "2\n", "expected_output": "night"},
        ],
        "hint": "Check the hours in order: morning first, then afternoon, and so on.",
    },
    "cond-11": {
        "title": "Who is greater?",
        "condition": (
            "Ask for two integers. "
            "If the first is greater than the second — print first, "
            "if the second is greater — second, "
            "if the numbers are equal — equal."
        ),
        "tests": [
            {"stdin": "10\n3\n", "expected_output": "first"},
            {"stdin": "2\n9\n", "expected_output": "second"},
            {"stdin": "5\n5\n", "expected_output": "equal"},
        ],
    },
    "cond-12": {
        "title": "Can go out?",
        "condition": (
            "Parents decide whether to let a child (age = 10) go outside. "
            "warm = true. "
            "If age is at least 6 and the weather is warm — can go out, otherwise — stay home. "
            "Connect the conditions with an and block."
        ),
        "tests": [{"expected_output": "can go out"}],
    },
    "cond-13": {
        "title": "Need an umbrella?",
        "condition": (
            "Forecast: rain = false, but wind = true. "
            "If it is raining or windy — advise take an umbrella, "
            "otherwise — no umbrella needed. Use an or block."
        ),
        "tests": [{"expected_output": "take an umbrella"}],
    },
    "cond-14": {
        "title": "Secret code",
        "condition": (
            "Ask for a code (as text). "
            "If the entered code equals the string Python, print door open, "
            "otherwise — wrong code."
        ),
        "tests": [
            {"stdin": "Python\n", "expected_output": "door open"},
            {"stdin": "python\n", "expected_output": "wrong code"},
        ],
        "hint": "Compare text exactly — the capital letter P matters.",
    },
    "cond-15": {
        "title": "Vowel or consonant",
        "condition": (
            "Ask for one letter (as text). "
            "If the letter is in the string aeiou (in block), print vowel, "
            "otherwise — consonant."
        ),
        "tests": [
            {"stdin": "o\n", "expected_output": "vowel"},
            {"stdin": "k\n", "expected_output": "consonant"},
        ],
    },
    "cond-16": {
        "title": "Is there a dog?",
        "condition": (
            "Ask for a phrase (as text). "
            "If the text contains the word dog (check with the in block), "
            "print about animals, otherwise — other topic."
        ),
        "tests": [
            {"stdin": "I have a dog\n", "expected_output": "about animals"},
            {"stdin": "I love math\n", "expected_output": "other topic"},
        ],
    },
    "cond-17": {
        "title": "Choose transport",
        "condition": (
            "Ask for a number (integer): 1 — bus, 2 — train, 3 — plane. "
            "Print bus, train, or plane accordingly. "
            "For any other number print unknown."
        ),
        "tests": [
            {"stdin": "1\n", "expected_output": "bus"},
            {"stdin": "3\n", "expected_output": "plane"},
            {"stdin": "9\n", "expected_output": "unknown"},
        ],
    },
    "cond-18": {
        "title": "What is the weather?",
        "condition": (
            "Ask for temperature (integer). Print: "
            "above 30 — hot "
            "above 15 — warm "
            "above 0 — cool "
            "otherwise — cold"
        ),
        "tests": [
            {"stdin": "35\n", "expected_output": "hot"},
            {"stdin": "20\n", "expected_output": "warm"},
            {"stdin": "-5\n", "expected_output": "cold"},
        ],
        "hint": "Check from higher temperature to lower — hot first, then warm.",
    },
    "cond-19": {
        "title": "Allowed on the slide?",
        "condition": (
            "Ask for two numbers: age and height in centimeters (both integers). "
            "If age is at least 12 and height is at least 140, "
            "print allowed, otherwise — not allowed."
        ),
        "tests": [
            {"stdin": "13\n150\n", "expected_output": "allowed"},
            {"stdin": "10\n145\n", "expected_output": "not allowed"},
            {"stdin": "14\n130\n", "expected_output": "not allowed"},
        ],
    },
    "cond-20": {
        "title": "Smart assistant",
        "condition": (
            "Ask for name and age (two inputs). Convert age to an integer. "
            "1) Print Hello, NAME! (substitute the entered name). "
            "2) On the next line: if age ≥ 18 — of legal age, "
            "otherwise — underage. "
            "3) On the next line: if age ≥ 6 and ≤ 17 — "
            "in school, otherwise — not in school."
        ),
        "tests": [
            {
                "stdin": "Anna\n15\n",
                "expected_output": "Hello, Anna!\nunderage\nin school",
            },
            {
                "stdin": "Ivan\n25\n",
                "expected_output": "Hello, Ivan!\nof legal age\nnot in school",
            },
        ],
        "hint": "Save name and age in variables — you will need them several times.",
    },
    "cond-21": {
        "title": "Leap year",
        "condition": (
            "Ask for a year (integer). If the year divides by 4 with no remainder — "
            "print leap year, otherwise — regular."
        ),
        "tests": [
            {"stdin": "2024\n", "expected_output": "leap year"},
            {"stdin": "2023\n", "expected_output": "regular"},
        ],
    },
    "cond-22": {
        "title": "Triangle type",
        "condition": (
            "Ask for three side lengths (integers). "
            "If all three are equal — equilateral. "
            "If exactly two are equal — isosceles. "
            "Otherwise — scalene."
        ),
        "tests": [
            {"stdin": "5\n5\n5\n", "expected_output": "equilateral"},
            {"stdin": "5\n5\n3\n", "expected_output": "isosceles"},
            {"stdin": "3\n4\n5\n", "expected_output": "scalene"},
        ],
    },
    "cond-23": {
        "title": "Grade by points",
        "condition": (
            "Ask for points (0–100). "
            "90 and above — excellent, 70–89 — good, 50–69 — satisfactory, "
            "otherwise — fail."
        ),
        "tests": [
            {"stdin": "95\n", "expected_output": "excellent"},
            {"stdin": "75\n", "expected_output": "good"},
            {"stdin": "55\n", "expected_output": "satisfactory"},
            {"stdin": "40\n", "expected_output": "fail"},
        ],
    },
    "cond-24": {
        "title": "Login and password",
        "condition": (
            "Ask for login and password (two text values). "
            "If login is admin and password is 12345 — access granted, otherwise — denied."
        ),
        "tests": [
            {"stdin": "admin\n12345\n", "expected_output": "access granted"},
            {"stdin": "admin\n0000\n", "expected_output": "denied"},
        ],
    },
    "cond-25": {
        "title": "Positive and even",
        "condition": (
            "Ask for an integer. If it is positive and even — "
            "print suitable, otherwise — not suitable."
        ),
        "tests": [
            {"stdin": "8\n", "expected_output": "suitable"},
            {"stdin": "7\n", "expected_output": "not suitable"},
            {"stdin": "-4\n", "expected_output": "not suitable"},
        ],
    },
    "cond-26": {
        "title": "FizzBuzz",
        "condition": (
            "Ask for integer n. "
            "If n divides by 3 and by 5 — FizzBuzz. "
            "Only by 3 — Fizz. Only by 5 — Buzz. Otherwise — n itself."
        ),
        "tests": [
            {"stdin": "15\n", "expected_output": "FizzBuzz"},
            {"stdin": "9\n", "expected_output": "Fizz"},
            {"stdin": "10\n", "expected_output": "Buzz"},
            {"stdin": "7\n", "expected_output": "7"},
        ],
    },
    "cond-27": {
        "title": "Season",
        "condition": (
            "Ask for month number (1–12). "
            "12, 1, 2 — winter; 3–5 — spring; 6–8 — summer; 9–11 — autumn. "
            "Any other number — error."
        ),
        "tests": [
            {"stdin": "1\n", "expected_output": "winter"},
            {"stdin": "4\n", "expected_output": "spring"},
            {"stdin": "7\n", "expected_output": "summer"},
            {"stdin": "10\n", "expected_output": "autumn"},
        ],
    },
    "cond-28": {
        "title": "Mini calculator",
        "condition": (
            "Ask for an operation sign (+, -, *, / as text) and two integers. "
            "Print the result. For an unknown sign — error."
        ),
        "tests": [
            {"stdin": "+\n5\n3\n", "expected_output": "8"},
            {"stdin": "*\n4\n5\n", "expected_output": "20"},
            {"stdin": "/\n7\n2\n", "expected_output": "3.5"},
            {"stdin": "%\n1\n1\n", "expected_output": "error"},
        ],
    },
    "cond-29": {
        "title": "Strong password",
        "condition": (
            "Ask for a password (text). If the length is at least 8 — "
            "strong, otherwise — weak."
        ),
        "tests": [
            {"stdin": "abcdefgh\n", "expected_output": "strong"},
            {"stdin": "123\n", "expected_output": "weak"},
        ],
    },
    "cond-30": {
        "title": "Final report",
        "condition": (
            "Ask for name, age (integer), and test score (0–100). "
            "Print three lines: "
            "1) Student: NAME "
            "2) if score ≥ 80 — passed, otherwise — failed "
            "3) if age < 10 — junior, otherwise — senior"
        ),
        "tests": [
            {
                "stdin": "Tim\n9\n85\n",
                "expected_output": "Student: Tim\npassed\njunior",
            },
            {
                "stdin": "Anna\n14\n70\n",
                "expected_output": "Student: Anna\nfailed\nsenior",
            },
        ],
    },
    "cond-31": {
        "title": "In range?",
        "condition": (
            "Ask for number x, then bounds a and b (all integers). "
            "If a ≤ x ≤ b, print in range, otherwise — out of range."
        ),
        "tests": [
            {"stdin": "5\n1\n10\n", "expected_output": "in range"},
            {"stdin": "15\n1\n10\n", "expected_output": "out of range"},
            {"stdin": "1\n1\n5\n", "expected_output": "in range"},
        ],
    },
    "cond-32": {
        "title": "Maximum of three",
        "condition": (
            "Ask for three integers. Find the largest and print: "
            "first, second, or third — depending on which number is greatest."
        ),
        "tests": [
            {"stdin": "1\n5\n3\n", "expected_output": "second"},
            {"stdin": "9\n2\n7\n", "expected_output": "first"},
            {"stdin": "4\n4\n8\n", "expected_output": "third"},
        ],
        "hint": "Compare the numbers step by step without printing the maximum value itself.",
    },
    "cond-33": {
        "title": "Divides evenly?",
        "condition": (
            "Ask for dividend and divisor (integers, divisor not zero). "
            "If the dividend divides by the divisor with no remainder — divides, "
            "otherwise — does not divide."
        ),
        "tests": [
            {"stdin": "10\n5\n", "expected_output": "divides"},
            {"stdin": "10\n3\n", "expected_output": "does not divide"},
        ],
    },
    "cond-34": {
        "title": "Triangle possible?",
        "condition": (
            "Three segments a, b, c can form a triangle "
            "if the sum of any two sides is greater than the third. "
            "Ask for three lengths (integers) and print possible or impossible."
        ),
        "tests": [
            {"stdin": "3\n4\n5\n", "expected_output": "possible"},
            {"stdin": "1\n2\n5\n", "expected_output": "impossible"},
            {"stdin": "5\n5\n5\n", "expected_output": "possible"},
        ],
    },
    "cond-35": {
        "title": "Grade jump",
        "condition": (
            "Ask for two grades in a row (integers from 1 to 5). "
            "If the absolute difference is at least 2 — jump, otherwise — stable."
        ),
        "tests": [
            {"stdin": "5\n3\n", "expected_output": "jump"},
            {"stdin": "4\n5\n", "expected_output": "stable"},
            {"stdin": "2\n5\n", "expected_output": "jump"},
        ],
    },
}

CONDITIONS_FIX: dict[str, dict] = {
    "cond-fix-01": {
        "title": "Fix: greater than ten?",
        "condition": (
            "At temperature 15 the program answers «no», "
            "although the value is clearly greater than 10. " + _FIX_INTRO
        ),
        "tests": [{"expected_output": "yes"}],
        "hint": "Check the comparison sign in the condition.",
    },
    "cond-fix-02": {
        "title": "Fix: sign of a number",
        "condition": (
            "The number classifier mixes up labels: "
            "positive numbers are called negative and vice versa. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "positive"},
            {"stdin": "0\n", "expected_output": "zero"},
            {"stdin": "-3\n", "expected_output": "negative"},
        ],
        "hint": "Match each branch to the correct text.",
    },
    "cond-fix-03": {
        "title": "Fix: adult or child",
        "condition": (
            "The age check prints «adult» for a schoolchild "
            "and «child» for an adult — the branches are swapped. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "20\n", "expected_output": "adult"},
            {"stdin": "12\n", "expected_output": "child"},
        ],
        "hint": "At age 20 the output should be «adult», at 12 — «child».",
    },
    "cond-fix-04": {
        "title": "Fix: can go out?",
        "condition": (
            "A 10-year-old child is not allowed outside in warm weather — "
            "the age threshold in the condition is too high. " + _FIX_INTRO
        ),
        "tests": [{"expected_output": "can go out"}],
        "hint": "At age 10 in warm weather, going outside is allowed.",
    },
    "cond-fix-05": {
        "title": "Fix: FizzBuzz",
        "condition": (
            "FizzBuzz on 15 prints only Fizz — "
            "the branch for dividing by both 3 and 5 comes too late. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "15\n", "expected_output": "FizzBuzz"},
            {"stdin": "9\n", "expected_output": "Fizz"},
            {"stdin": "10\n", "expected_output": "Buzz"},
            {"stdin": "7\n", "expected_output": "7"},
        ],
        "hint": "Check division by 3 and 5 together first.",
    },
    "cond-fix-06": {
        "title": "Fix: in range?",
        "condition": (
            "The number 15 is considered «in range» for segment [1, 10] — "
            "only the left bound is checked. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "5\n1\n10\n", "expected_output": "in range"},
            {"stdin": "15\n1\n10\n", "expected_output": "out of range"},
            {"stdin": "1\n1\n5\n", "expected_output": "in range"},
        ],
        "hint": "You need to check both the left and the right bound.",
    },
    "cond-fix-07": {
        "title": "Fix: maximum of three",
        "condition": (
            "Among three numbers the third is the largest, "
            "but the program compares only the first two. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "1\n5\n3\n", "expected_output": "second"},
            {"stdin": "9\n2\n7\n", "expected_output": "first"},
            {"stdin": "4\n4\n8\n", "expected_output": "third"},
        ],
        "hint": "The third number can be the maximum too.",
    },
    "cond-fix-08": {
        "title": "Fix: divides evenly?",
        "condition": (
            "The check whether 10 divides by 5 answers «does not divide» — "
            "integer division is used instead of the remainder. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "10\n5\n", "expected_output": "divides"},
            {"stdin": "10\n3\n", "expected_output": "does not divide"},
        ],
        "hint": "To check divisibility you need the remainder (%).",
    },
    "cond-fix-09": {
        "title": "Fix: triangle",
        "condition": (
            "Segments 1, 2, and 5 are wrongly accepted as a triangle — "
            "only one of the three inequalities is checked. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "3\n4\n5\n", "expected_output": "possible"},
            {"stdin": "1\n2\n5\n", "expected_output": "impossible"},
            {"stdin": "5\n5\n5\n", "expected_output": "possible"},
        ],
        "hint": "You need to check all three pairs of sides.",
    },
    "cond-fix-10": {
        "title": "Fix: grade jump",
        "condition": (
            "Grades 5 and 3 are marked as «stable», "
            "although the difference between them is 2. " + _FIX_INTRO
        ),
        "tests": [
            {"stdin": "5\n3\n", "expected_output": "jump"},
            {"stdin": "4\n5\n", "expected_output": "stable"},
            {"stdin": "2\n5\n", "expected_output": "jump"},
        ],
        "hint": "A jump occurs when the difference is 2 or more.",
    },
}

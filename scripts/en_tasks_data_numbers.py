"""English translations for numbers tasks (numbers-01..numbers-35, numbers-fix-01..numbers-fix-10)."""

from __future__ import annotations

_FIX_INTRO = (
    "A program is already assembled in the workspace, but it behaves incorrectly when checked. "
    "Find the mistake in the blocks and fix it."
)

NUMBERS: dict[str, dict] = {
    "numbers-01": {
        "title": "Candies in a bag",
        "condition": (
            "Masha had 7 candies and a friend gave her 5 more. "
            "Add the numbers with an addition block and print how many candies she has now."
        ),
        "hint": "Put 7 and 5 in the blocks, then print the answer.",
        "tests": [{"expected_output": "12"}],
    },
    "numbers-02": {
        "title": "Coins left",
        "condition": (
            "There were 50 coins in a piggy bank. Masha spent 18. "
            "Subtract and print how many coins remain."
        ),
        "tests": [{"expected_output": "32"}],
    },
    "numbers-03": {
        "title": "Rows in a cinema",
        "condition": (
            "A hall has 8 rows with 12 seats each. "
            "Multiply the numbers and print the total number of seats."
        ),
        "tests": [{"expected_output": "96"}],
    },
    "numbers-04": {
        "title": "Split among four",
        "condition": (
            "Grandma baked 9 pies and split them equally among 4 grandchildren. "
            "Divide 9 / 4 and print the result (a decimal number)."
        ),
        "hint": "Regular division in Python gives a decimal, e.g. 2.25.",
        "tests": [{"expected_output": "2.25"}],
    },
    "numbers-05": {
        "title": "Game score",
        "condition": (
            "A player scored 100 points in a level. "
            "Save the result in variable score and show it on screen."
        ),
        "tests": [{"expected_output": "100"}],
    },
    "numbers-06": {
        "title": "Square of a number",
        "condition": (
            "Compute 6 to the power of 2 (that is 6 × 6) "
            "with a power block and print the area of a square with side 6."
        ),
        "tests": [{"expected_output": "36"}],
    },
    "numbers-07": {
        "title": "Remainder of division",
        "condition": (
            "Peter has 17 stickers. He gives 5 to each friend equally. "
            "How many stickers are left? Use remainder of division for 17 and 5."
        ),
        "tests": [{"expected_output": "2"}],
    },
    "numbers-08": {
        "title": "Full boxes",
        "condition": (
            "A warehouse has 47 apples. Each box holds exactly 6. "
            "How many full boxes can be packed? Use integer division."
        ),
        "tests": [{"expected_output": "7"}],
    },
    "numbers-09": {
        "title": "Two operations in a row",
        "condition": (
            "Compute (10 + 4) × 3: first add, save the result in a variable, "
            "then multiply by 3 and print the answer."
        ),
        "tests": [{"expected_output": "42"}],
    },
    "numbers-10": {
        "title": "Plus ten",
        "condition": (
            "Ask for a number with an input block, convert it to an integer "
            "and add 10. Print the result."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "15"},
            {"stdin": "23\n", "expected_output": "33"},
        ],
    },
    "numbers-11": {
        "title": "Sum of two numbers",
        "condition": (
            "Ask for two integers (two input blocks), convert both to int, "
            "add them and print the sum."
        ),
        "tests": [
            {"stdin": "12\n8\n", "expected_output": "20"},
            {"stdin": "100\n250\n", "expected_output": "350"},
        ],
    },
    "numbers-12": {
        "title": "Average grade",
        "condition": (
            "Ask for two test grades (integers), add them and divide by 2. "
            "Print the average (may be a decimal)."
        ),
        "tests": [
            {"stdin": "5\n4\n", "expected_output": "4.5"},
            {"stdin": "3\n3\n", "expected_output": "3.0"},
        ],
    },
    "numbers-13": {
        "title": "Ticket cost",
        "condition": (
            "A museum ticket costs 150 dollars. Ask how many tickets a family buys, "
            "multiply by 150 and print the total cost."
        ),
        "tests": [
            {"stdin": "2\n", "expected_output": "300"},
            {"stdin": "4\n", "expected_output": "600"},
        ],
    },
    "numbers-14": {
        "title": "Years passed",
        "condition": (
            "Ask for birth year (integer). Subtract it from 2026 and print the age."
        ),
        "tests": [
            {"stdin": "2014\n", "expected_output": "12"},
            {"stdin": "2010\n", "expected_output": "16"},
        ],
    },
    "numbers-15": {
        "title": "Room area",
        "condition": (
            "Ask for room length and width in meters (two decimal numbers). "
            "Convert to float, multiply and print the area."
        ),
        "hint": "For decimals use the «convert to float» block.",
        "tests": [
            {"stdin": "4\n3\n", "expected_output": "12.0"},
            {"stdin": "2.5\n2\n", "expected_output": "5.0"},
        ],
    },
    "numbers-16": {
        "title": "Change at the store",
        "condition": (
            "Ask how many dollars the customer paid (integer). "
            "The item costs 73 dollars. Compute change: paid − 73 and print it."
        ),
        "tests": [
            {"stdin": "100\n", "expected_output": "27"},
            {"stdin": "200\n", "expected_output": "127"},
        ],
    },
    "numbers-17": {
        "title": "Extra balloons",
        "condition": (
            "A pack holds 8 balloons. Ask how many balloons were bought. "
            "Find remainder when dividing by 8 — how many don't fit in full packs."
        ),
        "tests": [
            {"stdin": "25\n", "expected_output": "1"},
            {"stdin": "16\n", "expected_output": "0"},
        ],
    },
    "numbers-18": {
        "title": "Power of two",
        "condition": (
            "In computing 2¹⁰ often appears — an old sense of «kilobyte». "
            "Compute 2 to the power of 10 and print the result."
        ),
        "tests": [{"expected_output": "1024"}],
    },
    "numbers-19": {
        "title": "Perimeter formula",
        "condition": (
            "Rectangle: side a = 7, side b = 3. "
            "Perimeter = 2 × (a + b). Save sides in variables, compute and print perimeter."
        ),
        "tests": [{"expected_output": "20"}],
    },
    "numbers-20": {
        "title": "Math quest",
        "condition": (
            "Ask for integer n. Compute and print three results on separate lines: "
            "1) n + 5 "
            "2) n × n "
            "3) n // 2 (integer half)"
        ),
        "hint": "Save the entered number in a variable and use it three times.",
        "tests": [
            {"stdin": "10\n", "expected_output": "15\n100\n5"},
            {"stdin": "7\n", "expected_output": "12\n49\n3"},
        ],
    },
    "numbers-21": {
        "title": "Area and perimeter",
        "condition": (
            "Ask for rectangle length and width (integers). "
            "Print on two lines: area and perimeter."
        ),
        "tests": [
            {"stdin": "5\n3\n", "expected_output": "15\n16"},
            {"stdin": "10\n2\n", "expected_output": "20\n24"},
        ],
    },
    "numbers-22": {
        "title": "Celsius to Fahrenheit",
        "condition": (
            "Ask for temperature in °C (integer). "
            "Convert with formula F = C × 9 / 5 + 32 and print the result."
        ),
        "tests": [
            {"stdin": "0\n", "expected_output": "32.0"},
            {"stdin": "100\n", "expected_output": "212.0"},
            {"stdin": "20\n", "expected_output": "68.0"},
        ],
    },
    "numbers-23": {
        "title": "Quotient and remainder",
        "condition": (
            "Ask for dividend and divisor (integers). "
            "Print on two lines: integer part (//) and remainder (%)."
        ),
        "tests": [
            {"stdin": "47\n6\n", "expected_output": "7\n5"},
            {"stdin": "20\n4\n", "expected_output": "5\n0"},
        ],
    },
    "numbers-24": {
        "title": "Three powers",
        "condition": (
            "Ask for integer n. Print on three lines: n², n³ and n⁴ "
            "(use the ** operator)."
        ),
        "tests": [
            {"stdin": "2\n", "expected_output": "4\n8\n16"},
            {"stdin": "3\n", "expected_output": "9\n27\n81"},
        ],
    },
    "numbers-25": {
        "title": "Average of three",
        "condition": "Ask for three integers. Print their arithmetic mean.",
        "tests": [
            {"stdin": "10\n20\n30\n", "expected_output": "20.0"},
            {"stdin": "1\n2\n3\n", "expected_output": "2.0"},
        ],
    },
    "numbers-26": {
        "title": "Dollars and cents",
        "condition": (
            "Ask for total cents (integer). "
            "Print on two lines: full dollars (// 100) and remaining cents (% 100)."
        ),
        "tests": [
            {"stdin": "257\n", "expected_output": "2\n57"},
            {"stdin": "100\n", "expected_output": "1\n0"},
        ],
    },
    "numbers-27": {
        "title": "Table of powers of three",
        "condition": (
            "Build a mini table of powers of 3. "
            "Set n = 3 and print on three lines: 3¹, 3² and 3³."
        ),
        "tests": [{"expected_output": "3\n9\n27"}],
    },
    "numbers-28": {
        "title": "Difference of cubes",
        "condition": "Ask for a and b (integers). Print a³ − b³.",
        "tests": [
            {"stdin": "5\n2\n", "expected_output": "117"},
            {"stdin": "3\n3\n", "expected_output": "0"},
        ],
    },
    "numbers-29": {
        "title": "Absolute value",
        "condition": (
            "Ask for integer x. If x < 0, print −x, else print x "
            "(absolute value without the abs function)."
        ),
        "hint": "Use if…else inside print or separate branches.",
        "tests": [
            {"stdin": "-15\n", "expected_output": "15"},
            {"stdin": "8\n", "expected_output": "8"},
            {"stdin": "0\n", "expected_output": "0"},
        ],
    },
    "numbers-30": {
        "title": "Complex calculation",
        "condition": (
            "Ask for integer n. Print on three lines: "
            "1) 2×n + 1 "
            "2) n² − n "
            "3) n // 3"
        ),
        "tests": [
            {"stdin": "9\n", "expected_output": "19\n72\n3"},
            {"stdin": "10\n", "expected_output": "21\n90\n3"},
        ],
    },
    "numbers-31": {
        "title": "Taxi ride",
        "condition": (
            "Base fare is 50 dollars, each kilometer costs 15 dollars. "
            "Ask for distance in km (integer) and print the trip cost."
        ),
        "tests": [
            {"stdin": "3\n", "expected_output": "95"},
            {"stdin": "10\n", "expected_output": "200"},
        ],
    },
    "numbers-32": {
        "title": "Hours and minutes",
        "condition": (
            "Ask for total time in minutes (integer). "
            "Print on two lines: full hours (// 60) and remaining minutes (% 60)."
        ),
        "tests": [
            {"stdin": "125\n", "expected_output": "2\n5"},
            {"stdin": "60\n", "expected_output": "1\n0"},
        ],
    },
    "numbers-33": {
        "title": "Hundreds digit",
        "condition": (
            "In number 528 the hundreds digit is 5. "
            "Set n = 528 and using // and % print the hundreds digit."
        ),
        "hint": "First remove tens and ones with integer division by 100.",
        "tests": [{"expected_output": "5"}],
    },
    "numbers-34": {
        "title": "Store discount",
        "condition": (
            "Ask for item price and discount percent (integers). "
            "Print final price after discount: price × (100 − discount) / 100."
        ),
        "tests": [
            {"stdin": "200\n10\n", "expected_output": "180.0"},
            {"stdin": "500\n20\n", "expected_output": "400.0"},
        ],
    },
    "numbers-35": {
        "title": "Neighbors of a number",
        "condition": (
            "On a number line neighbors matter. Ask for integer n "
            "and print three numbers on separate lines: n − 1, n and n + 1."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "9\n10\n11"},
            {"stdin": "0\n", "expected_output": "-1\n0\n1"},
        ],
    },
}

NUMBERS_FIX: dict[str, dict] = {
    "numbers-fix-01": {
        "title": "Fix: multiplication",
        "condition": (
            "The program counts seats in a hall (8 rows of 12 seats), "
            "but addition is used instead of multiplication — the answer is too small. "
            + _FIX_INTRO
        ),
        "hint": "You need multiplication, not addition.",
        "tests": [{"expected_output": "96"}],
    },
    "numbers-fix-02": {
        "title": "Fix: plus ten",
        "condition": (
            "The entered number should have 10 added, "
            "but the program adds text to a number and gets a strange result. "
            + _FIX_INTRO
        ),
        "hint": "Convert input to an integer before adding.",
        "tests": [
            {"stdin": "5\n", "expected_output": "15"},
            {"stdin": "23\n", "expected_output": "33"},
        ],
    },
    "numbers-fix-03": {
        "title": "Fix: arithmetic mean",
        "condition": (
            "The average of two test scores is wrong — "
            "the sum is divided by the wrong count. " + _FIX_INTRO
        ),
        "hint": "The mean of two numbers is sum divided by 2.",
        "tests": [
            {"stdin": "5\n4\n", "expected_output": "4.5"},
            {"stdin": "3\n3\n", "expected_output": "3.0"},
        ],
    },
    "numbers-fix-04": {
        "title": "Fix: square of six",
        "condition": (
            "A square with side 6 should have area 36, "
            "but the program outputs 12 — the wrong operation was chosen. " + _FIX_INTRO
        ),
        "hint": "A square is a number raised to power 2.",
        "tests": [{"expected_output": "36"}],
    },
    "numbers-fix-05": {
        "title": "Fix: remainder of division",
        "condition": (
            "You need to know how many stickers remain when giving 5 each, "
            "but the program counts full «packs», not the remainder. " + _FIX_INTRO
        ),
        "hint": "You need remainder (%), not integer division (//).",
        "tests": [{"expected_output": "2"}],
    },
    "numbers-fix-06": {
        "title": "Fix: taxi",
        "condition": (
            "The taxi meter adds only one kilometer to the base fare, "
            "without multiplying the rate by distance. " + _FIX_INTRO
        ),
        "hint": "Payment for kilometers is 15 × number of km.",
        "tests": [
            {"stdin": "3\n", "expected_output": "95"},
            {"stdin": "10\n", "expected_output": "200"},
        ],
    },
    "numbers-fix-07": {
        "title": "Fix: hours and minutes",
        "condition": (
            "Converting minutes to hours gives a decimal number of hours "
            "while the remaining minutes are correct. " + _FIX_INTRO
        ),
        "hint": "Hours are the integer part when dividing by 60.",
        "tests": [
            {"stdin": "125\n", "expected_output": "2\n5"},
            {"stdin": "60\n", "expected_output": "1\n0"},
        ],
    },
    "numbers-fix-08": {
        "title": "Fix: hundreds digit",
        "condition": (
            "From number 528 you need digit 5 (hundreds), "
            "but the program prints a two-digit remainder. " + _FIX_INTRO
        ),
        "hint": "Hundreds are obtained by dividing by 100 without remainder.",
        "tests": [{"expected_output": "5"}],
    },
    "numbers-fix-09": {
        "title": "Fix: discount",
        "condition": (
            "The register subtracts discount as a fixed dollar amount, "
            "although discount is given in percent. " + _FIX_INTRO
        ),
        "hint": "A 10% discount on 200 is not 10 dollars.",
        "tests": [
            {"stdin": "200\n10\n", "expected_output": "180.0"},
            {"stdin": "500\n20\n", "expected_output": "400.0"},
        ],
    },
    "numbers-fix-10": {
        "title": "Fix: neighbors of a number",
        "condition": (
            "Three neighboring numbers on a line are printed in wrong order — "
            "n itself ended up on the last line. " + _FIX_INTRO
        ),
        "hint": "The second line should be n itself.",
        "tests": [
            {"stdin": "10\n", "expected_output": "9\n10\n11"},
            {"stdin": "0\n", "expected_output": "-1\n0\n1"},
        ],
    },
}

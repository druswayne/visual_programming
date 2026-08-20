"""English translations for while/for loop tasks."""

from __future__ import annotations

_FIX_INTRO = (
    "A program is already assembled in the workspace, but it behaves incorrectly when checked. "
    "Find the mistake in the blocks and fix it."
)

# ---------------------------------------------------------------------------
# While loop tasks (while-01 .. while-35)
# ---------------------------------------------------------------------------
WHILE: dict[str, dict] = {
    "while-01": {
        "title": "Count from one to five",
        "condition": (
            "A referee counts runners at a race. Start with number = 1 "
            "and in a while loop print the number and increase it by 1 "
            "until number is greater than 5. The screen should show 1 … 5."
        ),
        "tests": [{"expected_output": "1\n2\n3\n4\n5"}],
        "hint": "Loop condition: number ≤ 5. Inside the loop — print and add 1.",
    },
    "while-02": {
        "title": "Three times «Ready!»",
        "condition": (
            "Before a competition an athlete answers a command three times. "
            "Counter count = 0; while count < 3 — print Ready! and increase count."
        ),
        "tests": [{"expected_output": "Ready!\nReady!\nReady!"}],
    },
    "while-03": {
        "title": "Countdown",
        "condition": (
            "A rocket launches in 5 seconds. "
            "Variable t = 5: while t > 0, show t on the display and decrease by 1."
        ),
        "tests": [{"expected_output": "5\n4\n3\n2\n1"}],
    },
    "while-04": {
        "title": "Evens up to ten",
        "condition": (
            "Even seat numbers are marked on the track. "
            "Start with n = 2 and while n ≤ 10 print the number and add 2."
        ),
        "tests": [{"expected_output": "2\n4\n6\n8\n10"}],
    },
    "while-05": {
        "title": "Sum from 1 to 5",
        "condition": (
            "Add the numbers from 1 to 5 in a while loop. "
            "Save the result in sum and print 15."
        ),
        "tests": [{"expected_output": "15"}],
        "hint": "Create a counter and a sum. In the loop add the counter to the sum.",
    },
    "while-06": {
        "title": "Times table for ten",
        "condition": (
            "Variable i = 1. "
            "While i ≤ 4, print i × 10 and increase i."
        ),
        "tests": [{"expected_output": "10\n20\n30\n40"}],
    },
    "while-07": {
        "title": "Five stars",
        "condition": (
            "A hotel rating is five stars. "
            "Counter k = 0: while k < 5, print ★ and increase k."
        ),
        "tests": [{"expected_output": "★\n★\n★\n★\n★"}],
    },
    "while-08": {
        "title": "Count to entered number",
        "condition": (
            "Ask for an integer n (convert to int). "
            "Set i = 1 and in a while loop while i ≤ n print i, "
            "increasing i."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n2\n3\n4"},
            {"stdin": "6\n", "expected_output": "1\n2\n3\n4\n5\n6"},
        ],
    },
    "while-09": {
        "title": "Squares of numbers",
        "condition": (
            "Variable x = 1. "
            "While x ≤ 5, print x × x and increase x."
        ),
        "tests": [{"expected_output": "1\n4\n9\n16\n25"}],
    },
    "while-10": {
        "title": "Doubling",
        "condition": (
            "Variable number = 1. "
            "While number ≤ 32, print it and replace with number × 2."
        ),
        "tests": [{"expected_output": "1\n2\n4\n8\n16\n32"}],
    },
    "while-11": {
        "title": "Sum up to ten",
        "condition": (
            "Using a while loop find the sum of numbers from 1 to 10 "
            "and print 55."
        ),
        "tests": [{"expected_output": "55"}],
    },
    "while-12": {
        "title": "From ten down to six",
        "condition": (
            "Variable n = 10. "
            "While n ≥ 6, print n and decrease by 1."
        ),
        "tests": [{"expected_output": "10\n9\n8\n7\n6"}],
    },
    "while-13": {
        "title": "Step minus five",
        "condition": (
            "Variable remainder = 20. "
            "While remainder > 0, print remainder and subtract 5."
        ),
        "tests": [{"expected_output": "20\n15\n10\n5"}],
    },
    "while-14": {
        "title": "Sum from 1 to n",
        "condition": (
            "Ask for an integer n. "
            "In a while loop add all numbers from 1 to n and print the sum."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "15"},
            {"stdin": "4\n", "expected_output": "10"},
        ],
    },
    "while-15": {
        "title": "Sevens up to thirty-five",
        "condition": (
            "Variable m = 7. "
            "While m ≤ 35, print m and add 7."
        ),
        "tests": [{"expected_output": "7\n14\n21\n28\n35"}],
    },
    "while-16": {
        "title": "Three greetings",
        "condition": (
            "A robot greets three visitors in a row. "
            "Counter c = 0: while c < 3, say hello and increase c."
        ),
        "tests": [{"expected_output": "hello\nhello\nhello"}],
    },
    "while-17": {
        "title": "Powers of three",
        "condition": (
            "Variable value = 1. "
            "While value < 100, print it and multiply by 3."
        ),
        "tests": [{"expected_output": "1\n3\n9\n27\n81"}],
    },
    "while-18": {
        "title": "How many steps?",
        "condition": (
            "Ask for an integer — how many times to print the word step. "
            "Use a while loop with a counter."
        ),
        "tests": [
            {"stdin": "3\n", "expected_output": "step\nstep\nstep"},
            {"stdin": "2\n", "expected_output": "step\nstep"},
        ],
    },
    "while-19": {
        "title": "Countdown from n",
        "condition": (
            "Ask for an integer n. "
            "In a while loop while n > 0 print n and decrease by 1."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "5\n4\n3\n2\n1"},
            {"stdin": "3\n", "expected_output": "3\n2\n1"},
        ],
    },
    "while-20": {
        "title": "While marathon",
        "condition": (
            "Ask for an integer n. Print on three lines: "
            "1) the number n itself "
            "2) n × 2 "
            "3) the sum of numbers from 1 to n (in a while loop)"
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "4\n8\n10"},
            {"stdin": "5\n", "expected_output": "5\n10\n15"},
        ],
        "hint": "For the sum create a variable and accumulate it in the loop.",
    },
    "while-21": {
        "title": "How many digits",
        "condition": (
            "Set n = 48291. In a while loop, while n > 0, divide n by 10 "
            "and count how many times. Print the number of digits."
        ),
        "tests": [{"expected_output": "5"}],
    },
    "while-22": {
        "title": "Sum of digits",
        "condition": (
            "Set n = 123. In a while loop, while n > 0, take the remainder "
            "when dividing by 10, add it to the sum, and divide n by 10. "
            "Print the sum of digits."
        ),
        "tests": [{"expected_output": "6"}],
    },
    "while-23": {
        "title": "Multiplication table",
        "condition": (
            "Ask for n (integer). In a while loop with i from 1 to 10 print i × n."
        ),
        "tests": [
            {
                "stdin": "7\n",
                "expected_output": "7\n14\n21\n28\n35\n42\n49\n56\n63\n70",
            },
        ],
    },
    "while-24": {
        "title": "Power of two greater than n",
        "condition": (
            "Ask for n (integer). Find the smallest power of two "
            "greater than n: p = 1, while p <= n multiply p by 2. Print p."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "16"},
            {"stdin": "32\n", "expected_output": "64"},
        ],
    },
    "while-25": {
        "title": "Collatz sequence",
        "condition": (
            "Set n = 6. While n > 1: print n; if n is even — n = n // 2, "
            "else n = n * 3 + 1. Stop when n becomes 1."
        ),
        "tests": [{"expected_output": "6\n3\n10\n5\n16\n8\n4\n2"}],
        "hint": "We do not print 1 — the loop ends when n equals 1.",
    },
    "while-26": {
        "title": "Factorial via while",
        "condition": (
            "Ask for n (integer ≥ 0). Compute n! in a while loop and print."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "120"},
            {"stdin": "0\n", "expected_output": "1"},
        ],
    },
    "while-27": {
        "title": "Sum of squares",
        "condition": (
            "Ask for n. In a while loop find the sum of i² for i from 1 to n and print."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "30"},
            {"stdin": "3\n", "expected_output": "14"},
        ],
    },
    "while-28": {
        "title": "Strip trailing zeros",
        "condition": (
            "Set n = 5000. While n is divisible by 10 without remainder, divide n by 10. "
            "Print the resulting number."
        ),
        "tests": [{"expected_output": "5"}],
    },
    "while-29": {
        "title": "Smallest divisor",
        "condition": (
            "Ask for n (> 1). With d = 2 in a while loop find the smallest divisor: "
            "while n % d != 0 increase d. Print d."
        ),
        "tests": [
            {"stdin": "15\n", "expected_output": "3"},
            {"stdin": "7\n", "expected_output": "7"},
        ],
    },
    "while-30": {
        "title": "While combo",
        "condition": (
            "Ask for n. Print on two lines: "
            "1) n! (via while) "
            "2) the sum of digits of n (via while)"
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "120\n5"},
            {"stdin": "12\n", "expected_output": "479001600\n3"},
        ],
    },
    "while-31": {
        "title": "Reverse number",
        "condition": (
            "Ask for an integer. Reversing digits means building a new number "
            "right to left. Do this in a while loop and print the result "
            "(for example 12345 → 54321)."
        ),
        "tests": [
            {"stdin": "12345\n", "expected_output": "54321"},
            {"stdin": "120\n", "expected_output": "21"},
        ],
        "hint": "At each step: rev = rev * 10 + n % 10, then n = n // 10.",
    },
    "while-32": {
        "title": "Sum until zero",
        "condition": (
            "Game: the player enters numbers until they enter 0. "
            "Add all entered numbers before zero (zero itself does not count) and print the sum."
        ),
        "tests": [
            {"stdin": "3\n5\n2\n0\n", "expected_output": "10"},
            {"stdin": "7\n0\n", "expected_output": "7"},
        ],
    },
    "while-33": {
        "title": "Greatest common divisor",
        "condition": (
            "Ask for two integers. Find their GCD using Euclid's algorithm in a while loop "
            "(while the second is not 0, replace the pair with (second, remainder of division)) "
            "and print the answer."
        ),
        "tests": [
            {"stdin": "48\n18\n", "expected_output": "6"},
            {"stdin": "17\n13\n", "expected_output": "1"},
        ],
    },
    "while-34": {
        "title": "Power in a loop",
        "condition": (
            "Ask for a base and an exponent (integers ≥ 0). "
            "Compute the power by multiplication in a while loop and print the result."
        ),
        "tests": [
            {"stdin": "2\n10\n", "expected_output": "1024"},
            {"stdin": "5\n3\n", "expected_output": "125"},
            {"stdin": "9\n0\n", "expected_output": "1"},
        ],
    },
    "while-35": {
        "title": "How many divisors",
        "condition": (
            "Ask for an integer n > 0. In a while loop check divisors from 1 to n "
            "and print how many of them divide n without remainder."
        ),
        "tests": [
            {"stdin": "12\n", "expected_output": "6"},
            {"stdin": "7\n", "expected_output": "2"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
    },
    "while-36": {
        "title": "Digit sum of a number",
        "condition": (
            "Ask for an integer n > 0. In a while loop add up all its digits and print the sum."
        ),
        "tests": [
            {"stdin": "48291\n", "expected_output": "24"},
            {"stdin": "100\n", "expected_output": "1"},
            {"stdin": "9\n", "expected_output": "9"},
        ],
        "hint": "On each step take n % 10 and divide n by 10 using integer division.",
    },
    "while-37": {
        "title": "Powers of two up to n",
        "condition": (
            "Ask for an integer n ≥ 1. Starting from 1, print powers of two "
            "(1, 2, 4, 8, …) while the next number is not greater than n. Each on a new line."
        ),
        "tests": [
            {"stdin": "20\n", "expected_output": "1\n2\n4\n8\n16"},
            {"stdin": "1\n", "expected_output": "1"},
            {"stdin": "8\n", "expected_output": "1\n2\n4\n8"},
        ],
    },
    "while-38": {
        "title": "Prime or composite",
        "condition": (
            "Ask for an integer n > 0. In a while loop count the number of divisors. "
            "If there are exactly 2 divisors — print prime, otherwise — composite."
        ),
        "tests": [
            {"stdin": "7\n", "expected_output": "prime"},
            {"stdin": "12\n", "expected_output": "composite"},
            {"stdin": "1\n", "expected_output": "composite"},
        ],
        "hint": "A prime number has only 1 and itself as divisors.",
    },
    "while-39": {
        "title": "Collatz steps",
        "condition": (
            "Ask for an integer n > 0. While n is not 1: if n is even — divide it by 2, "
            "otherwise replace it with 3×n + 1. Count how many steps it took and print that number. "
            "The value 1 itself is not a step."
        ),
        "tests": [
            {"stdin": "6\n", "expected_output": "8"},
            {"stdin": "1\n", "expected_output": "0"},
            {"stdin": "3\n", "expected_output": "7"},
        ],
        "hint": "Increase the counter after each change of n.",
    },
    "while-40": {
        "title": "Even digits",
        "condition": (
            "Ask for an integer n > 0. In a while loop count how many of its digits are even "
            "and print that count. The digit 0 counts as even."
        ),
        "tests": [
            {"stdin": "246\n", "expected_output": "3"},
            {"stdin": "135\n", "expected_output": "0"},
            {"stdin": "1024\n", "expected_output": "3"},
        ],
    },
    "while-41": {
        "title": "Palindrome number",
        "condition": (
            "Ask for an integer n > 0. Reverse its digits in a while loop. "
            "If you get the same number — print yes, otherwise — no."
        ),
        "tests": [
            {"stdin": "121\n", "expected_output": "yes"},
            {"stdin": "123\n", "expected_output": "no"},
            {"stdin": "10\n", "expected_output": "no"},
        ],
        "hint": "Keep the original value and compare the reversed number with it.",
    },
    "while-42": {
        "title": "Odd digits",
        "condition": (
            "Ask for an integer n > 0. Count how many of its digits are odd and print that number."
        ),
        "tests": [
            {"stdin": "135\n", "expected_output": "3"},
            {"stdin": "246\n", "expected_output": "0"},
            {"stdin": "1024\n", "expected_output": "1"},
        ],
    },
    "while-43": {
        "title": "Least common multiple",
        "condition": (
            "Ask for two integers a and b > 0. Find the GCD with the Euclidean algorithm, "
            "then print the LCM = a × b / GCD."
        ),
        "tests": [
            {"stdin": "12\n18\n", "expected_output": "36"},
            {"stdin": "7\n5\n", "expected_output": "35"},
            {"stdin": "6\n9\n", "expected_output": "18"},
        ],
        "hint": "It is convenient to compute LCM via GCD so you do not iterate over large numbers.",
    },
    "while-44": {
        "title": "Digital root",
        "condition": (
            "Ask for an integer n > 0. While the number is greater than 9, replace it with the sum of its digits. "
            "Print the resulting single digit."
        ),
        "tests": [
            {"stdin": "38\n", "expected_output": "2"},
            {"stdin": "999\n", "expected_output": "9"},
            {"stdin": "10\n", "expected_output": "1"},
        ],
        "hint": "Inside the outer while loop, sum the digits again with an inner loop.",
    },
    "while-45": {
        "title": "Maximum digit",
        "condition": "Ask for an integer n > 0 and print its largest digit.",
        "tests": [
            {"stdin": "582\n", "expected_output": "8"},
            {"stdin": "100\n", "expected_output": "1"},
            {"stdin": "7\n", "expected_output": "7"},
        ],
    },
    "while-46": {
        "title": "Power of two?",
        "condition": (
            "Ask for an integer n > 0. If n is a power of two (1, 2, 4, 8, …) — yes, otherwise — no. "
            "Divide n by 2 while it is even, then check whether 1 remains."
        ),
        "tests": [
            {"stdin": "8\n", "expected_output": "yes"},
            {"stdin": "12\n", "expected_output": "no"},
            {"stdin": "1\n", "expected_output": "yes"},
        ],
    },
    "while-47": {
        "title": "Fibonacci up to n",
        "condition": (
            "Ask for an integer n ≥ 1. Print Fibonacci numbers not greater than n, "
            "starting from 1, 1 — each on a new line."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "1\n1\n2\n3\n5\n8"},
            {"stdin": "1\n", "expected_output": "1\n1"},
            {"stdin": "2\n", "expected_output": "1\n1\n2"},
        ],
    },
    "while-48": {
        "title": "How many times divisible by two",
        "condition": (
            "Ask for an integer n > 0. While n is even, divide it by 2 and count the steps. "
            "Print the number of divisions."
        ),
        "tests": [
            {"stdin": "80\n", "expected_output": "4"},
            {"stdin": "7\n", "expected_output": "0"},
            {"stdin": "16\n", "expected_output": "4"},
        ],
    },
    "while-49": {
        "title": "Product of digits",
        "condition": "Ask for an integer n > 0 and print the product of its digits.",
        "tests": [
            {"stdin": "23\n", "expected_output": "6"},
            {"stdin": "105\n", "expected_output": "0"},
            {"stdin": "22\n", "expected_output": "4"},
        ],
        "hint": "Start the product at 1. A zero among the digits will make the answer zero.",
    },
    "while-50": {
        "title": "Sum until greater than n",
        "condition": (
            "Ask for an integer n ≥ 1. Add 1 + 2 + 3 + … in a while loop "
            "until the sum becomes greater than n. Print how many terms were added "
            "by that moment (the last term after which the sum exceeded n also counts)."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "5"},
            {"stdin": "1\n", "expected_output": "2"},
            {"stdin": "6\n", "expected_output": "4"},
        ],
        "hint": "For n = 10: 1+2+3+4=10 is not yet greater, +5 gives 15 — 5 terms.",
    },
}

# ---------------------------------------------------------------------------
# While fix tasks (while-fix-01 .. while-fix-10)
# ---------------------------------------------------------------------------
WHILE_FIX: dict[str, dict] = {
    "while-fix-01": {
        "title": "Fix: numbers from 1 to 5",
        "condition": (
            "The race count stops at 4 — "
            "the loop ends one step too early. " + _FIX_INTRO
        ),
        "hint": "Check the loop continuation condition.",
        "tests": [{"expected_output": "1\n2\n3\n4\n5"}],
    },
    "while-fix-02": {
        "title": "Fix: countdown",
        "condition": (
            "The rocket countdown goes on forever — "
            "the counter grows instead of decreasing. " + _FIX_INTRO
        ),
        "hint": "In a countdown the variable should decrease.",
        "tests": [{"expected_output": "5\n4\n3\n2\n1"}],
    },
    "while-fix-03": {
        "title": "Fix: sum from 1 to 5",
        "condition": (
            "The sum of numbers from 1 to 5 is 9 instead of 15 — "
            "the counter in the loop skips numbers. " + _FIX_INTRO
        ),
        "hint": "On each step the counter should increase by 1.",
        "tests": [{"expected_output": "15"}],
    },
    "while-fix-04": {
        "title": "Fix: evens up to 10",
        "condition": (
            "The row of even numbers starts at 1 instead of 2 — "
            "the starting value of the counter is wrong. " + _FIX_INTRO
        ),
        "hint": "The first even number in the range is 2.",
        "tests": [{"expected_output": "2\n4\n6\n8\n10"}],
    },
    "while-fix-05": {
        "title": "Fix: n times «step»",
        "condition": (
            "For n = 3 the word «step» is printed 4 times — "
            "the loop makes one extra pass. " + _FIX_INTRO
        ),
        "hint": "You need exactly n repetitions, not n + 1.",
        "tests": [
            {"stdin": "3\n", "expected_output": "step\nstep\nstep"},
            {"stdin": "2\n", "expected_output": "step\nstep"},
        ],
    },
    "while-fix-06": {
        "title": "Fix: reverse number",
        "condition": (
            "The digits of the number are printed separately in reverse order, "
            "but are not combined into one final number. " + _FIX_INTRO
        ),
        "hint": "Accumulate the reversal in a variable instead of printing digits.",
        "tests": [
            {"stdin": "12345\n", "expected_output": "54321"},
            {"stdin": "120\n", "expected_output": "21"},
        ],
    },
    "while-fix-07": {
        "title": "Fix: sum until zero",
        "condition": (
            "For input 3, 5, 2, 0 the sum is 7 instead of 10 — "
            "the first entered number is not counted. " + _FIX_INTRO
        ),
        "hint": "Add each non-zero number to the sum before reading the next one.",
        "tests": [
            {"stdin": "3\n5\n2\n0\n", "expected_output": "10"},
            {"stdin": "7\n0\n", "expected_output": "7"},
        ],
    },
    "while-fix-08": {
        "title": "Fix: GCD",
        "condition": (
            "Euclid's algorithm for 48 and 18 gives the wrong answer — "
            "the dividend is updated incorrectly in the loop. " + _FIX_INTRO
        ),
        "hint": "New a is the old b, new b is the remainder of division.",
        "tests": [
            {"stdin": "48\n18\n", "expected_output": "6"},
            {"stdin": "17\n13\n", "expected_output": "1"},
        ],
    },
    "while-fix-09": {
        "title": "Fix: power in a loop",
        "condition": (
            "2¹⁰ becomes 2048 instead of 1024 — "
            "the loop multiplies one time too many. " + _FIX_INTRO
        ),
        "hint": "For exponent 3 you need exactly 3 multiplications, not 4.",
        "tests": [
            {"stdin": "2\n10\n", "expected_output": "1024"},
            {"stdin": "5\n3\n", "expected_output": "125"},
            {"stdin": "9\n0\n", "expected_output": "1"},
        ],
    },
    "while-fix-10": {
        "title": "Fix: divisors",
        "condition": (
            "For the number 12 the program reports 12 divisors — "
            "the counter increases for every number, not only for divisors. "
            + _FIX_INTRO
        ),
        "hint": "Increase the counter only when n is divisible by d.",
        "tests": [
            {"stdin": "12\n", "expected_output": "6"},
            {"stdin": "7\n", "expected_output": "2"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
    },
}

# ---------------------------------------------------------------------------
# For loop tasks (for-01 .. for-35)
# ---------------------------------------------------------------------------
FOR: dict[str, dict] = {
    "for-01": {
        "title": "Numbers from 1 to 5",
        "condition": (
            "Seat numbering in a row: using a for loop and range(1, 6, 1) "
            "print the numbers 1, 2, 3, 4, 5."
        ),
        "tests": [{"expected_output": "1\n2\n3\n4\n5"}],
        "hint": "The second number in range is not included — for five numbers use 6.",
    },
    "for-02": {
        "title": "Four times Python",
        "condition": (
            "At a conference there are four talks about Python — "
            "print the language name four times in a for loop with range(0, 4, 1)."
        ),
        "tests": [{"expected_output": "Python\nPython\nPython\nPython"}],
    },
    "for-03": {
        "title": "Evens from zero",
        "condition": (
            "Even centimeters from 0 to 8 are marked on a measuring tape. "
            "Iterate range(0, 10, 2) in a for loop and print each mark."
        ),
        "tests": [{"expected_output": "0\n2\n4\n6\n8"}],
    },
    "for-04": {
        "title": "From ten down to one",
        "condition": (
            "Countdown at the finish: use range(10, 0, -1) "
            "and print numbers from 10 to 1."
        ),
        "tests": [{"expected_output": "10\n9\n8\n7\n6\n5\n4\n3\n2\n1"}],
    },
    "for-05": {
        "title": "Sum from 1 to 10",
        "condition": (
            "Iterate range(1, 11, 1), accumulate the sum in a variable and print 55."
        ),
        "tests": [{"expected_output": "55"}],
    },
    "for-06": {
        "title": "Squares from 1 to 5",
        "condition": (
            "In a for loop for i in range(1, 6, 1) print i × i for each i."
        ),
        "tests": [{"expected_output": "1\n4\n9\n16\n25"}],
    },
    "for-07": {
        "title": "Count to n",
        "condition": (
            "Ask for an integer n. "
            "In a for loop with range from 1 to n + 1 print each number."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n2\n3\n4"},
            {"stdin": "6\n", "expected_output": "1\n2\n3\n4\n5\n6"},
        ],
        "hint": "For range up to n inclusive the upper bound is n + 1.",
    },
    "for-08": {
        "title": "From fifth to fifteenth",
        "condition": (
            "Iterate range(5, 16, 1) and print all numbers."
        ),
        "tests": [{"expected_output": "5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15"}],
    },
    "for-09": {
        "title": "Triple the numbers",
        "condition": (
            "In a for loop for x in range(3, 8, 1) print x × 3."
        ),
        "tests": [{"expected_output": "9\n12\n15\n18\n21"}],
    },
    "for-10": {
        "title": "Step three",
        "condition": (
            "Iterate range(1, 10, 3) and print the numbers."
        ),
        "tests": [{"expected_output": "1\n4\n7"}],
    },
    "for-11": {
        "title": "Product 1×2×3×4×5",
        "condition": (
            "In a for loop multiply numbers from 1 to 5 "
            "and print the result 120."
        ),
        "tests": [{"expected_output": "120"}],
        "hint": "Create variable product = 1 and multiply in the loop.",
    },
    "for-12": {
        "title": "Zero and onward",
        "condition": (
            "Ask for an integer n. "
            "Print numbers range(0, n, 1) — from 0 to n − 1."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "0\n1\n2\n3\n4"},
            {"stdin": "3\n", "expected_output": "0\n1\n2"},
        ],
    },
    "for-13": {
        "title": "Decrease by two",
        "condition": (
            "Iterate range(20, 10, -2) and print each number."
        ),
        "tests": [{"expected_output": "20\n18\n16\n14\n12"}],
    },
    "for-14": {
        "title": "From a to b",
        "condition": (
            "Ask for two integers: start and end. "
            "Print all numbers from start to end − 1 "
            "using range(start, end, 1)."
        ),
        "tests": [
            {"stdin": "3\n7\n", "expected_output": "3\n4\n5\n6"},
            {"stdin": "10\n13\n", "expected_output": "10\n11\n12"},
        ],
    },
    "for-15": {
        "title": "Sum of evens",
        "condition": (
            "Add the even numbers 2, 4, 6, 8, 10 in a for loop with range(2, 11, 2) "
            "and print 30."
        ),
        "tests": [{"expected_output": "30"}],
    },
    "for-16": {
        "title": "Plus ten",
        "condition": (
            "In a for loop for i in range(1, 6, 1) print i + 10."
        ),
        "tests": [{"expected_output": "11\n12\n13\n14\n15"}],
    },
    "for-17": {
        "title": "Fives up to n",
        "condition": (
            "Ask for an integer n. "
            "In a for loop for i in range(1, n + 1, 1) print i × 5."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "5\n10\n15\n20"},
            {"stdin": "3\n", "expected_output": "5\n10\n15"},
        ],
    },
    "for-18": {
        "title": "Hundred with step 25",
        "condition": (
            "Iterate range(100, 0, -25) and print the numbers."
        ),
        "tests": [{"expected_output": "100\n75\n50\n25"}],
    },
    "for-19": {
        "title": "Stars by count",
        "condition": (
            "A viewer rates a performance: ask how many «stars» to give, "
            "and print the word star that many times in a for loop."
        ),
        "tests": [
            {"stdin": "3\n", "expected_output": "star\nstar\nstar"},
            {"stdin": "2\n", "expected_output": "star\nstar"},
        ],
    },
    "for-20": {
        "title": "For marathon",
        "condition": (
            "Ask for an integer n. Print on three lines: "
            "1) the sum of numbers from 1 to n (for loop) "
            "2) the product of numbers from 1 to n "
            "3) the number n itself"
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "10\n24\n4"},
            {"stdin": "5\n", "expected_output": "15\n120\n5"},
        ],
        "hint": "For the product start at 1, for the sum — at 0.",
    },
    "for-21": {
        "title": "Table of 7",
        "condition": (
            "Iterate i from 1 to 10 in a for loop and print i × 7."
        ),
        "tests": [{"expected_output": "7\n14\n21\n28\n35\n42\n49\n56\n63\n70"}],
    },
    "for-22": {
        "title": "Sum of squares",
        "condition": (
            "Ask for n. In a for loop find the sum of squares from 1 to n and print."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "30"},
            {"stdin": "5\n", "expected_output": "55"},
        ],
    },
    "for-23": {
        "title": "How many evens",
        "condition": (
            "Ask for a and b (a ≤ b). Count in a for loop "
            "how many even numbers are in the range from a to b inclusive."
        ),
        "tests": [
            {"stdin": "1\n10\n", "expected_output": "5"},
            {"stdin": "2\n9\n", "expected_output": "4"},
        ],
    },
    "for-24": {
        "title": "Product of odds",
        "condition": (
            "In a for loop find the product of odd numbers from 1 to 7 and print."
        ),
        "tests": [{"expected_output": "105"}],
    },
    "for-25": {
        "title": "Star ladder",
        "condition": (
            "In a for loop with i from 1 to 4 print i asterisks on each line."
        ),
        "tests": [{"expected_output": "*\n**\n***\n****"}],
        "hint": "Line 1 — one *, line 2 — two * and so on.",
    },
    "for-26": {
        "title": "Sum of evens up to n",
        "condition": (
            "Ask for n. In a for loop add all even numbers from 2 to n "
            "(if n is odd — up to n − 1)."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "30"},
            {"stdin": "7\n", "expected_output": "12"},
        ],
    },
    "for-27": {
        "title": "Fibonacci numbers",
        "condition": (
            "Ask for n (≥ 2). Print the first n Fibonacci numbers "
            "each on a new line, starting with 1 and 1."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "1\n1\n2\n3\n5"},
            {"stdin": "7\n", "expected_output": "1\n1\n2\n3\n5\n8\n13"},
        ],
    },
    "for-28": {
        "title": "Maximum in range",
        "condition": (
            "Ask for a and b (a ≤ b). Find the maximum number "
            "in the range from a to b via a for loop."
        ),
        "tests": [
            {"stdin": "3\n9\n", "expected_output": "9"},
            {"stdin": "-2\n5\n", "expected_output": "5"},
        ],
    },
    "for-29": {
        "title": "Countdown for",
        "condition": (
            "Ask for n. In a for loop print n, n−1, …, 1 (each on a new line)."
        ),
        "tests": [{"stdin": "5\n", "expected_output": "5\n4\n3\n2\n1"}],
    },
    "for-30": {
        "title": "Final for",
        "condition": (
            "Ask for n. On three lines print: "
            "the sum 1..n, the sum of squares 1..n, and how many numbers from 1 to n "
            "are divisible by 3."
        ),
        "tests": [{"stdin": "6\n", "expected_output": "21\n91\n2"}],
    },
    "for-31": {
        "title": "First n odds",
        "condition": (
            "Ask for n. Print the first n odd numbers, starting from 1 "
            "(each on a new line)."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n3\n5\n7"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
        "hint": "Hint: range(1, 2 * n, 2).",
    },
    "for-32": {
        "title": "Multiples of k",
        "condition": (
            "Ask for n and k (integers). Print all numbers from k to n inclusive "
            "that are divisible by k."
        ),
        "tests": [
            {"stdin": "20\n3\n", "expected_output": "3\n6\n9\n12\n15\n18"},
            {"stdin": "10\n5\n", "expected_output": "5\n10"},
        ],
    },
    "for-33": {
        "title": "Sum of evens in segment",
        "condition": (
            "Ask for bounds a and b (a ≤ b). "
            "In a for loop add all even numbers from a to b inclusive and print the sum."
        ),
        "tests": [
            {"stdin": "1\n10\n", "expected_output": "30"},
            {"stdin": "4\n4\n", "expected_output": "4"},
        ],
    },
    "for-34": {
        "title": "How many letters in a word",
        "condition": (
            "Ask for a letter, then a word. Count in a for loop "
            "how many times that letter appears in the word, and print the number."
        ),
        "tests": [
            {"stdin": "a\nbanana\n", "expected_output": "2"},
            {"stdin": "o\ncat\n", "expected_output": "1"},
        ],
    },
    "for-35": {
        "title": "Numbers divisible by six",
        "condition": (
            "Ask for n. Print all numbers from 1 to n inclusive "
            "that are divisible by both 2 and 3 (each on a new line)."
        ),
        "tests": [
            {"stdin": "30\n", "expected_output": "6\n12\n18\n24\n30"},
            {"stdin": "12\n", "expected_output": "6\n12"},
        ],
    },
    "for-36": {
        "title": "Factorial with for",
        "condition": (
            "Ask for an integer n ≥ 0. Compute n! in a for loop and print the result. "
            "Treat 0! as 1."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "120"},
            {"stdin": "0\n", "expected_output": "1"},
            {"stdin": "6\n", "expected_output": "720"},
        ],
        "hint": "Start the product at 1 and multiply by each number from 1 to n.",
    },
    "for-37": {
        "title": "Sum of multiples of 3 or 5",
        "condition": (
            "Ask for an integer n. In a for loop add all numbers from 1 to n inclusive "
            "that divide by 3 or by 5, and print the sum."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "33"},
            {"stdin": "9\n", "expected_output": "23"},
            {"stdin": "2\n", "expected_output": "0"},
        ],
        "hint": "Number 15 divides by both 3 and 5 — still add it only once.",
    },
    "for-38": {
        "title": "Prime with for",
        "condition": (
            "Ask for an integer n > 0. In a for loop count the divisors from 1 to n. "
            "If there are exactly 2 divisors — print prime, otherwise — composite."
        ),
        "tests": [
            {"stdin": "7\n", "expected_output": "prime"},
            {"stdin": "9\n", "expected_output": "composite"},
            {"stdin": "2\n", "expected_output": "prime"},
        ],
    },
    "for-39": {
        "title": "Number ladder",
        "condition": (
            "Ask for an integer n ≥ 1. On line i (i from 1 to n) print the numbers "
            "from 1 to i joined with no spaces. For example, for n = 4: 1, then 12, then 123, then 1234."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n12\n123\n1234"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
        "hint": "Accumulate a string: on each step glue the next digit and print the current result.",
    },
    "for-40": {
        "title": "Alternating sum",
        "condition": (
            "Ask for an integer n ≥ 1. Compute 1 − 2 + 3 − 4 + … ± n in a for loop and print the result. "
            "Add odd terms and subtract even terms."
        ),
        "tests": [
            {"stdin": "5\n", "expected_output": "3"},
            {"stdin": "4\n", "expected_output": "-2"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
    },
    "for-41": {
        "title": "Perfect number",
        "condition": (
            "Ask for an integer n > 1. If the sum of all divisors of n except n itself equals n — "
            "print perfect, otherwise — no. Examples: 6 = 1+2+3, 28 = 1+2+4+7+14."
        ),
        "tests": [
            {"stdin": "6\n", "expected_output": "perfect"},
            {"stdin": "28\n", "expected_output": "perfect"},
            {"stdin": "12\n", "expected_output": "no"},
        ],
        "hint": "In a for loop add the divisors from 1 to n − 1.",
    },
    "for-42": {
        "title": "Primes up to n",
        "condition": (
            "Ask for an integer n ≥ 2. Print all prime numbers from 2 to n inclusive, "
            "each on a new line. A prime number has exactly two divisors."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "2\n3\n5\n7"},
            {"stdin": "5\n", "expected_output": "2\n3\n5"},
        ],
        "hint": "For each x from 2 to n count the divisors with an inner loop.",
    },
    "for-43": {
        "title": "Rectangle of stars",
        "condition": (
            "Ask for the number of rows n and the number of columns m. Print a rectangle of * characters "
            "(n rows, each with exactly m asterisks and no spaces)."
        ),
        "tests": [
            {"stdin": "2\n3\n", "expected_output": "***\n***"},
            {"stdin": "3\n1\n", "expected_output": "*\n*\n*"},
        ],
        "hint": "A row of m stars can be built with '*' * m or with a loop.",
    },
    "for-44": {
        "title": "GCD by brute force",
        "condition": (
            "Ask for two integers a and b > 0. Find the GCD: iterate d from 1 up to the smaller of them "
            "and print the last d that divides both numbers."
        ),
        "tests": [
            {"stdin": "24\n18\n", "expected_output": "6"},
            {"stdin": "7\n3\n", "expected_output": "1"},
            {"stdin": "10\n10\n", "expected_output": "10"},
        ],
    },
    "for-45": {
        "title": "How many perfect squares",
        "condition": (
            "Ask for an integer n ≥ 1. How many positive perfect squares are not greater than n? "
            "Print that count (for 10 these are 1, 4 and 9 — the answer is 3)."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "3"},
            {"stdin": "1\n", "expected_output": "1"},
            {"stdin": "16\n", "expected_output": "4"},
        ],
        "hint": "Iterate i while i × i ≤ n and count such i.",
    },
    "for-46": {
        "title": "Multiples of 4 but not 6",
        "condition": (
            "Ask for an integer n. Print all numbers from 1 to n inclusive "
            "that are divisible by 4 and not divisible by 6 — each on a new line."
        ),
        "tests": [
            {"stdin": "20\n", "expected_output": "4\n8\n16\n20"},
            {"stdin": "8\n", "expected_output": "4\n8"},
        ],
    },
    "for-47": {
        "title": "Factorial table",
        "condition": (
            "Ask for an integer n ≥ 1. Print n lines: 1!, 2!, …, n! — one number per line."
        ),
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n2\n6\n24"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
        "hint": "You can accumulate a product in a variable and print it on each step.",
    },
    "for-48": {
        "title": "Nested series sum",
        "condition": (
            "Ask for an integer n ≥ 1. Compute the sum: for each i from 1 to n add the sum of numbers from 1 to i. "
            "That is (1) + (1+2) + (1+2+3) + … and print the result."
        ),
        "tests": [
            {"stdin": "3\n", "expected_output": "10"},
            {"stdin": "1\n", "expected_output": "1"},
            {"stdin": "4\n", "expected_output": "20"},
        ],
        "hint": "You need an outer loop over i and an inner loop over j from 1 to i.",
    },
    "for-49": {
        "title": "Count of primes",
        "condition": (
            "Ask for an integer n ≥ 1. Print how many prime numbers there are from 2 to n inclusive. "
            "If n < 2, the answer is 0."
        ),
        "tests": [
            {"stdin": "10\n", "expected_output": "4"},
            {"stdin": "1\n", "expected_output": "0"},
            {"stdin": "2\n", "expected_output": "1"},
        ],
    },
    "for-50": {
        "title": "Number pyramid",
        "condition": (
            "Ask for an integer n ≥ 1. On row i (from top to bottom, i from n down to 1) print i asterisks. "
            "For n = 3 you get 3 rows: ***, then **, then *."
        ),
        "tests": [
            {"stdin": "3\n", "expected_output": "***\n**\n*"},
            {"stdin": "1\n", "expected_output": "*"},
        ],
    },
}

# ---------------------------------------------------------------------------
# For fix tasks (for-fix-01 .. for-fix-10)
# ---------------------------------------------------------------------------
FOR_FIX: dict[str, dict] = {
    "for-fix-01": {
        "title": "Fix: from 1 to 5",
        "condition": (
            "The for loop prints only 1, 2, 3, 4 — "
            "the upper bound of range is set without including the last number. "
            + _FIX_INTRO
        ),
        "hint": "In range the end of the interval is not included.",
        "tests": [{"expected_output": "1\n2\n3\n4\n5"}],
    },
    "for-fix-02": {
        "title": "Fix: four times Python",
        "condition": (
            "The word Python should appear four times, "
            "but the loop prints it only three. " + _FIX_INTRO
        ),
        "hint": "Count how many values range(0, 3) produces.",
        "tests": [{"expected_output": "Python\nPython\nPython\nPython"}],
    },
    "for-fix-03": {
        "title": "Fix: sum from 1 to 10",
        "condition": (
            "Instead of the sum 1+…+10 the program multiplies the numbers "
            "and produces a huge result. " + _FIX_INTRO
        ),
        "hint": "For a sum use addition, not multiplication.",
        "tests": [{"expected_output": "55"}],
    },
    "for-fix-04": {
        "title": "Fix: squares from 1 to 5",
        "condition": (
            "Squares 1, 4, 9… should be printed, "
            "but the numbers 1, 2, 3… are shown instead. " + _FIX_INTRO
        ),
        "hint": "You need to print i * i.",
        "tests": [{"expected_output": "1\n4\n9\n16\n25"}],
    },
    "for-fix-05": {
        "title": "Fix: from 1 to n",
        "condition": (
            "For n = 5 the last number 5 is not printed — "
            "the upper bound of range does not include n. " + _FIX_INTRO
        ),
        "hint": "To include n, increase the second argument of range by 1.",
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n2\n3\n4"},
            {"stdin": "6\n", "expected_output": "1\n2\n3\n4\n5\n6"},
        ],
    },
    "for-fix-06": {
        "title": "Fix: odd numbers",
        "condition": (
            "The first odd numbers are replaced by evens: 2, 4, 6… "
            "instead of 1, 3, 5…. " + _FIX_INTRO
        ),
        "hint": "The first odd number is 1, step is 2.",
        "tests": [
            {"stdin": "4\n", "expected_output": "1\n3\n5\n7"},
            {"stdin": "1\n", "expected_output": "1"},
        ],
    },
    "for-fix-07": {
        "title": "Fix: multiples of k",
        "condition": (
            "The list of multiples starts at zero, "
            "although 0 is not in the required range. " + _FIX_INTRO
        ),
        "hint": "The first multiple of k is k itself.",
        "tests": [
            {"stdin": "20\n3\n", "expected_output": "3\n6\n9\n12\n15\n18"},
            {"stdin": "10\n5\n", "expected_output": "5\n10"},
        ],
    },
    "for-fix-08": {
        "title": "Fix: sum of evens",
        "condition": (
            "The sum of «evens» in the segment equals the sum of all numbers — "
            "odd numbers are included too. " + _FIX_INTRO
        ),
        "hint": "Add to the sum only even i.",
        "tests": [
            {"stdin": "1\n10\n", "expected_output": "30"},
            {"stdin": "4\n4\n", "expected_output": "4"},
        ],
    },
    "for-fix-09": {
        "title": "Fix: letter count",
        "condition": (
            "Counting the letter «a» in the word «banana» gives 1 — "
            "each character is compared to the whole string. " + _FIX_INTRO
        ),
        "hint": "Compare each character with the sought letter ch.",
        "tests": [
            {"stdin": "a\nbanana\n", "expected_output": "2"},
            {"stdin": "o\ncat\n", "expected_output": "1"},
        ],
    },
    "for-fix-10": {
        "title": "Fix: numbers divisible by six",
        "condition": (
            "Instead of numbers divisible by 6, all even numbers are printed — "
            "the check for divisibility by 3 is missing. " + _FIX_INTRO
        ),
        "hint": "A number divisible by 6 is divisible by both 2 and 3.",
        "tests": [
            {"stdin": "30\n", "expected_output": "6\n12\n18\n24\n30"},
            {"stdin": "12\n", "expected_output": "6\n12"},
        ],
    },
}

"""English translations for PyBlocks tasks."""

from __future__ import annotations

TASKS_EN: dict[str, dict] = {
    "cond-01": {
        'title': 'Greater than ten?',
        'condition': (
            'A thermometer reads 15 degrees — store it in variable number. If the value is greater than 10, print yes, otherwise — no. Use an if block and a comparison.'
        ),
        'hint': (
            'In the condition, use variable «number» and 10 with the «greater than» block.'
        ),
        'tests': [{'expected_output': 'yes'}],
    },
    "cond-02": {
        'title': 'Below zero',
        'condition': (
            'On a winter morning it is −4 °C outside — save this in variable temperature. If the temperature is below zero, print frost, otherwise — no frost.'
        ),
        'tests': [{'expected_output': 'frost'}],
    },
    "cond-03": {
        'title': 'Same numbers',
        'condition': (
            'Two players scored the same number of points: a = 8 and b = 8. Compare the scores and print equal or different.'
        ),
        'tests': [{'expected_output': 'equal'}],
    },
    "cond-04": {
        'title': 'Even or odd',
        'condition': (
            'There are 14 candies in a box — store this in n. Can they be split evenly between two people? If n divides by 2 with no remainder, print even, otherwise — odd.'
        ),
        'hint': 'First find the remainder of 14 divided by 2, then compare it to zero.',
        'tests': [{'expected_output': 'even'}],
    },
    "cond-05": {
        'title': 'Block «true»',
        'condition': (
            'Check how the logical constant works: put the true block in the if condition. When the condition is true — print true, otherwise — false.'
        ),
        'tests': [{'expected_output': 'true'}],
    },
    "cond-06": {
        'title': 'Adult or child',
        'condition': (
            'Ask for age with an input block and convert the answer to an integer. If age is greater than or equal to 18, print adult, otherwise — child.'
        ),
        'tests': [{'stdin': '20\n', 'expected_output': 'adult'}, {'stdin': '12\n', 'expected_output': 'child'}],
    },
    "cond-07": {
        'title': 'Sign of a number',
        'condition': (
            'Ask for an integer. Print: positive if the number is greater than zero; zero if the number equals zero; negative if the number is less than zero. Use an if block with elif and else branches.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': 'positive'},
 {'stdin': '0\n', 'expected_output': 'zero'},
 {'stdin': '-3\n', 'expected_output': 'negative'}],
    },
    "cond-08": {
        'title': 'Passed the test',
        'condition': (
            'Ask for a test grade (integer from 1 to 5). If the grade is greater than or equal to 4, print passed, otherwise — failed.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': 'passed'}, {'stdin': '3\n', 'expected_output': 'failed'}],
    },
    "cond-09": {
        'title': 'Word for a grade',
        'condition': (
            'Ask for a grade (integer). Print one word: 5 → excellent 4 → good 3 → satisfactory any other → unsatisfactory Add elif branches in the condition block.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': 'excellent'},
 {'stdin': '4\n', 'expected_output': 'good'},
 {'stdin': '2\n', 'expected_output': 'unsatisfactory'}],
    },
    "cond-10": {
        'title': 'Time of day',
        'condition': (
            'Ask for the hour (integer from 0 to 23). Print: from 6 to 11 inclusive — morning from 12 to 17 inclusive — afternoon from 18 to 22 inclusive — evening otherwise — night'
        ),
        'hint': 'Check the hours in order: morning first, then afternoon, and so on.',
        'tests': [{'stdin': '8\n', 'expected_output': 'morning'},
 {'stdin': '14\n', 'expected_output': 'afternoon'},
 {'stdin': '21\n', 'expected_output': 'evening'},
 {'stdin': '2\n', 'expected_output': 'night'}],
    },
    "cond-11": {
        'title': 'Who is greater?',
        'condition': (
            'Ask for two integers. If the first is greater than the second — print first, if the second is greater — second, if the numbers are equal — equal.'
        ),
        'tests': [{'stdin': '10\n3\n', 'expected_output': 'first'},
 {'stdin': '2\n9\n', 'expected_output': 'second'},
 {'stdin': '5\n5\n', 'expected_output': 'equal'}],
    },
    "cond-12": {
        'title': 'Can go out?',
        'condition': (
            'Parents decide whether to let a child (age = 10) go outside. warm = true. If age is at least 6 and the weather is warm — can go out, otherwise — stay home. Connect the conditions with an and block.'
        ),
        'tests': [{'expected_output': 'can go out'}],
    },
    "cond-13": {
        'title': 'Need an umbrella?',
        'condition': (
            'Forecast: rain = false, but wind = true. If it is raining or windy — advise take an umbrella, otherwise — no umbrella needed. Use an or block.'
        ),
        'tests': [{'expected_output': 'take an umbrella'}],
    },
    "cond-14": {
        'title': 'Secret code',
        'condition': (
            'Ask for a code (as text). If the entered code equals the string Python, print door open, otherwise — wrong code.'
        ),
        'hint': 'Compare text exactly — the capital letter P matters.',
        'tests': [{'stdin': 'Python\n', 'expected_output': 'door open'},
 {'stdin': 'python\n', 'expected_output': 'wrong code'}],
    },
    "cond-15": {
        'title': 'Vowel or consonant',
        'condition': (
            'Ask for one letter (as text). If the letter is in the string aeiou (in block), print vowel, otherwise — consonant.'
        ),
        'tests': [{'stdin': 'o\n', 'expected_output': 'vowel'}, {'stdin': 'k\n', 'expected_output': 'consonant'}],
    },
    "cond-16": {
        'title': 'Is there a dog?',
        'condition': (
            'Ask for a phrase (as text). If the text contains the word dog (check with the in block), print about animals, otherwise — other topic.'
        ),
        'tests': [{'stdin': 'I have a dog\n', 'expected_output': 'about animals'},
 {'stdin': 'I love math\n', 'expected_output': 'other topic'}],
    },
    "cond-17": {
        'title': 'Choose transport',
        'condition': (
            'Ask for a number (integer): 1 — bus, 2 — train, 3 — plane. Print bus, train, or plane accordingly. For any other number print unknown.'
        ),
        'tests': [{'stdin': '1\n', 'expected_output': 'bus'},
 {'stdin': '3\n', 'expected_output': 'plane'},
 {'stdin': '9\n', 'expected_output': 'unknown'}],
    },
    "cond-18": {
        'title': 'What is the weather?',
        'condition': (
            'Ask for temperature (integer). Print: above 30 — hot above 15 — warm above 0 — cool otherwise — cold'
        ),
        'hint': 'Check from higher temperature to lower — hot first, then warm.',
        'tests': [{'stdin': '35\n', 'expected_output': 'hot'},
 {'stdin': '20\n', 'expected_output': 'warm'},
 {'stdin': '-5\n', 'expected_output': 'cold'}],
    },
    "cond-19": {
        'title': 'Allowed on the slide?',
        'condition': (
            'Ask for two numbers: age and height in centimeters (both integers). If age is at least 12 and height is at least 140, print allowed, otherwise — not allowed.'
        ),
        'tests': [{'stdin': '13\n150\n', 'expected_output': 'allowed'},
 {'stdin': '10\n145\n', 'expected_output': 'not allowed'},
 {'stdin': '14\n130\n', 'expected_output': 'not allowed'}],
    },
    "cond-20": {
        'title': 'Smart assistant',
        'condition': (
            'Ask for name and age (two inputs). Convert age to an integer. 1) Print Hello, NAME! (substitute the entered name). 2) On the next line: if age ≥ 18 — of legal age, otherwise — underage. 3) On the next line: if age ≥ 6 and ≤ 17 — in school, otherwise — not in school.'
        ),
        'hint': 'Save name and age in variables — you will need them several times.',
        'tests': [{'stdin': 'Anna\n15\n', 'expected_output': 'Hello, Anna!\nunderage\nin school'},
 {'stdin': 'Ivan\n25\n', 'expected_output': 'Hello, Ivan!\nof legal age\nnot in school'}],
    },
    "cond-21": {
        'title': 'Leap year',
        'condition': (
            'Ask for a year (integer). If the year divides by 4 with no remainder — print leap year, otherwise — regular.'
        ),
        'tests': [{'stdin': '2024\n', 'expected_output': 'leap year'},
 {'stdin': '2023\n', 'expected_output': 'regular'}],
    },
    "cond-22": {
        'title': 'Triangle type',
        'condition': (
            'Ask for three side lengths (integers). If all three are equal — equilateral. If exactly two are equal — isosceles. Otherwise — scalene.'
        ),
        'tests': [{'stdin': '5\n5\n5\n', 'expected_output': 'equilateral'},
 {'stdin': '5\n5\n3\n', 'expected_output': 'isosceles'},
 {'stdin': '3\n4\n5\n', 'expected_output': 'scalene'}],
    },
    "cond-23": {
        'title': 'Grade by points',
        'condition': (
            'Ask for points (0–100). 90 and above — excellent, 70–89 — good, 50–69 — satisfactory, otherwise — fail.'
        ),
        'tests': [{'stdin': '95\n', 'expected_output': 'excellent'},
 {'stdin': '75\n', 'expected_output': 'good'},
 {'stdin': '55\n', 'expected_output': 'satisfactory'},
 {'stdin': '40\n', 'expected_output': 'fail'}],
    },
    "cond-24": {
        'title': 'Login and password',
        'condition': (
            'Ask for login and password (two text values). If login is admin and password is 12345 — access granted, otherwise — denied.'
        ),
        'tests': [{'stdin': 'admin\n12345\n', 'expected_output': 'access granted'},
 {'stdin': 'admin\n0000\n', 'expected_output': 'denied'}],
    },
    "cond-25": {
        'title': 'Positive and even',
        'condition': (
            'Ask for an integer. If it is positive and even — print suitable, otherwise — not suitable.'
        ),
        'tests': [{'stdin': '8\n', 'expected_output': 'suitable'},
 {'stdin': '7\n', 'expected_output': 'not suitable'},
 {'stdin': '-4\n', 'expected_output': 'not suitable'}],
    },
    "cond-26": {
        'title': 'FizzBuzz',
        'condition': (
            'Ask for integer n. If n divides by 3 and by 5 — FizzBuzz. Only by 3 — Fizz. Only by 5 — Buzz. Otherwise — n itself.'
        ),
        'tests': [{'stdin': '15\n', 'expected_output': 'FizzBuzz'},
 {'stdin': '9\n', 'expected_output': 'Fizz'},
 {'stdin': '10\n', 'expected_output': 'Buzz'},
 {'stdin': '7\n', 'expected_output': '7'}],
    },
    "cond-27": {
        'title': 'Season',
        'condition': (
            'Ask for month number (1–12). 12, 1, 2 — winter; 3–5 — spring; 6–8 — summer; 9–11 — autumn. Any other number — error.'
        ),
        'tests': [{'stdin': '1\n', 'expected_output': 'winter'},
 {'stdin': '4\n', 'expected_output': 'spring'},
 {'stdin': '7\n', 'expected_output': 'summer'},
 {'stdin': '10\n', 'expected_output': 'autumn'}],
    },
    "cond-28": {
        'title': 'Mini calculator',
        'condition': (
            'Ask for an operation sign (+, -, *, / as text) and two integers. Print the result. For an unknown sign — error.'
        ),
        'tests': [{'stdin': '+\n5\n3\n', 'expected_output': '8'},
 {'stdin': '*\n4\n5\n', 'expected_output': '20'},
 {'stdin': '/\n7\n2\n', 'expected_output': '3.5'},
 {'stdin': '%\n1\n1\n', 'expected_output': 'error'}],
    },
    "cond-29": {
        'title': 'Strong password',
        'condition': (
            'Ask for a password (text). If the length is at least 8 — strong, otherwise — weak.'
        ),
        'tests': [{'stdin': 'abcdefgh\n', 'expected_output': 'strong'},
 {'stdin': '123\n', 'expected_output': 'weak'}],
    },
    "cond-30": {
        'title': 'Final report',
        'condition': (
            'Ask for name, age (integer), and test score (0–100). Print three lines: 1) Student: NAME 2) if score ≥ 80 — passed, otherwise — failed 3) if age < 10 — junior, otherwise — senior'
        ),
        'tests': [{'stdin': 'Tim\n9\n85\n', 'expected_output': 'Student: Tim\npassed\njunior'},
 {'stdin': 'Anna\n14\n70\n', 'expected_output': 'Student: Anna\nfailed\nsenior'}],
    },
    "cond-31": {
        'title': 'In range?',
        'condition': (
            'Ask for number x, then bounds a and b (all integers). If a ≤ x ≤ b, print in range, otherwise — out of range.'
        ),
        'tests': [{'stdin': '5\n1\n10\n', 'expected_output': 'in range'},
 {'stdin': '15\n1\n10\n', 'expected_output': 'out of range'},
 {'stdin': '1\n1\n5\n', 'expected_output': 'in range'}],
    },
    "cond-32": {
        'title': 'Maximum of three',
        'condition': (
            'Ask for three integers. Find the largest and print: first, second, or third — depending on which number is greatest.'
        ),
        'hint': (
            'Compare the numbers step by step without printing the maximum value itself.'
        ),
        'tests': [{'stdin': '1\n5\n3\n', 'expected_output': 'second'},
 {'stdin': '9\n2\n7\n', 'expected_output': 'first'},
 {'stdin': '4\n4\n8\n', 'expected_output': 'third'}],
    },
    "cond-33": {
        'title': 'Divides evenly?',
        'condition': (
            'Ask for dividend and divisor (integers, divisor not zero). If the dividend divides by the divisor with no remainder — divides, otherwise — does not divide.'
        ),
        'tests': [{'stdin': '10\n5\n', 'expected_output': 'divides'},
 {'stdin': '10\n3\n', 'expected_output': 'does not divide'}],
    },
    "cond-34": {
        'title': 'Triangle possible?',
        'condition': (
            'Three segments a, b, c can form a triangle if the sum of any two sides is greater than the third. Ask for three lengths (integers) and print possible or impossible.'
        ),
        'tests': [{'stdin': '3\n4\n5\n', 'expected_output': 'possible'},
 {'stdin': '1\n2\n5\n', 'expected_output': 'impossible'},
 {'stdin': '5\n5\n5\n', 'expected_output': 'possible'}],
    },
    "cond-35": {
        'title': 'Grade jump',
        'condition': (
            'Ask for two grades in a row (integers from 1 to 5). If the absolute difference is at least 2 — jump, otherwise — stable.'
        ),
        'tests': [{'stdin': '5\n3\n', 'expected_output': 'jump'},
 {'stdin': '4\n5\n', 'expected_output': 'stable'},
 {'stdin': '2\n5\n', 'expected_output': 'jump'}],
    },
    "cond-fix-01": {
        'title': 'Fix: greater than ten?',
        'condition': (
            'At temperature 15 the program answers «no», although the value is clearly greater than 10. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Check the comparison sign in the condition.',
        'tests': [{'expected_output': 'yes'}],
    },
    "cond-fix-02": {
        'title': 'Fix: sign of a number',
        'condition': (
            'The number classifier mixes up labels: positive numbers are called negative and vice versa. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Match each branch to the correct text.',
        'tests': [{'stdin': '5\n', 'expected_output': 'positive'},
 {'stdin': '0\n', 'expected_output': 'zero'},
 {'stdin': '-3\n', 'expected_output': 'negative'}],
    },
    "cond-fix-03": {
        'title': 'Fix: adult or child',
        'condition': (
            'The age check prints «adult» for a schoolchild and «child» for an adult — the branches are swapped. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'At age 20 the output should be «adult», at 12 — «child».',
        'tests': [{'stdin': '20\n', 'expected_output': 'adult'}, {'stdin': '12\n', 'expected_output': 'child'}],
    },
    "cond-fix-04": {
        'title': 'Fix: can go out?',
        'condition': (
            'A 10-year-old child is not allowed outside in warm weather — the age threshold in the condition is too high. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'At age 10 in warm weather, going outside is allowed.',
        'tests': [{'expected_output': 'can go out'}],
    },
    "cond-fix-05": {
        'title': 'Fix: FizzBuzz',
        'condition': (
            'FizzBuzz on 15 prints only Fizz — the branch for dividing by both 3 and 5 comes too late. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Check division by 3 and 5 together first.',
        'tests': [{'stdin': '15\n', 'expected_output': 'FizzBuzz'},
 {'stdin': '9\n', 'expected_output': 'Fizz'},
 {'stdin': '10\n', 'expected_output': 'Buzz'},
 {'stdin': '7\n', 'expected_output': '7'}],
    },
    "cond-fix-06": {
        'title': 'Fix: in range?',
        'condition': (
            'The number 15 is considered «in range» for segment [1, 10] — only the left bound is checked. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to check both the left and the right bound.',
        'tests': [{'stdin': '5\n1\n10\n', 'expected_output': 'in range'},
 {'stdin': '15\n1\n10\n', 'expected_output': 'out of range'},
 {'stdin': '1\n1\n5\n', 'expected_output': 'in range'}],
    },
    "cond-fix-07": {
        'title': 'Fix: maximum of three',
        'condition': (
            'Among three numbers the third is the largest, but the program compares only the first two. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The third number can be the maximum too.',
        'tests': [{'stdin': '1\n5\n3\n', 'expected_output': 'second'},
 {'stdin': '9\n2\n7\n', 'expected_output': 'first'},
 {'stdin': '4\n4\n8\n', 'expected_output': 'third'}],
    },
    "cond-fix-08": {
        'title': 'Fix: divides evenly?',
        'condition': (
            'The check whether 10 divides by 5 answers «does not divide» — integer division is used instead of the remainder. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'To check divisibility you need the remainder (%).',
        'tests': [{'stdin': '10\n5\n', 'expected_output': 'divides'},
 {'stdin': '10\n3\n', 'expected_output': 'does not divide'}],
    },
    "cond-fix-09": {
        'title': 'Fix: triangle',
        'condition': (
            'Segments 1, 2, and 5 are wrongly accepted as a triangle — only one of the three inequalities is checked. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to check all three pairs of sides.',
        'tests': [{'stdin': '3\n4\n5\n', 'expected_output': 'possible'},
 {'stdin': '1\n2\n5\n', 'expected_output': 'impossible'},
 {'stdin': '5\n5\n5\n', 'expected_output': 'possible'}],
    },
    "cond-fix-10": {
        'title': 'Fix: grade jump',
        'condition': (
            'Grades 5 and 3 are marked as «stable», although the difference between them is 2. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'A jump occurs when the difference is 2 or more.',
        'tests': [{'stdin': '5\n3\n', 'expected_output': 'jump'},
 {'stdin': '4\n5\n', 'expected_output': 'stable'},
 {'stdin': '2\n5\n', 'expected_output': 'jump'}],
    },
    "for-01": {
        'title': 'Numbers from 1 to 5',
        'condition': (
            'Seat numbering in a row: using a for loop and range(1, 6, 1) print the numbers 1, 2, 3, 4, 5.'
        ),
        'hint': 'The second number in range is not included — for five numbers use 6.',
        'tests': [{'expected_output': '1\n2\n3\n4\n5'}],
    },
    "for-02": {
        'title': 'Four times Python',
        'condition': (
            'At a conference there are four talks about Python — print the language name four times in a for loop with range(0, 4, 1).'
        ),
        'tests': [{'expected_output': 'Python\nPython\nPython\nPython'}],
    },
    "for-03": {
        'title': 'Evens from zero',
        'condition': (
            'Even centimeters from 0 to 8 are marked on a measuring tape. Iterate range(0, 10, 2) in a for loop and print each mark.'
        ),
        'tests': [{'expected_output': '0\n2\n4\n6\n8'}],
    },
    "for-04": {
        'title': 'From ten down to one',
        'condition': (
            'Countdown at the finish: use range(10, 0, -1) and print numbers from 10 to 1.'
        ),
        'tests': [{'expected_output': '10\n9\n8\n7\n6\n5\n4\n3\n2\n1'}],
    },
    "for-05": {
        'title': 'Sum from 1 to 10',
        'condition': (
            'Iterate range(1, 11, 1), accumulate the sum in a variable and print 55.'
        ),
        'tests': [{'expected_output': '55'}],
    },
    "for-06": {
        'title': 'Squares from 1 to 5',
        'condition': 'In a for loop for i in range(1, 6, 1) print i × i for each i.',
        'tests': [{'expected_output': '1\n4\n9\n16\n25'}],
    },
    "for-07": {
        'title': 'Count to n',
        'condition': (
            'Ask for an integer n. In a for loop with range from 1 to n + 1 print each number.'
        ),
        'hint': 'For range up to n inclusive the upper bound is n + 1.',
        'tests': [{'stdin': '4\n', 'expected_output': '1\n2\n3\n4'},
 {'stdin': '6\n', 'expected_output': '1\n2\n3\n4\n5\n6'}],
    },
    "for-08": {
        'title': 'From fifth to fifteenth',
        'condition': 'Iterate range(5, 16, 1) and print all numbers.',
        'tests': [{'expected_output': '5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15'}],
    },
    "for-09": {
        'title': 'Triple the numbers',
        'condition': 'In a for loop for x in range(3, 8, 1) print x × 3.',
        'tests': [{'expected_output': '9\n12\n15\n18\n21'}],
    },
    "for-10": {
        'title': 'Step three',
        'condition': 'Iterate range(1, 10, 3) and print the numbers.',
        'tests': [{'expected_output': '1\n4\n7'}],
    },
    "for-11": {
        'title': 'Product 1×2×3×4×5',
        'condition': 'In a for loop multiply numbers from 1 to 5 and print the result 120.',
        'hint': 'Create variable product = 1 and multiply in the loop.',
        'tests': [{'expected_output': '120'}],
    },
    "for-12": {
        'title': 'Zero and onward',
        'condition': 'Ask for an integer n. Print numbers range(0, n, 1) — from 0 to n − 1.',
        'tests': [{'stdin': '5\n', 'expected_output': '0\n1\n2\n3\n4'},
 {'stdin': '3\n', 'expected_output': '0\n1\n2'}],
    },
    "for-13": {
        'title': 'Decrease by two',
        'condition': 'Iterate range(20, 10, -2) and print each number.',
        'tests': [{'expected_output': '20\n18\n16\n14\n12'}],
    },
    "for-14": {
        'title': 'From a to b',
        'condition': (
            'Ask for two integers: start and end. Print all numbers from start to end − 1 using range(start, end, 1).'
        ),
        'tests': [{'stdin': '3\n7\n', 'expected_output': '3\n4\n5\n6'},
 {'stdin': '10\n13\n', 'expected_output': '10\n11\n12'}],
    },
    "for-15": {
        'title': 'Sum of evens',
        'condition': (
            'Add the even numbers 2, 4, 6, 8, 10 in a for loop with range(2, 11, 2) and print 30.'
        ),
        'tests': [{'expected_output': '30'}],
    },
    "for-16": {
        'title': 'Plus ten',
        'condition': 'In a for loop for i in range(1, 6, 1) print i + 10.',
        'tests': [{'expected_output': '11\n12\n13\n14\n15'}],
    },
    "for-17": {
        'title': 'Fives up to n',
        'condition': (
            'Ask for an integer n. In a for loop for i in range(1, n + 1, 1) print i × 5.'
        ),
        'tests': [{'stdin': '4\n', 'expected_output': '5\n10\n15\n20'},
 {'stdin': '3\n', 'expected_output': '5\n10\n15'}],
    },
    "for-18": {
        'title': 'Hundred with step 25',
        'condition': 'Iterate range(100, 0, -25) and print the numbers.',
        'tests': [{'expected_output': '100\n75\n50\n25'}],
    },
    "for-19": {
        'title': 'Stars by count',
        'condition': (
            'A viewer rates a performance: ask how many «stars» to give, and print the word star that many times in a for loop.'
        ),
        'tests': [{'stdin': '3\n', 'expected_output': 'star\nstar\nstar'},
 {'stdin': '2\n', 'expected_output': 'star\nstar'}],
    },
    "for-20": {
        'title': 'For marathon',
        'condition': (
            'Ask for an integer n. Print on three lines: 1) the sum of numbers from 1 to n (for loop) 2) the product of numbers from 1 to n 3) the number n itself'
        ),
        'hint': 'For the product start at 1, for the sum — at 0.',
        'tests': [{'stdin': '4\n', 'expected_output': '10\n24\n4'},
 {'stdin': '5\n', 'expected_output': '15\n120\n5'}],
    },
    "for-21": {
        'title': 'Table of 7',
        'condition': 'Iterate i from 1 to 10 in a for loop and print i × 7.',
        'tests': [{'expected_output': '7\n14\n21\n28\n35\n42\n49\n56\n63\n70'}],
    },
    "for-22": {
        'title': 'Sum of squares',
        'condition': (
            'Ask for n. In a for loop find the sum of squares from 1 to n and print.'
        ),
        'tests': [{'stdin': '4\n', 'expected_output': '30'}, {'stdin': '5\n', 'expected_output': '55'}],
    },
    "for-23": {
        'title': 'How many evens',
        'condition': (
            'Ask for a and b (a ≤ b). Count in a for loop how many even numbers are in the range from a to b inclusive.'
        ),
        'tests': [{'stdin': '1\n10\n', 'expected_output': '5'}, {'stdin': '2\n9\n', 'expected_output': '4'}],
    },
    "for-24": {
        'title': 'Product of odds',
        'condition': 'In a for loop find the product of odd numbers from 1 to 7 and print.',
        'tests': [{'expected_output': '105'}],
    },
    "for-25": {
        'title': 'Star ladder',
        'condition': 'In a for loop with i from 1 to 4 print i asterisks on each line.',
        'hint': 'Line 1 — one *, line 2 — two * and so on.',
        'tests': [{'expected_output': '*\n**\n***\n****'}],
    },
    "for-26": {
        'title': 'Sum of evens up to n',
        'condition': (
            'Ask for n. In a for loop add all even numbers from 2 to n (if n is odd — up to n − 1).'
        ),
        'tests': [{'stdin': '10\n', 'expected_output': '30'}, {'stdin': '7\n', 'expected_output': '12'}],
    },
    "for-27": {
        'title': 'Fibonacci numbers',
        'condition': (
            'Ask for n (≥ 2). Print the first n Fibonacci numbers each on a new line, starting with 1 and 1.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': '1\n1\n2\n3\n5'},
 {'stdin': '7\n', 'expected_output': '1\n1\n2\n3\n5\n8\n13'}],
    },
    "for-28": {
        'title': 'Maximum in range',
        'condition': (
            'Ask for a and b (a ≤ b). Find the maximum number in the range from a to b via a for loop.'
        ),
        'tests': [{'stdin': '3\n9\n', 'expected_output': '9'}, {'stdin': '-2\n5\n', 'expected_output': '5'}],
    },
    "for-29": {
        'title': 'Countdown for',
        'condition': 'Ask for n. In a for loop print n, n−1, …, 1 (each on a new line).',
        'tests': [{'stdin': '5\n', 'expected_output': '5\n4\n3\n2\n1'}],
    },
    "for-30": {
        'title': 'Final for',
        'condition': (
            'Ask for n. On three lines print: the sum 1..n, the sum of squares 1..n, and how many numbers from 1 to n are divisible by 3.'
        ),
        'tests': [{'stdin': '6\n', 'expected_output': '21\n91\n2'}],
    },
    "for-31": {
        'title': 'First n odds',
        'condition': (
            'Ask for n. Print the first n odd numbers, starting from 1 (each on a new line).'
        ),
        'hint': 'Hint: range(1, 2 * n, 2).',
        'tests': [{'stdin': '4\n', 'expected_output': '1\n3\n5\n7'}, {'stdin': '1\n', 'expected_output': '1'}],
    },
    "for-32": {
        'title': 'Multiples of k',
        'condition': (
            'Ask for n and k (integers). Print all numbers from k to n inclusive that are divisible by k.'
        ),
        'tests': [{'stdin': '20\n3\n', 'expected_output': '3\n6\n9\n12\n15\n18'},
 {'stdin': '10\n5\n', 'expected_output': '5\n10'}],
    },
    "for-33": {
        'title': 'Sum of evens in segment',
        'condition': (
            'Ask for bounds a and b (a ≤ b). In a for loop add all even numbers from a to b inclusive and print the sum.'
        ),
        'tests': [{'stdin': '1\n10\n', 'expected_output': '30'}, {'stdin': '4\n4\n', 'expected_output': '4'}],
    },
    "for-34": {
        'title': 'How many letters in a word',
        'condition': (
            'Ask for a letter, then a word. Count in a for loop how many times that letter appears in the word, and print the number.'
        ),
        'tests': [{'stdin': 'a\nbanana\n', 'expected_output': '3'}, {'stdin': 'o\ndog\n', 'expected_output': '1'}],
    },
    "for-35": {
        'title': 'Numbers divisible by six',
        'condition': (
            'Ask for n. Print all numbers from 1 to n inclusive that are divisible by both 2 and 3 (each on a new line).'
        ),
        'tests': [{'stdin': '30\n', 'expected_output': '6\n12\n18\n24\n30'},
 {'stdin': '12\n', 'expected_output': '6\n12'}],
    },
    "for-fix-01": {
        'title': 'Fix: from 1 to 5',
        'condition': (
            'The for loop prints only 1, 2, 3, 4 — the upper bound of range is set without including the last number. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'In range the end of the interval is not included.',
        'tests': [{'expected_output': '1\n2\n3\n4\n5'}],
    },
    "for-fix-02": {
        'title': 'Fix: four times Python',
        'condition': (
            'The word Python should appear four times, but the loop prints it only three. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Count how many values range(0, 3) produces.',
        'tests': [{'expected_output': 'Python\nPython\nPython\nPython'}],
    },
    "for-fix-03": {
        'title': 'Fix: sum from 1 to 10',
        'condition': (
            'Instead of the sum 1+…+10 the program multiplies the numbers and produces a huge result. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'For a sum use addition, not multiplication.',
        'tests': [{'expected_output': '55'}],
    },
    "for-fix-04": {
        'title': 'Fix: squares from 1 to 5',
        'condition': (
            'Squares 1, 4, 9… should be printed, but the numbers 1, 2, 3… are shown instead. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to print i * i.',
        'tests': [{'expected_output': '1\n4\n9\n16\n25'}],
    },
    "for-fix-05": {
        'title': 'Fix: from 1 to n',
        'condition': (
            'For n = 5 the last number 5 is not printed — the upper bound of range does not include n. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'To include n, increase the second argument of range by 1.',
        'tests': [{'stdin': '4\n', 'expected_output': '1\n2\n3\n4'},
 {'stdin': '6\n', 'expected_output': '1\n2\n3\n4\n5\n6'}],
    },
    "for-fix-06": {
        'title': 'Fix: odd numbers',
        'condition': (
            'The first odd numbers are replaced by evens: 2, 4, 6… instead of 1, 3, 5…. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The first odd number is 1, step is 2.',
        'tests': [{'stdin': '4\n', 'expected_output': '1\n3\n5\n7'}, {'stdin': '1\n', 'expected_output': '1'}],
    },
    "for-fix-07": {
        'title': 'Fix: multiples of k',
        'condition': (
            'The list of multiples starts at zero, although 0 is not in the required range. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The first multiple of k is k itself.',
        'tests': [{'stdin': '20\n3\n', 'expected_output': '3\n6\n9\n12\n15\n18'},
 {'stdin': '10\n5\n', 'expected_output': '5\n10'}],
    },
    "for-fix-08": {
        'title': 'Fix: sum of evens',
        'condition': (
            'The sum of «evens» in the segment equals the sum of all numbers — odd numbers are included too. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Add to the sum only even i.',
        'tests': [{'stdin': '1\n10\n', 'expected_output': '30'}, {'stdin': '4\n4\n', 'expected_output': '4'}],
    },
    "for-fix-09": {
        'title': 'Fix: letter count',
        'condition': (
            'Counting the letter «a» in the word «banana» gives 1 — each character is compared to the whole string. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Compare each character with the sought letter ch.',
        'tests': [{'stdin': 'a\nbanana\n', 'expected_output': '3'}, {'stdin': 'o\ndog\n', 'expected_output': '1'}],
    },
    "for-fix-10": {
        'title': 'Fix: numbers divisible by six',
        'condition': (
            'Instead of numbers divisible by 6, all even numbers are printed — the check for divisibility by 3 is missing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'A number divisible by 6 is divisible by both 2 and 3.',
        'tests': [{'stdin': '30\n', 'expected_output': '6\n12\n18\n24\n30'},
 {'stdin': '12\n', 'expected_output': '6\n12'}],
    },
    "io-01": {
        'title': 'Hello, world!',
        'condition': (
            'By tradition, the first program in any language greets the world. Print on screen: Hello, world!'
        ),
        'tests': [{'expected_output': 'Hello, world!'}],
    },
    "io-02": {
        'title': 'New student',
        'condition': (
            'A new student joined the class. Write her name on the door sign — print on screen: Anna'
        ),
        'tests': [{'expected_output': 'Anna'}],
    },
    "io-03": {
        'title': 'School poster',
        'condition': (
            'A poster on the wall has one big word. Help print the sign from the poster: School'
        ),
        'tests': [{'expected_output': 'School'}],
    },
    "io-04": {
        'title': 'Favorite subject',
        'condition': (
            'A student answers the question «Which subject do you like most?». Save the answer computer science in variable subject and show it on screen.'
        ),
        'tests': [{'expected_output': 'computer science'}],
    },
    "io-05": {
        'title': 'City on a form',
        'condition': (
            'An olympiad registration form has a «City» field. Store London in variable city and print it.'
        ),
        'tests': [{'expected_output': 'London'}],
    },
    "io-06": {
        'title': 'Two greetings',
        'condition': (
            'Two friends chat in a messenger. Print their lines in order: first Hello!, then How are you?'
        ),
        'tests': [{'expected_output': 'Hello!\nHow are you?'}],
    },
    "io-07": {
        'title': 'Countdown before start',
        'condition': (
            'Before a race the referee counts aloud. Print three lines: One, Two, Three'
        ),
        'tests': [{'expected_output': 'One\nTwo\nThree'}],
    },
    "io-08": {
        'title': 'Variable and text',
        'condition': (
            'You started learning a new language. Store it in variable language = Python, then print the phrase I am learning Python (you can build it with «join text» or print the variable separately).'
        ),
        'tests': [{'expected_output': 'I am learning Python'}],
    },
    "io-09": {
        'title': 'Introduction',
        'condition': (
            'A robot greets guests at the entrance. Ask for a name with an input block and reply: Hello,  with the entered name'
        ),
        'tests': [{'stdin': 'Masha\n', 'expected_output': 'Hello, Masha'},
 {'stdin': 'Peter\n', 'expected_output': 'Hello, Peter'}],
    },
    "io-10": {
        'title': 'Animal quiz',
        'condition': (
            "The quiz host asks: «Name your favorite animal!» Ask for an answer with an input block and repeat it on screen — as if confirming the contestant's answer."
        ),
        'tests': [{'stdin': 'cat\n', 'expected_output': 'cat'}, {'stdin': 'dolphin\n', 'expected_output': 'dolphin'}],
    },
    "io-11": {
        'title': 'Postcard',
        'condition': (
            "A postcard needs the sender's city. Ask for the city with an input block, save it in variable city and print it."
        ),
        'tests': [{'stdin': 'Paris\n', 'expected_output': 'Paris'},
 {'stdin': 'Berlin\n', 'expected_output': 'Berlin'}],
    },
    "io-12": {
        'title': "Friend's profile",
        'condition': (
            'Make a mini profile: ask for name and favorite color. Show both answers — each on a new line.'
        ),
        'tests': [{'stdin': 'Olivia\nblue\n', 'expected_output': 'Olivia\nblue'}],
    },
    "io-13": {
        'title': 'Echo machine',
        'condition': (
            'An echo machine repeats everything you say — twice. Ask for a word and print it two times in a row (two «print» blocks).'
        ),
        'tests': [{'stdin': 'Hello\n', 'expected_output': 'Hello\nHello'}],
    },
    "io-14": {
        'title': 'Player profile',
        'condition': (
            'A game creates a character profile. Ask for name, then age (as text) and print both fields on separate lines.'
        ),
        'tests': [{'stdin': 'Igor\n12\n', 'expected_output': 'Igor\n12'}],
    },
    "io-15": {
        'title': 'Secret word',
        'condition': (
            'An agent writes a code word in a notebook. Ask for the secret word, save it in variable word and print the notebook entry.'
        ),
        'tests': [{'stdin': 'Python\n', 'expected_output': 'Python'}],
    },
    "io-16": {
        'title': "Coach's command",
        'condition': (
            'The coach gives a short command to athletes. Set command = Run! and duplicate it on screen twice.'
        ),
        'tests': [{'expected_output': 'Run!\nRun!'}],
    },
    "io-17": {
        'title': 'Mini story',
        'condition': (
            'Write a short three-line dialogue — each on a new line:\n— Hello!\n— Hello!\n— Shall we go for a walk?'
        ),
        'tests': [{'expected_output': '— Hello!\n— Hello!\n— Shall we go for a walk?'}],
    },
    "io-18": {
        'title': 'Hero card',
        'condition': (
            'In a role-playing game a character has a name and a trait. Create name = Hero and title = brave, then print both lines.'
        ),
        'tests': [{'expected_output': 'Hero\nbrave'}],
    },
    "io-19": {
        'title': 'Greeting by name',
        'condition': (
            'The host welcomes a guest at the door. Ask for a name and say: Glad to see you, NAME! (substitute the entered name).'
        ),
        'tests': [{'stdin': 'Sam\n', 'expected_output': 'Glad to see you, Sam!'}],
    },
    "io-20": {
        'title': 'Input-output marathon',
        'condition': (
            'Final student interview: ask for favorite school subject and dream. Show both answers, then print a wish: Good luck in school!'
        ),
        'tests': [{'stdin': 'math\nbecome a programmer\n',
  'expected_output': 'math\nbecome a programmer\nGood luck in school!'}],
    },
    "io-21": {
        'title': 'Business card',
        'condition': (
            'Build an electronic card: ask for name, grade (number as text) and city. Print three lines: Student: NAME, Grade: GRADE, City: CITY'
        ),
        'tests': [{'stdin': 'Masha\n5\nLondon\n', 'expected_output': 'Student: Masha\nGrade: 5\nCity: London'}],
    },
    "io-22": {
        'title': 'Echo with label',
        'condition': (
            "A radio station repeats a listener's message with a label. Ask for a word and print You said: WORD twice."
        ),
        'tests': [{'stdin': 'Python\n', 'expected_output': 'You said: Python\nYou said: Python'}],
    },
    "io-23": {
        'title': 'Three words with commas',
        'condition': (
            'Make a short list of three words: ask for them one by one and join into one string with comma and space.'
        ),
        'hint': 'Save each word in a variable and build the string with «join text».',
        'tests': [{'stdin': 'cat\nhouse\ngarden\n', 'expected_output': 'cat, house, garden'}],
    },
    "io-24": {
        'title': 'Password length',
        'condition': (
            'Password strength check: ask for a password (as text) and print on two lines the password itself and its length.'
        ),
        'tests': [{'stdin': 'abc123\n', 'expected_output': 'abc123\n6'}],
    },
    "io-25": {
        'title': 'Reverse order',
        'condition': (
            'Two envelopes lie in a stack — «first» at the bottom, «second» on top. Ask for two strings, save in a and b, but print in reverse order: b first, then a.'
        ),
        'tests': [{'stdin': 'first\nsecond\n', 'expected_output': 'second\nfirst'}],
    },
    "io-26": {
        'title': 'Shopping list',
        'condition': (
            'Mom gave a list of three products — ask the user for them and format a numbered list: 1) …, 2) …, 3) … (each item on a new line).'
        ),
        'tests': [{'stdin': 'milk\nbread\ncheese\n', 'expected_output': '1) milk\n2) bread\n3) cheese'}],
    },
    "io-27": {
        'title': 'Exclamation',
        'condition': (
            'A fan shouts a word with an exclamation mark. Ask for a word and add ! at the end when printing.'
        ),
        'tests': [{'stdin': 'Hooray\n', 'expected_output': 'Hooray!'}],
    },
    "io-28": {
        'title': 'Two numbers as text',
        'condition': (
            'A stock ticker shows a range as text. Ask for two numbers (as text) and print them with spaces around a dash: num1 - num2'
        ),
        'tests': [{'stdin': '12\n34\n', 'expected_output': '12 - 34'}],
    },
    "io-29": {
        'title': 'Repeat three times',
        'condition': (
            'An exam mantra: ask for a phrase and print it three times — each time on a new line.'
        ),
        'tests': [{'stdin': 'study\n', 'expected_output': 'study\nstudy\nstudy'}],
    },
    "io-30": {
        'title': 'Farewell program',
        'condition': (
            'The program says goodbye to the user. Ask for name and dream, then print three lines: Hello, NAME! — Your dream: DREAM — Good luck!'
        ),
        'tests': [{'stdin': 'Kate\nscientist\n',
  'expected_output': 'Hello, Kate!\nYour dream: scientist\nGood luck!'}],
    },
    "io-31": {
        'title': 'Field order',
        'condition': (
            'In a logbook the surname comes first, then the first name. Ask for both values and print two lines: First: SURNAME and Then: NAME — in that order.'
        ),
        'hint': 'First save both inputs in variables, then plan the output.',
        'tests': [{'stdin': 'Smith\nPeter\n', 'expected_output': 'First: Smith\nThen: Peter'}],
    },
    "io-32": {
        'title': 'Code from letters',
        'condition': (
            'A cipher clerk builds a three-letter code with no spaces. Ask for three letters in a row and print them joined as one string.'
        ),
        'tests': [{'stdin': 'a\nb\nc\n', 'expected_output': 'abc'}],
    },
    "io-33": {
        'title': 'Menu line',
        'condition': (
            'A cashier prints a receipt: ask for dish name and price (as text). Print one line: Dish: NAME, price: PRICE USD.'
        ),
        'tests': [{'stdin': 'soup\n150\n', 'expected_output': 'Dish: soup, price: 150 USD.'}],
    },
    "io-34": {
        'title': 'Compare lengths',
        'condition': (
            'A linguist compares two words. Ask for two words and print four lines: first word, its length, second word, its length.'
        ),
        'tests': [{'stdin': 'cat\nelephant\n', 'expected_output': 'cat\n3\nelephant\n8'}],
    },
    "io-35": {
        'title': 'Batch label',
        'condition': (
            'A warehouse labels goods. Ask for product name and batch number (as text) and print: Batch NUMBER: NAME — OK'
        ),
        'tests': [{'stdin': 'milk\n42\n', 'expected_output': 'Batch 42: milk — OK'}],
    },
    "io-fix-01": {
        'title': 'Fix: Hello, world!',
        'condition': (
            'The first program on the course should greet the world, but the text appears without an exclamation mark. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Check punctuation in the printed string.',
        'tests': [{'expected_output': 'Hello, world!'}],
    },
    "io-fix-02": {
        'title': 'Fix: subject variable',
        'condition': (
            'A student saved the answer in variable subject, but the wrong subject is shown when printing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Look at which value is assigned to the variable.',
        'tests': [{'expected_output': 'computer science'}],
    },
    "io-fix-03": {
        'title': 'Fix: introduction',
        'condition': (
            "A robot at the entrance asks for a name but replies only «Hello!» — without the guest's name. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it."
        ),
        'hint': (
            'You need to print not just «Hello!», but «Hello, » and the entered name.'
        ),
        'tests': [{'stdin': 'Masha\n', 'expected_output': 'Hello, Masha'},
 {'stdin': 'Peter\n', 'expected_output': 'Hello, Peter'}],
    },
    "io-fix-04": {
        'title': 'Fix: two greetings',
        'condition': (
            "Two friends' chat is shown backwards: the second line appears before the first. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it."
        ),
        'hint': 'Swap the «print» blocks or their texts.',
        'tests': [{'expected_output': 'Hello!\nHow are you?'}],
    },
    "io-fix-05": {
        'title': 'Fix: greeting by name',
        'condition': (
            'The host greets a guest with «Glad to see you, …», but the exclamation mark at the end is missing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The greeting should end with an exclamation mark.',
        'tests': [{'stdin': 'Sam\n', 'expected_output': 'Glad to see you, Sam!'}],
    },
    "io-fix-06": {
        'title': 'Fix: field order',
        'condition': (
            'A log entry prints first name, then surname — but the log uses the opposite order. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The surname should come first, then the first name.',
        'tests': [{'stdin': 'Smith\nPeter\n', 'expected_output': 'First: Smith\nThen: Peter'}],
    },
    "io-fix-07": {
        'title': 'Fix: code from letters',
        'condition': (
            'A cipher clerk joins three letters, but spaces appear between them — the code is longer than needed. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The code should be continuous — no spaces between letters.',
        'tests': [{'stdin': 'a\nb\nc\n', 'expected_output': 'abc'}],
    },
    "io-fix-08": {
        'title': 'Fix: menu line',
        'condition': (
            'The receipt is almost correct, but after the price the currency unit is missing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'After the price there should be «USD.».',
        'tests': [{'stdin': 'soup\n150\n', 'expected_output': 'Dish: soup, price: 150 USD.'}],
    },
    "io-fix-09": {
        'title': 'Fix: compare lengths',
        'condition': (
            "A linguist compares words, but each word's length is printed before the word itself. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it."
        ),
        'hint': 'First the word, then its length.',
        'tests': [{'stdin': 'cat\nelephant\n', 'expected_output': 'cat\n3\nelephant\n8'}],
    },
    "io-fix-10": {
        'title': 'Fix: batch label',
        'condition': (
            'Warehouse labeling swapped batch number and product name. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'After «Batch» should come the number, not the name.',
        'tests': [{'stdin': 'milk\n42\n', 'expected_output': 'Batch 42: milk — OK'}],
    },
    "list-01": {
        'title': 'First fruit',
        'condition': (
            'On a store display the fruits stand in a row: apple, banana, pear. Store them in list fruits and show only the first fruit.'
        ),
        'hint': 'The first element — in the get element block choose «from 1».',
        'tests': [{'expected_output': 'apple'}],
    },
    "list-02": {
        'title': 'How many numbers',
        'condition': (
            'A grade book records scores: 5, 10, 15. Save them in list numbers and print how many entries are in the book.'
        ),
        'tests': [{'expected_output': '3'}],
    },
    "list-03": {
        'title': 'Add four',
        'condition': (
            'To the row of numbers 1, 2, 3 a new participant arrived — 4. Add it to the end of list numbers and show the updated row.'
        ),
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-04": {
        'title': 'Empty list',
        'condition': (
            'Start with an empty list of alphabet letters. Add a and b to it in order, then print the list.'
        ),
        'tests': [{'expected_output': "['a', 'b']"}],
    },
    "list-05": {
        'title': 'Loop over a list',
        'condition': (
            'A scoreboard shows numbers 1, 2, 3, 4, 5. Save them in a list and in a for loop print each number on a new line.'
        ),
        'tests': [{'expected_output': '1\n2\n3\n4\n5'}],
    },
    "list-06": {
        'title': 'Sum of a list',
        'condition': (
            'A cashier adds receipts: 10, 20 and 30 dollars. Write the amounts in a list and in a for loop find the total — 60.'
        ),
        'tests': [{'expected_output': '60'}],
    },
    "list-07": {
        'title': 'Insert 99',
        'condition': (
            'An urgent client with ticket 99 joined the front of the queue. In list numbers = [1, 2, 3] insert 99 at position 0 and show the queue.'
        ),
        'tests': [{'expected_output': '[99, 1, 2, 3]'}],
    },
    "list-08": {
        'title': 'Remove two',
        'condition': (
            'In list numbers = [1, 2, 3, 2] an extra two gets in the way. Remove the first occurrence of 2 and print the list.'
        ),
        'tests': [{'expected_output': '[1, 3, 2]'}],
    },
    "list-09": {
        'title': 'Pop last',
        'condition': (
            'The last part is taken off the conveyor. From list numbers = [5, 6, 7] pop the last element and print it.'
        ),
        'hint': 'For the last element use position -1 or pop without an index.',
        'tests': [{'expected_output': '7'}],
    },
    "list-10": {
        'title': 'How many twos',
        'condition': (
            'At a warehouse they count boxes marked 2. In list [1, 2, 2, 3, 2] print how many times the number 2 appears.'
        ),
        'tests': [{'expected_output': '3'}],
    },
    "list-11": {
        'title': 'Index of «cat»',
        'condition': (
            'At the zoo animals stand in a row: dog, cat, bird. Find the position of cat in list animals and print its index.'
        ),
        'tests': [{'expected_output': '1'}],
    },
    "list-12": {
        'title': 'Sorting',
        'condition': (
            'A teacher arranges grades in ascending order. Sort list [3, 1, 4, 2] and print the result.'
        ),
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-13": {
        'title': 'Reverse',
        'condition': (
            'A parade goes backwards. Reverse list [1, 2, 3] with the reverse block and show the new order.'
        ),
        'tests': [{'expected_output': '[3, 2, 1]'}],
    },
    "list-14": {
        'title': 'Extend list',
        'condition': (
            'Two groups merge: a = [1, 2] and [3, 4]. Extend list a with the second group and print the combined roster.'
        ),
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-15": {
        'title': 'Animal sounds',
        'condition': (
            'The zoo holds a concert: meow, woof, crunch. Store the sounds in a list and in a for loop «play» each — print on a new line.'
        ),
        'tests': [{'expected_output': 'meow\nwoof\ncrunch'}],
    },
    "list-16": {
        'title': 'Sum of five numbers',
        'condition': (
            'Five dice rolls gave numbers 1, 2, 3, 4, 5. Add them in a for loop and print the total score.'
        ),
        'tests': [{'expected_output': '15'}],
    },
    "list-17": {
        'title': 'Clear list',
        'condition': (
            'The to-do list is done — [10, 20] can be erased. Clear it with the clear block and print how many items remain (length).'
        ),
        'tests': [{'expected_output': '0'}],
    },
    "list-18": {
        'title': 'Pop at position 1',
        'condition': (
            'From a stack of books they take the second from the top (position 1). In list [10, 20, 30, 40] pop the element at position 1 and show it.'
        ),
        'tests': [{'expected_output': '20'}],
    },
    "list-19": {
        'title': 'Add a letter',
        'condition': (
            'Alphabet list [a, b] is missing a letter. Ask the user for one letter, append it to the end and print the list.'
        ),
        'tests': [{'stdin': 'c\n', 'expected_output': "['a', 'b', 'c']"},
 {'stdin': 'd\n', 'expected_output': "['a', 'b', 'd']"}],
    },
    "list-20": {
        'title': 'List marathon',
        'condition': (
            'Collect statistics: create an empty list numbers, ask for three integers and append each one. Print: 1) list length 2) sum (for loop) 3) the list itself.'
        ),
        'tests': [{'stdin': '2\n4\n6\n', 'expected_output': '3\n12\n[2, 4, 6]'},
 {'stdin': '1\n1\n1\n', 'expected_output': '3\n3\n[1, 1, 1]'}],
    },
    "list-21": {
        'title': 'Minimum in a list',
        'condition': (
            'Among race results [15, 3, 42, 7] you need the best (minimum) result. Find it in a for loop and print it.'
        ),
        'tests': [{'expected_output': '3'}],
    },
    "list-22": {
        'title': 'Maximum from input',
        'condition': (
            'Judges give scores: ask for n, then n integers, save them in a list and find the maximum score with a for loop.'
        ),
        'tests': [{'stdin': '3\n2\n8\n5\n', 'expected_output': '8'},
 {'stdin': '4\n1\n9\n3\n7\n', 'expected_output': '9'}],
    },
    "list-23": {
        'title': 'Evens only',
        'condition': (
            'From set [1, 2, 3, 4, 5, 6] pick even numbers. Create an empty list evens and in a for loop append only even elements.'
        ),
        'tests': [{'expected_output': '[2, 4, 6]'}],
    },
    "list-24": {
        'title': 'Sum and average',
        'condition': (
            'In a grade book: 4, 5, 3, 5, 4. Print on two lines the total score and the average (sum / len).'
        ),
        'tests': [{'expected_output': '21\n4.2'}],
    },
    "list-25": {
        'title': 'Sort words',
        'condition': (
            'Words on a shelf are mixed up: apple, pear, banana. Sort the list alphabetically and print it.'
        ),
        'tests': [{'expected_output': "['apple', 'banana', 'pear']"}],
    },
    "list-26": {
        'title': 'Merge lists',
        'condition': (
            'Two squads merge: a = [1, 2] and b = [3, 4]. Extend list a with elements from b (extend) and show the combined squad.'
        ),
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-27": {
        'title': 'Double elements',
        'condition': (
            'Each element of list [1, 2, 3] must be duplicated. Create an empty double list and in a for loop append each element twice.'
        ),
        'tests': [{'expected_output': '[1, 1, 2, 2, 3, 3]'}],
    },
    "list-28": {
        'title': 'Two pops in a row',
        'condition': (
            'From stack [10, 20, 30, 40] two top sheets are removed in a row. Call pop() twice and print what remains in the stack.'
        ),
        'tests': [{'expected_output': '[10, 20]'}],
    },
    "list-29": {
        'title': 'Search in a list',
        'condition': (
            'At a pet shop they search for an animal by name. Ask for a word and check list [cat, dog, hamster]: found or not found.'
        ),
        'tests': [{'stdin': 'cat\n', 'expected_output': 'found'},
 {'stdin': 'fish\n', 'expected_output': 'not found'}],
    },
    "list-30": {
        'title': 'Sort and sum',
        'condition': (
            'Enter 4 integers into an empty list, sort them and print on two lines: the sorted list and the sum (for loop).'
        ),
        'tests': [{'stdin': '3\n1\n4\n2\n', 'expected_output': '[1, 2, 3, 4]\n10'}],
    },
    "list-31": {
        'title': 'Reversed list',
        'condition': (
            'Given list numbers = [1, 2, 3, 4]. Create an empty rev and in a for loop collect elements in reverse order (insert each at the beginning). Print rev.'
        ),
        'tests': [{'expected_output': '[4, 3, 2, 1]'}],
    },
    "list-32": {
        'title': 'Greater than five',
        'condition': (
            'From list [2, 8, 5, 11, 3] pick only elements greater than 5. Create an empty list and in a for loop append matching ones. Print the result.'
        ),
        'tests': [{'expected_output': '[8, 11]'}],
    },
    "list-33": {
        'title': 'Access by index',
        'condition': (
            'List nums = [10, 20, 30, 40, 50]. Ask for an index (integer). If the index is from 0 to len − 1 — print the element, otherwise — error.'
        ),
        'tests': [{'stdin': '2\n', 'expected_output': '30'},
 {'stdin': '0\n', 'expected_output': '10'},
 {'stdin': '9\n', 'expected_output': 'error'}],
    },
    "list-34": {
        'title': 'Without edges',
        'condition': (
            'From list [1, 2, 3, 4, 5] remove the first and last element (pop twice — first from the end, then from the beginning) and print the remaining list.'
        ),
        'hint': (
            'After pop() from the end the indices shift — the order of operations matters.'
        ),
        'tests': [{'expected_output': '[2, 3, 4]'}],
    },
    "list-35": {
        'title': 'Even positions',
        'condition': (
            'In list [10, 20, 30, 40, 50] print elements at even positions (0, 2, 4…) — each on a new line, using a for loop and range with step 2.'
        ),
        'tests': [{'expected_output': '10\n30\n50'}],
    },
    "list-fix-01": {
        'title': 'Fix: first element',
        'condition': (
            'Only the first fruit from the display is needed, but the loop prints the whole list. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Only the first fruit is needed — apple.',
        'tests': [{'expected_output': 'apple'}],
    },
    "list-fix-02": {
        'title': 'Fix: append',
        'condition': (
            'The number 4 should end up at the end of the list, but it is inserted at the beginning. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need the append method, not insert at the beginning.',
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-fix-03": {
        'title': 'Fix: sum of a list',
        'condition': (
            'The sum of receipts 10+20+30 is computed with multiplication instead of addition. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'For the sum accumulate the value with +.',
        'tests': [{'expected_output': '60'}],
    },
    "list-fix-04": {
        'title': 'Fix: sorting',
        'condition': (
            'Grades should be arranged in ascending order, but the list is simply reversed. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need the sort method, not reverse.',
        'tests': [{'expected_output': '[1, 2, 3, 4]'}],
    },
    "list-fix-05": {
        'title': 'Fix: length after clear',
        'condition': (
            'After «clearing» the list one element remains — only one item was removed instead of all. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'To make the list empty, use clear.',
        'tests': [{'expected_output': '0'}],
    },
    "list-fix-06": {
        'title': 'Fix: reversed list',
        'condition': (
            'Reversing list [1,2,3,4] did not work — elements are appended at the end in the same order. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'To reverse, insert each element at the beginning.',
        'tests': [{'expected_output': '[4, 3, 2, 1]'}],
    },
    "list-fix-07": {
        'title': 'Fix: greater than five',
        'condition': (
            'The «greater than five» filter only lets through numbers greater than 10 — the threshold is too high. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need numbers strictly greater than 5.',
        'tests': [{'expected_output': '[8, 11]'}],
    },
    "list-fix-08": {
        'title': 'Fix: index',
        'condition': (
            'Access by index always prints error, even for a valid index 2. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'For a valid index you need to print the list element.',
        'tests': [{'stdin': '2\n', 'expected_output': '30'},
 {'stdin': '0\n', 'expected_output': '10'},
 {'stdin': '9\n', 'expected_output': 'error'}],
    },
    "list-fix-09": {
        'title': 'Fix: without edges',
        'condition': (
            'From list [1,2,3,4,5] only the last element was removed — the first one stayed in place. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to remove both the last and the first element.',
        'tests': [{'expected_output': '[2, 3, 4]'}],
    },
    "list-fix-10": {
        'title': 'Fix: even positions',
        'condition': (
            'Elements at positions 0, 2, 4 are needed, but the loop prints all five values. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Loop over indices with step 2.',
        'tests': [{'expected_output': '10\n30\n50'}],
    },
    "numbers-01": {
        'title': 'Candies in a bag',
        'condition': (
            'Masha had 7 candies and a friend gave her 5 more. Add the numbers with an addition block and print how many candies she has now.'
        ),
        'hint': 'Put 7 and 5 in the blocks, then print the answer.',
        'tests': [{'expected_output': '12'}],
    },
    "numbers-02": {
        'title': 'Coins left',
        'condition': (
            'There were 50 coins in a piggy bank. Masha spent 18. Subtract and print how many coins remain.'
        ),
        'tests': [{'expected_output': '32'}],
    },
    "numbers-03": {
        'title': 'Rows in a cinema',
        'condition': (
            'A hall has 8 rows with 12 seats each. Multiply the numbers and print the total number of seats.'
        ),
        'tests': [{'expected_output': '96'}],
    },
    "numbers-04": {
        'title': 'Split among four',
        'condition': (
            'Grandma baked 9 pies and split them equally among 4 grandchildren. Divide 9 / 4 and print the result (a decimal number).'
        ),
        'hint': 'Regular division in Python gives a decimal, e.g. 2.25.',
        'tests': [{'expected_output': '2.25'}],
    },
    "numbers-05": {
        'title': 'Game score',
        'condition': (
            'A player scored 100 points in a level. Save the result in variable score and show it on screen.'
        ),
        'tests': [{'expected_output': '100'}],
    },
    "numbers-06": {
        'title': 'Square of a number',
        'condition': (
            'Compute 6 to the power of 2 (that is 6 × 6) with a power block and print the area of a square with side 6.'
        ),
        'tests': [{'expected_output': '36'}],
    },
    "numbers-07": {
        'title': 'Remainder of division',
        'condition': (
            'Peter has 17 stickers. He gives 5 to each friend equally. How many stickers are left? Use remainder of division for 17 and 5.'
        ),
        'tests': [{'expected_output': '2'}],
    },
    "numbers-08": {
        'title': 'Full boxes',
        'condition': (
            'A warehouse has 47 apples. Each box holds exactly 6. How many full boxes can be packed? Use integer division.'
        ),
        'tests': [{'expected_output': '7'}],
    },
    "numbers-09": {
        'title': 'Two operations in a row',
        'condition': (
            'Compute (10 + 4) × 3: first add, save the result in a variable, then multiply by 3 and print the answer.'
        ),
        'tests': [{'expected_output': '42'}],
    },
    "numbers-10": {
        'title': 'Plus ten',
        'condition': (
            'Ask for a number with an input block, convert it to an integer and add 10. Print the result.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': '15'}, {'stdin': '23\n', 'expected_output': '33'}],
    },
    "numbers-11": {
        'title': 'Sum of two numbers',
        'condition': (
            'Ask for two integers (two input blocks), convert both to int, add them and print the sum.'
        ),
        'tests': [{'stdin': '12\n8\n', 'expected_output': '20'}, {'stdin': '100\n250\n', 'expected_output': '350'}],
    },
    "numbers-12": {
        'title': 'Average grade',
        'condition': (
            'Ask for two test grades (integers), add them and divide by 2. Print the average (may be a decimal).'
        ),
        'tests': [{'stdin': '5\n4\n', 'expected_output': '4.5'}, {'stdin': '3\n3\n', 'expected_output': '3.0'}],
    },
    "numbers-13": {
        'title': 'Ticket cost',
        'condition': (
            'A museum ticket costs 150 dollars. Ask how many tickets a family buys, multiply by 150 and print the total cost.'
        ),
        'tests': [{'stdin': '2\n', 'expected_output': '300'}, {'stdin': '4\n', 'expected_output': '600'}],
    },
    "numbers-14": {
        'title': 'Years passed',
        'condition': 'Ask for birth year (integer). Subtract it from 2026 and print the age.',
        'tests': [{'stdin': '2014\n', 'expected_output': '12'}, {'stdin': '2010\n', 'expected_output': '16'}],
    },
    "numbers-15": {
        'title': 'Room area',
        'condition': (
            'Ask for room length and width in meters (two decimal numbers). Convert to float, multiply and print the area.'
        ),
        'hint': 'For decimals use the «convert to float» block.',
        'tests': [{'stdin': '4\n3\n', 'expected_output': '12.0'}, {'stdin': '2.5\n2\n', 'expected_output': '5.0'}],
    },
    "numbers-16": {
        'title': 'Change at the store',
        'condition': (
            'Ask how many dollars the customer paid (integer). The item costs 73 dollars. Compute change: paid − 73 and print it.'
        ),
        'tests': [{'stdin': '100\n', 'expected_output': '27'}, {'stdin': '200\n', 'expected_output': '127'}],
    },
    "numbers-17": {
        'title': 'Extra balloons',
        'condition': (
            "A pack holds 8 balloons. Ask how many balloons were bought. Find remainder when dividing by 8 — how many don't fit in full packs."
        ),
        'tests': [{'stdin': '25\n', 'expected_output': '1'}, {'stdin': '16\n', 'expected_output': '0'}],
    },
    "numbers-18": {
        'title': 'Power of two',
        'condition': (
            'In computing 2¹⁰ often appears — an old sense of «kilobyte». Compute 2 to the power of 10 and print the result.'
        ),
        'tests': [{'expected_output': '1024'}],
    },
    "numbers-19": {
        'title': 'Perimeter formula',
        'condition': (
            'Rectangle: side a = 7, side b = 3. Perimeter = 2 × (a + b). Save sides in variables, compute and print perimeter.'
        ),
        'tests': [{'expected_output': '20'}],
    },
    "numbers-20": {
        'title': 'Math quest',
        'condition': (
            'Ask for integer n. Compute and print three results on separate lines: 1) n + 5 2) n × n 3) n // 2 (integer half)'
        ),
        'hint': 'Save the entered number in a variable and use it three times.',
        'tests': [{'stdin': '10\n', 'expected_output': '15\n100\n5'},
 {'stdin': '7\n', 'expected_output': '12\n49\n3'}],
    },
    "numbers-21": {
        'title': 'Area and perimeter',
        'condition': (
            'Ask for rectangle length and width (integers). Print on two lines: area and perimeter.'
        ),
        'tests': [{'stdin': '5\n3\n', 'expected_output': '15\n16'},
 {'stdin': '10\n2\n', 'expected_output': '20\n24'}],
    },
    "numbers-22": {
        'title': 'Celsius to Fahrenheit',
        'condition': (
            'Ask for temperature in °C (integer). Convert with formula F = C × 9 / 5 + 32 and print the result.'
        ),
        'tests': [{'stdin': '0\n', 'expected_output': '32.0'},
 {'stdin': '100\n', 'expected_output': '212.0'},
 {'stdin': '20\n', 'expected_output': '68.0'}],
    },
    "numbers-23": {
        'title': 'Quotient and remainder',
        'condition': (
            'Ask for dividend and divisor (integers). Print on two lines: integer part (//) and remainder (%).'
        ),
        'tests': [{'stdin': '47\n6\n', 'expected_output': '7\n5'}, {'stdin': '20\n4\n', 'expected_output': '5\n0'}],
    },
    "numbers-24": {
        'title': 'Three powers',
        'condition': (
            'Ask for integer n. Print on three lines: n², n³ and n⁴ (use the ** operator).'
        ),
        'tests': [{'stdin': '2\n', 'expected_output': '4\n8\n16'}, {'stdin': '3\n', 'expected_output': '9\n27\n81'}],
    },
    "numbers-25": {
        'title': 'Average of three',
        'condition': 'Ask for three integers. Print their arithmetic mean.',
        'tests': [{'stdin': '10\n20\n30\n', 'expected_output': '20.0'},
 {'stdin': '1\n2\n3\n', 'expected_output': '2.0'}],
    },
    "numbers-26": {
        'title': 'Dollars and cents',
        'condition': (
            'Ask for total cents (integer). Print on two lines: full dollars (// 100) and remaining cents (% 100).'
        ),
        'tests': [{'stdin': '257\n', 'expected_output': '2\n57'}, {'stdin': '100\n', 'expected_output': '1\n0'}],
    },
    "numbers-27": {
        'title': 'Table of powers of three',
        'condition': (
            'Build a mini table of powers of 3. Set n = 3 and print on three lines: 3¹, 3² and 3³.'
        ),
        'tests': [{'expected_output': '3\n9\n27'}],
    },
    "numbers-28": {
        'title': 'Difference of cubes',
        'condition': 'Ask for a and b (integers). Print a³ − b³.',
        'tests': [{'stdin': '5\n2\n', 'expected_output': '117'}, {'stdin': '3\n3\n', 'expected_output': '0'}],
    },
    "numbers-29": {
        'title': 'Absolute value',
        'condition': (
            'Ask for integer x. If x < 0, print −x, else print x (absolute value without the abs function).'
        ),
        'hint': 'Use if…else inside print or separate branches.',
        'tests': [{'stdin': '-15\n', 'expected_output': '15'},
 {'stdin': '8\n', 'expected_output': '8'},
 {'stdin': '0\n', 'expected_output': '0'}],
    },
    "numbers-30": {
        'title': 'Complex calculation',
        'condition': (
            'Ask for integer n. Print on three lines: 1) 2×n + 1 2) n² − n 3) n // 3'
        ),
        'tests': [{'stdin': '9\n', 'expected_output': '19\n72\n3'},
 {'stdin': '10\n', 'expected_output': '21\n90\n3'}],
    },
    "numbers-31": {
        'title': 'Taxi ride',
        'condition': (
            'Base fare is 50 dollars, each kilometer costs 15 dollars. Ask for distance in km (integer) and print the trip cost.'
        ),
        'tests': [{'stdin': '3\n', 'expected_output': '95'}, {'stdin': '10\n', 'expected_output': '200'}],
    },
    "numbers-32": {
        'title': 'Hours and minutes',
        'condition': (
            'Ask for total time in minutes (integer). Print on two lines: full hours (// 60) and remaining minutes (% 60).'
        ),
        'tests': [{'stdin': '125\n', 'expected_output': '2\n5'}, {'stdin': '60\n', 'expected_output': '1\n0'}],
    },
    "numbers-33": {
        'title': 'Hundreds digit',
        'condition': (
            'In number 528 the hundreds digit is 5. Set n = 528 and using // and % print the hundreds digit.'
        ),
        'hint': 'First remove tens and ones with integer division by 100.',
        'tests': [{'expected_output': '5'}],
    },
    "numbers-34": {
        'title': 'Store discount',
        'condition': (
            'Ask for item price and discount percent (integers). Print final price after discount: price × (100 − discount) / 100.'
        ),
        'tests': [{'stdin': '200\n10\n', 'expected_output': '180.0'},
 {'stdin': '500\n20\n', 'expected_output': '400.0'}],
    },
    "numbers-35": {
        'title': 'Neighbors of a number',
        'condition': (
            'On a number line neighbors matter. Ask for integer n and print three numbers on separate lines: n − 1, n and n + 1.'
        ),
        'tests': [{'stdin': '10\n', 'expected_output': '9\n10\n11'}, {'stdin': '0\n', 'expected_output': '-1\n0\n1'}],
    },
    "numbers-fix-01": {
        'title': 'Fix: multiplication',
        'condition': (
            'The program counts seats in a hall (8 rows of 12 seats), but addition is used instead of multiplication — the answer is too small. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need multiplication, not addition.',
        'tests': [{'expected_output': '96'}],
    },
    "numbers-fix-02": {
        'title': 'Fix: plus ten',
        'condition': (
            'The entered number should have 10 added, but the program adds text to a number and gets a strange result. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Convert input to an integer before adding.',
        'tests': [{'stdin': '5\n', 'expected_output': '15'}, {'stdin': '23\n', 'expected_output': '33'}],
    },
    "numbers-fix-03": {
        'title': 'Fix: arithmetic mean',
        'condition': (
            'The average of two test scores is wrong — the sum is divided by the wrong count. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The mean of two numbers is sum divided by 2.',
        'tests': [{'stdin': '5\n4\n', 'expected_output': '4.5'}, {'stdin': '3\n3\n', 'expected_output': '3.0'}],
    },
    "numbers-fix-04": {
        'title': 'Fix: square of six',
        'condition': (
            'A square with side 6 should have area 36, but the program outputs 12 — the wrong operation was chosen. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'A square is a number raised to power 2.',
        'tests': [{'expected_output': '36'}],
    },
    "numbers-fix-05": {
        'title': 'Fix: remainder of division',
        'condition': (
            'You need to know how many stickers remain when giving 5 each, but the program counts full «packs», not the remainder. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need remainder (%), not integer division (//).',
        'tests': [{'expected_output': '2'}],
    },
    "numbers-fix-06": {
        'title': 'Fix: taxi',
        'condition': (
            'The taxi meter adds only one kilometer to the base fare, without multiplying the rate by distance. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Payment for kilometers is 15 × number of km.',
        'tests': [{'stdin': '3\n', 'expected_output': '95'}, {'stdin': '10\n', 'expected_output': '200'}],
    },
    "numbers-fix-07": {
        'title': 'Fix: hours and minutes',
        'condition': (
            'Converting minutes to hours gives a decimal number of hours while the remaining minutes are correct. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Hours are the integer part when dividing by 60.',
        'tests': [{'stdin': '125\n', 'expected_output': '2\n5'}, {'stdin': '60\n', 'expected_output': '1\n0'}],
    },
    "numbers-fix-08": {
        'title': 'Fix: hundreds digit',
        'condition': (
            'From number 528 you need digit 5 (hundreds), but the program prints a two-digit remainder. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Hundreds are obtained by dividing by 100 without remainder.',
        'tests': [{'expected_output': '5'}],
    },
    "numbers-fix-09": {
        'title': 'Fix: discount',
        'condition': (
            'The register subtracts discount as a fixed dollar amount, although discount is given in percent. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'A 10% discount on 200 is not 10 dollars.',
        'tests': [{'stdin': '200\n10\n', 'expected_output': '180.0'},
 {'stdin': '500\n20\n', 'expected_output': '400.0'}],
    },
    "numbers-fix-10": {
        'title': 'Fix: neighbors of a number',
        'condition': (
            'Three neighboring numbers on a line are printed in wrong order — n itself ended up on the last line. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The second line should be n itself.',
        'tests': [{'stdin': '10\n', 'expected_output': '9\n10\n11'}, {'stdin': '0\n', 'expected_output': '-1\n0\n1'}],
    },
    "str-01": {
        'title': 'Uppercase',
        'condition': (
            'A store price tag shows the word in lowercase: python. Format the shop window sign — print the word with the uppercase block.'
        ),
        'tests': [{'expected_output': 'PYTHON'}],
    },
    "str-02": {
        'title': 'Lowercase',
        'condition': (
            'A loud ad is written in capitals: HELLO. Convert the text to calm lowercase and show it on screen.'
        ),
        'tests': [{'expected_output': 'hello'}],
    },
    "str-03": {
        'title': 'Strip spaces',
        'condition': (
            'When copying from a document, the word cat picked up extra spaces: «  cat  ». Clean the string with the strip block and print the result.'
        ),
        'tests': [{'expected_output': 'cat'}],
    },
    "str-04": {
        'title': 'Capitalize',
        'condition': (
            'On a café menu the fruit name is lowercase: apple. Format it nicely — with a capital letter at the start.'
        ),
        'tests': [{'expected_output': 'Apple'}],
    },
    "str-05": {
        'title': 'Title case',
        'condition': (
            'A magazine article is called: big green house. Turn the title into title format (title block).'
        ),
        'tests': [{'expected_output': 'Big Green House'}],
    },
    "str-06": {
        'title': 'Is it digits?',
        'condition': (
            'On a form the «Year of birth» field contains 2024. Check with the is digits? block whether the value consists only of digits.'
        ),
        'hint': 'Python prints True or False for logical checks.',
        'tests': [{'expected_output': 'True'}],
    },
    "str-07": {
        'title': 'Letters only?',
        'condition': (
            'The entry code word is abc. Make sure it has no digits or symbols: print the result of the letters only? block.'
        ),
        'tests': [{'expected_output': 'True'}],
    },
    "str-08": {
        'title': 'Find substring',
        'condition': (
            'In the word Friend you need to find where the part end starts. With the find block, print the substring position (expected 3).'
        ),
        'tests': [{'expected_output': '3'}],
    },
    "str-09": {
        'title': 'How many times «n»',
        'condition': (
            'A linguist counts letters in the word banana. Print how many times the letter n appears (count block).'
        ),
        'tests': [{'expected_output': '2'}],
    },
    "str-10": {
        'title': 'Starts with «fro»',
        'condition': (
            'A weather report checks the word frost. Print the result of the check: does it start with fro?'
        ),
        'tests': [{'expected_output': 'True'}],
    },
    "str-11": {
        'title': 'Ends with «ma»',
        'condition': (
            'A librarian looks for books whose titles end with ma. Check the word sigma and print the result of the check.'
        ),
        'tests': [{'expected_output': 'True'}],
    },
    "str-12": {
        'title': 'Replace a letter',
        'condition': (
            'In the word cot there is a typo: replace o with a to get a different word. Make the replacement and print the result.'
        ),
        'tests': [{'expected_output': 'cat'}],
    },
    "str-13": {
        'title': 'Join words',
        'condition': (
            'Build a greeting from two parts: Hello and , world! Join them with the join text block and print the finished phrase.'
        ),
        'tests': [{'expected_output': 'Hello, world!'}],
    },
    "str-14": {
        'title': 'Swap case',
        'condition': (
            "The label PyThOn is written in mixed case. Swap each letter's case with the swap case block and show the result."
        ),
        'tests': [{'expected_output': 'pYtHoN'}],
    },
    "str-15": {
        'title': 'Spaces only?',
        'condition': (
            'A form field is filled with three spaces — empty to the eye, but not to the program. Check with the spaces only? block and print the answer.'
        ),
        'tests': [{'expected_output': 'True'}],
    },
    "str-16": {
        'title': 'Word length',
        'condition': (
            'In a crossword you need the length of the word informatics. Count it with the length block and print the number.'
        ),
        'tests': [{'expected_output': '11'}],
    },
    "str-17": {
        'title': 'Word in uppercase',
        'condition': (
            'The user enters a word for a box stamp. Ask for the word and print it in uppercase.'
        ),
        'tests': [{'stdin': 'cat\n', 'expected_output': 'CAT'}, {'stdin': 'world\n', 'expected_output': 'WORLD'}],
    },
    "str-18": {
        'title': 'Second word',
        'condition': (
            'An address line has two words separated by a space (for example red house). Ask for the line, split with the split by space block and print the second word.'
        ),
        'hint': (
            'After splitting, save the parts in variables or print the needed element.'
        ),
        'tests': [{'stdin': 'red house\n', 'expected_output': 'house'},
 {'stdin': 'big ship\n', 'expected_output': 'ship'}],
    },
    "str-19": {
        'title': 'Spaces to underscores',
        'condition': (
            'Spaces are not allowed in a file name. Ask for a phrase (for example I learn python) and replace spaces with _.'
        ),
        'tests': [{'stdin': 'I learn python\n', 'expected_output': 'I_learn_python'},
 {'stdin': 'good day\n', 'expected_output': 'good_day'}],
    },
    "str-20": {
        'title': 'Three word properties',
        'condition': (
            'A dictionary builds a word card. Ask for a word and print on three lines: 1) length 2) word in uppercase 3) word in lowercase'
        ),
        'tests': [{'stdin': 'Friend\n', 'expected_output': '6\nFRIEND\nfriend'},
 {'stdin': 'Python\n', 'expected_output': '6\nPYTHON\npython'}],
    },
    "str-21": {
        'title': 'Three-letter palindrome',
        'condition': (
            'Mirror game: ask for a three-letter word. If the first and last letters match — palindrome, otherwise — not a palindrome.'
        ),
        'hint': 'Compare the first and third letters of the word.',
        'tests': [{'stdin': 'pop\n', 'expected_output': 'palindrome'},
 {'stdin': 'cat\n', 'expected_output': 'not a palindrome'}],
    },
    "str-22": {
        'title': 'How many words',
        'condition': (
            'An editor counts words in a headline. Ask for a phrase, split by space and print the number of words.'
        ),
        'tests': [{'stdin': 'I learn python\n', 'expected_output': '3'},
 {'stdin': 'good day\n', 'expected_output': '2'}],
    },
    "str-23": {
        'title': 'Article title',
        'condition': (
            'A blogger formats a post title. Ask for a phrase of several words and convert it to title format (title).'
        ),
        'tests': [{'stdin': 'study at school\n', 'expected_output': 'Study At School'},
 {'stdin': 'my first code\n', 'expected_output': 'My First Code'}],
    },
    "str-24": {
        'title': 'First letters',
        'condition': (
            'Build an abbreviation from two words. Ask for a pair of words separated by a space and print their first letters in a row.'
        ),
        'tests': [{'stdin': 'data code\n', 'expected_output': 'dc'},
 {'stdin': 'big world\n', 'expected_output': 'bw'}],
    },
    "str-25": {
        'title': 'String type',
        'condition': (
            'A form filter determines the input type. Ask for a string: if all characters are digits, print all digits; if only letters — letters only; otherwise — mixed.'
        ),
        'hint': 'Use the isdigit and isalpha blocks for the whole string.',
        'tests': [{'stdin': '123\n', 'expected_output': 'all digits'},
 {'stdin': 'python\n', 'expected_output': 'letters only'},
 {'stdin': 'abc123\n', 'expected_output': 'mixed'}],
    },
    "str-26": {
        'title': 'Words with a hyphen',
        'condition': (
            'For a URL two words are joined with a hyphen. Ask for two words separated by a space and print them as word1-word2.'
        ),
        'tests': [{'stdin': 'red house\n', 'expected_output': 'red-house'},
 {'stdin': 'I learn\n', 'expected_output': 'I-learn'}],
    },
    "str-27": {
        'title': 'Strip and uppercase',
        'condition': (
            'The user accidentally entered a word with spaces at the edges. Remove them (strip) and print the word in uppercase.'
        ),
        'tests': [{'stdin': '  python  \n', 'expected_output': 'PYTHON'},
 {'stdin': '  code \n', 'expected_output': 'CODE'}],
    },
    "str-28": {
        'title': 'How many spaces',
        'condition': (
            'A text editor counts spaces in a line. Ask for a phrase and print how many times a space appears.'
        ),
        'tests': [{'stdin': 'I learn python\n', 'expected_output': '2'}, {'stdin': 'one\n', 'expected_output': '0'}],
    },
    "str-29": {
        'title': 'Period to exclamation',
        'condition': (
            'An editor replaces a boring period with an exclamation mark. Ask for a sentence ending with a period and print it with ! at the end.'
        ),
        'tests': [{'stdin': 'Hello.\n', 'expected_output': 'Hello!'},
 {'stdin': 'Hooray.\n', 'expected_output': 'Hooray!'}],
    },
    "str-30": {
        'title': 'Full word analysis',
        'condition': (
            'A linguistic analyzer: ask for a word and print on four lines: 1) length 2) capitalize 3) letters only? (True/False) 4) word in lowercase'
        ),
        'tests': [{'stdin': 'Python\n', 'expected_output': '6\nPython\nTrue\npython'},
 {'stdin': '123\n', 'expected_output': '3\n123\nFalse\n123'}],
    },
    "str-31": {
        'title': 'How many vowels',
        'condition': (
            'Ask for a word. Count in a for loop how many letters from the set aeiou appear in the word, and print the number.'
        ),
        'tests': [{'stdin': 'mama\n', 'expected_output': '2'}, {'stdin': 'animal\n', 'expected_output': '3'}],
    },
    "str-32": {
        'title': 'Full palindrome',
        'condition': (
            'Ask for a word. If it reads the same left to right and right to left — print palindrome, otherwise — not a palindrome.'
        ),
        'hint': 'Compare the string with its reversal s[::-1].',
        'tests': [{'stdin': 'radar\n', 'expected_output': 'palindrome'},
 {'stdin': 'cat\n', 'expected_output': 'not a palindrome'}],
    },
    "str-33": {
        'title': 'In brackets',
        'condition': (
            'Format a word as a label: ask for a word and print it in square brackets — [word].'
        ),
        'tests': [{'stdin': 'python\n', 'expected_output': '[python]'}],
    },
    "str-34": {
        'title': 'Echo double',
        'condition': (
            'Ask for a word and print it repeated twice in a row with no space (the word glued to itself).'
        ),
        'tests': [{'stdin': 'cat\n', 'expected_output': 'catcat'}, {'stdin': 'hi\n', 'expected_output': 'hihi'}],
    },
    "str-35": {
        'title': 'Mirror word',
        'condition': 'Ask for a word and print its letters in reverse order.',
        'tests': [{'stdin': 'cat\n', 'expected_output': 'tac'}, {'stdin': 'Python\n', 'expected_output': 'nohtyP'}],
    },
    "str-fix-01": {
        'title': 'Fix: uppercase',
        'condition': (
            'The price tag python stays lowercase — the method for the opposite case was applied. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need the upper method, not lower.',
        'tests': [{'expected_output': 'PYTHON'}],
    },
    "str-fix-02": {
        'title': 'Fix: strip',
        'condition': (
            'The word cat with spaces at the edges is not cleaned — instead of strip the string is converted to uppercase. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to remove spaces at the edges, not change case.',
        'tests': [{'expected_output': 'cat'}],
    },
    "str-fix-03": {
        'title': 'Fix: find',
        'condition': (
            'Searching for a substring in the word Friend returns position of fri (0), not end (3). A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Check the argument of the find method.',
        'tests': [{'expected_output': '3'}],
    },
    "str-fix-04": {
        'title': 'Fix: replace',
        'condition': (
            'From cot you should get cat, but the wrong letter is replaced. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to replace o, not t.',
        'tests': [{'expected_output': 'cat'}],
    },
    "str-fix-05": {
        'title': 'Fix: input to uppercase',
        'condition': (
            'The entered word for a stamp is printed in lowercase — lower was chosen instead of upper. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'After input you need to convert the string to uppercase.',
        'tests': [{'stdin': 'cat\n', 'expected_output': 'CAT'}, {'stdin': 'world\n', 'expected_output': 'WORLD'}],
    },
    "str-fix-06": {
        'title': 'Fix: vowels',
        'condition': (
            'The counter counts consonants instead of vowels — the condition in the loop is inverted. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to count letters from the vowel set.',
        'tests': [{'stdin': 'mama\n', 'expected_output': '2'}, {'stdin': 'animal\n', 'expected_output': '3'}],
    },
    "str-fix-07": {
        'title': 'Fix: palindrome',
        'condition': (
            'The palindrome check always answers palindrome — comparison with the reversed string is missing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Compare the word with its reversal s[::-1].',
        'tests': [{'stdin': 'radar\n', 'expected_output': 'palindrome'},
 {'stdin': 'cat\n', 'expected_output': 'not a palindrome'}],
    },
    "str-fix-08": {
        'title': 'Fix: in brackets',
        'condition': (
            'Brackets are printed after the word, not around it: cat[] instead of [cat]. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Brackets should wrap the word: [word].',
        'tests': [{'stdin': 'python\n', 'expected_output': '[python]'}],
    },
    "str-fix-09": {
        'title': 'Fix: echo double',
        'condition': (
            'The doubled word is separated by a space — cat cat instead of catcat. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The two copies should be joined with no space.',
        'tests': [{'stdin': 'cat\n', 'expected_output': 'catcat'}, {'stdin': 'hi\n', 'expected_output': 'hihi'}],
    },
    "str-fix-10": {
        'title': 'Fix: mirror word',
        'condition': (
            'The mirror changes letter case but not their order. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need to reverse the order of letters, not change case.',
        'tests': [{'stdin': 'cat\n', 'expected_output': 'tac'}, {'stdin': 'Python\n', 'expected_output': 'nohtyP'}],
    },
    "while-01": {
        'title': 'Count from one to five',
        'condition': (
            'A referee counts runners at a race. Start with number = 1 and in a while loop print the number and increase it by 1 until number is greater than 5. The screen should show 1 … 5.'
        ),
        'hint': 'Loop condition: number ≤ 5. Inside the loop — print and add 1.',
        'tests': [{'expected_output': '1\n2\n3\n4\n5'}],
    },
    "while-02": {
        'title': 'Three times «Ready!»',
        'condition': (
            'Before a competition an athlete answers a command three times. Counter count = 0; while count < 3 — print Ready! and increase count.'
        ),
        'tests': [{'expected_output': 'Ready!\nReady!\nReady!'}],
    },
    "while-03": {
        'title': 'Countdown',
        'condition': (
            'A rocket launches in 5 seconds. Variable t = 5: while t > 0, show t on the display and decrease by 1.'
        ),
        'tests': [{'expected_output': '5\n4\n3\n2\n1'}],
    },
    "while-04": {
        'title': 'Evens up to ten',
        'condition': (
            'Even seat numbers are marked on the track. Start with n = 2 and while n ≤ 10 print the number and add 2.'
        ),
        'tests': [{'expected_output': '2\n4\n6\n8\n10'}],
    },
    "while-05": {
        'title': 'Sum from 1 to 5',
        'condition': (
            'Add the numbers from 1 to 5 in a while loop. Save the result in sum and print 15.'
        ),
        'hint': 'Create a counter and a sum. In the loop add the counter to the sum.',
        'tests': [{'expected_output': '15'}],
    },
    "while-06": {
        'title': 'Times table for ten',
        'condition': 'Variable i = 1. While i ≤ 4, print i × 10 and increase i.',
        'tests': [{'expected_output': '10\n20\n30\n40'}],
    },
    "while-07": {
        'title': 'Five stars',
        'condition': (
            'A hotel rating is five stars. Counter k = 0: while k < 5, print ★ and increase k.'
        ),
        'tests': [{'expected_output': '★\n★\n★\n★\n★'}],
    },
    "while-08": {
        'title': 'Count to entered number',
        'condition': (
            'Ask for an integer n (convert to int). Set i = 1 and in a while loop while i ≤ n print i, increasing i.'
        ),
        'tests': [{'stdin': '4\n', 'expected_output': '1\n2\n3\n4'},
 {'stdin': '6\n', 'expected_output': '1\n2\n3\n4\n5\n6'}],
    },
    "while-09": {
        'title': 'Squares of numbers',
        'condition': 'Variable x = 1. While x ≤ 5, print x × x and increase x.',
        'tests': [{'expected_output': '1\n4\n9\n16\n25'}],
    },
    "while-10": {
        'title': 'Doubling',
        'condition': (
            'Variable number = 1. While number ≤ 32, print it and replace with number × 2.'
        ),
        'tests': [{'expected_output': '1\n2\n4\n8\n16\n32'}],
    },
    "while-11": {
        'title': 'Sum up to ten',
        'condition': 'Using a while loop find the sum of numbers from 1 to 10 and print 55.',
        'tests': [{'expected_output': '55'}],
    },
    "while-12": {
        'title': 'From ten down to six',
        'condition': 'Variable n = 10. While n ≥ 6, print n and decrease by 1.',
        'tests': [{'expected_output': '10\n9\n8\n7\n6'}],
    },
    "while-13": {
        'title': 'Step minus five',
        'condition': (
            'Variable remainder = 20. While remainder > 0, print remainder and subtract 5.'
        ),
        'tests': [{'expected_output': '20\n15\n10\n5'}],
    },
    "while-14": {
        'title': 'Sum from 1 to n',
        'condition': (
            'Ask for an integer n. In a while loop add all numbers from 1 to n and print the sum.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': '15'}, {'stdin': '4\n', 'expected_output': '10'}],
    },
    "while-15": {
        'title': 'Sevens up to thirty-five',
        'condition': 'Variable m = 7. While m ≤ 35, print m and add 7.',
        'tests': [{'expected_output': '7\n14\n21\n28\n35'}],
    },
    "while-16": {
        'title': 'Three greetings',
        'condition': (
            'A robot greets three visitors in a row. Counter c = 0: while c < 3, say hello and increase c.'
        ),
        'tests': [{'expected_output': 'hello\nhello\nhello'}],
    },
    "while-17": {
        'title': 'Powers of three',
        'condition': 'Variable value = 1. While value < 100, print it and multiply by 3.',
        'tests': [{'expected_output': '1\n3\n9\n27\n81'}],
    },
    "while-18": {
        'title': 'How many steps?',
        'condition': (
            'Ask for an integer — how many times to print the word step. Use a while loop with a counter.'
        ),
        'tests': [{'stdin': '3\n', 'expected_output': 'step\nstep\nstep'},
 {'stdin': '2\n', 'expected_output': 'step\nstep'}],
    },
    "while-19": {
        'title': 'Countdown from n',
        'condition': (
            'Ask for an integer n. In a while loop while n > 0 print n and decrease by 1.'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': '5\n4\n3\n2\n1'},
 {'stdin': '3\n', 'expected_output': '3\n2\n1'}],
    },
    "while-20": {
        'title': 'While marathon',
        'condition': (
            'Ask for an integer n. Print on three lines: 1) the number n itself 2) n × 2 3) the sum of numbers from 1 to n (in a while loop)'
        ),
        'hint': 'For the sum create a variable and accumulate it in the loop.',
        'tests': [{'stdin': '4\n', 'expected_output': '4\n8\n10'}, {'stdin': '5\n', 'expected_output': '5\n10\n15'}],
    },
    "while-21": {
        'title': 'How many digits',
        'condition': (
            'Set n = 48291. In a while loop, while n > 0, divide n by 10 and count how many times. Print the number of digits.'
        ),
        'tests': [{'expected_output': '5'}],
    },
    "while-22": {
        'title': 'Sum of digits',
        'condition': (
            'Set n = 123. In a while loop, while n > 0, take the remainder when dividing by 10, add it to the sum, and divide n by 10. Print the sum of digits.'
        ),
        'tests': [{'expected_output': '6'}],
    },
    "while-23": {
        'title': 'Multiplication table',
        'condition': 'Ask for n (integer). In a while loop with i from 1 to 10 print i × n.',
        'tests': [{'stdin': '7\n', 'expected_output': '7\n14\n21\n28\n35\n42\n49\n56\n63\n70'}],
    },
    "while-24": {
        'title': 'Power of two greater than n',
        'condition': (
            'Ask for n (integer). Find the smallest power of two greater than n: p = 1, while p <= n multiply p by 2. Print p.'
        ),
        'tests': [{'stdin': '10\n', 'expected_output': '16'}, {'stdin': '32\n', 'expected_output': '64'}],
    },
    "while-25": {
        'title': 'Collatz sequence',
        'condition': (
            'Set n = 6. While n > 1: print n; if n is even — n = n // 2, else n = n * 3 + 1. Stop when n becomes 1.'
        ),
        'hint': 'We do not print 1 — the loop ends when n equals 1.',
        'tests': [{'expected_output': '6\n3\n10\n5\n16\n8\n4\n2'}],
    },
    "while-26": {
        'title': 'Factorial via while',
        'condition': 'Ask for n (integer ≥ 0). Compute n! in a while loop and print.',
        'tests': [{'stdin': '5\n', 'expected_output': '120'}, {'stdin': '0\n', 'expected_output': '1'}],
    },
    "while-27": {
        'title': 'Sum of squares',
        'condition': (
            'Ask for n. In a while loop find the sum of i² for i from 1 to n and print.'
        ),
        'tests': [{'stdin': '4\n', 'expected_output': '30'}, {'stdin': '3\n', 'expected_output': '14'}],
    },
    "while-28": {
        'title': 'Strip trailing zeros',
        'condition': (
            'Set n = 5000. While n is divisible by 10 without remainder, divide n by 10. Print the resulting number.'
        ),
        'tests': [{'expected_output': '5'}],
    },
    "while-29": {
        'title': 'Smallest divisor',
        'condition': (
            'Ask for n (> 1). With d = 2 in a while loop find the smallest divisor: while n % d != 0 increase d. Print d.'
        ),
        'tests': [{'stdin': '15\n', 'expected_output': '3'}, {'stdin': '7\n', 'expected_output': '7'}],
    },
    "while-30": {
        'title': 'While combo',
        'condition': (
            'Ask for n. Print on two lines: 1) n! (via while) 2) the sum of digits of n (via while)'
        ),
        'tests': [{'stdin': '5\n', 'expected_output': '120\n5'},
 {'stdin': '12\n', 'expected_output': '479001600\n3'}],
    },
    "while-31": {
        'title': 'Reverse number',
        'condition': (
            'Ask for an integer. Reversing digits means building a new number right to left. Do this in a while loop and print the result (for example 12345 → 54321).'
        ),
        'hint': 'At each step: rev = rev * 10 + n % 10, then n = n // 10.',
        'tests': [{'stdin': '12345\n', 'expected_output': '54321'}, {'stdin': '120\n', 'expected_output': '21'}],
    },
    "while-32": {
        'title': 'Sum until zero',
        'condition': (
            'Game: the player enters numbers until they enter 0. Add all entered numbers before zero (zero itself does not count) and print the sum.'
        ),
        'tests': [{'stdin': '3\n5\n2\n0\n', 'expected_output': '10'}, {'stdin': '7\n0\n', 'expected_output': '7'}],
    },
    "while-33": {
        'title': 'Greatest common divisor',
        'condition': (
            "Ask for two integers. Find their GCD using Euclid's algorithm in a while loop (while the second is not 0, replace the pair with (second, remainder of division)) and print the answer."
        ),
        'tests': [{'stdin': '48\n18\n', 'expected_output': '6'}, {'stdin': '17\n13\n', 'expected_output': '1'}],
    },
    "while-34": {
        'title': 'Power in a loop',
        'condition': (
            'Ask for a base and an exponent (integers ≥ 0). Compute the power by multiplication in a while loop and print the result.'
        ),
        'tests': [{'stdin': '2\n10\n', 'expected_output': '1024'},
 {'stdin': '5\n3\n', 'expected_output': '125'},
 {'stdin': '9\n0\n', 'expected_output': '1'}],
    },
    "while-35": {
        'title': 'How many divisors',
        'condition': (
            'Ask for an integer n > 0. In a while loop check divisors from 1 to n and print how many of them divide n without remainder.'
        ),
        'tests': [{'stdin': '12\n', 'expected_output': '6'},
 {'stdin': '7\n', 'expected_output': '2'},
 {'stdin': '1\n', 'expected_output': '1'}],
    },
    "while-fix-01": {
        'title': 'Fix: numbers from 1 to 5',
        'condition': (
            'The race count stops at 4 — the loop ends one step too early. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Check the loop continuation condition.',
        'tests': [{'expected_output': '1\n2\n3\n4\n5'}],
    },
    "while-fix-02": {
        'title': 'Fix: countdown',
        'condition': (
            'The rocket countdown goes on forever — the counter grows instead of decreasing. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'In a countdown the variable should decrease.',
        'tests': [{'expected_output': '5\n4\n3\n2\n1'}],
    },
    "while-fix-03": {
        'title': 'Fix: sum from 1 to 5',
        'condition': (
            'The sum of numbers from 1 to 5 is 9 instead of 15 — the counter in the loop skips numbers. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'On each step the counter should increase by 1.',
        'tests': [{'expected_output': '15'}],
    },
    "while-fix-04": {
        'title': 'Fix: evens up to 10',
        'condition': (
            'The row of even numbers starts at 1 instead of 2 — the starting value of the counter is wrong. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'The first even number in the range is 2.',
        'tests': [{'expected_output': '2\n4\n6\n8\n10'}],
    },
    "while-fix-05": {
        'title': 'Fix: n times «step»',
        'condition': (
            'For n = 3 the word «step» is printed 4 times — the loop makes one extra pass. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'You need exactly n repetitions, not n + 1.',
        'tests': [{'stdin': '3\n', 'expected_output': 'step\nstep\nstep'},
 {'stdin': '2\n', 'expected_output': 'step\nstep'}],
    },
    "while-fix-06": {
        'title': 'Fix: reverse number',
        'condition': (
            'The digits of the number are printed separately in reverse order, but are not combined into one final number. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Accumulate the reversal in a variable instead of printing digits.',
        'tests': [{'stdin': '12345\n', 'expected_output': '54321'}, {'stdin': '120\n', 'expected_output': '21'}],
    },
    "while-fix-07": {
        'title': 'Fix: sum until zero',
        'condition': (
            'For input 3, 5, 2, 0 the sum is 7 instead of 10 — the first entered number is not counted. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Add each non-zero number to the sum before reading the next one.',
        'tests': [{'stdin': '3\n5\n2\n0\n', 'expected_output': '10'}, {'stdin': '7\n0\n', 'expected_output': '7'}],
    },
    "while-fix-08": {
        'title': 'Fix: GCD',
        'condition': (
            "Euclid's algorithm for 48 and 18 gives the wrong answer — the dividend is updated incorrectly in the loop. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it."
        ),
        'hint': 'New a is the old b, new b is the remainder of division.',
        'tests': [{'stdin': '48\n18\n', 'expected_output': '6'}, {'stdin': '17\n13\n', 'expected_output': '1'}],
    },
    "while-fix-09": {
        'title': 'Fix: power in a loop',
        'condition': (
            '2¹⁰ becomes 2048 instead of 1024 — the loop multiplies one time too many. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'For exponent 3 you need exactly 3 multiplications, not 4.',
        'tests': [{'stdin': '2\n10\n', 'expected_output': '1024'},
 {'stdin': '5\n3\n', 'expected_output': '125'},
 {'stdin': '9\n0\n', 'expected_output': '1'}],
    },
    "while-fix-10": {
        'title': 'Fix: divisors',
        'condition': (
            'For the number 12 the program reports 12 divisors — the counter increases for every number, not only for divisors. A program is already assembled in the workspace, but it behaves incorrectly when checked. Find the mistake in the blocks and fix it.'
        ),
        'hint': 'Increase the counter only when n is divisible by d.',
        'tests': [{'stdin': '12\n', 'expected_output': '6'},
 {'stdin': '7\n', 'expected_output': '2'},
 {'stdin': '1\n', 'expected_output': '1'}],
    },
}

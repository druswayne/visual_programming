"""English translations for PyBlocks topic guides."""

from __future__ import annotations

from data import guide_xml as gx

GUIDES_EN: dict[str, dict] = {
    "io": {
        "title": "Input and Output",
        "intro": (
            "Every program communicates with a person: it shows results and can "
            "ask for answers. This is the foundation of interactive programs — "
            "from a calculator to a game. In PyBlocks, output uses the «print» "
            "block and input uses the «input» block."
        ),
        "sections": [
            {
                "title": "Why output matters",
                "text": (
                    "Output is how you show information on the screen: "
                    "text, a number, or the result of a calculation. Without output, "
                    "a program runs silently — you won't see what it did.\n\n"
                    "Real-life examples: an «Order accepted» message, a game score, "
                    "or a calculator answer.\n\n"
                    "You can put text, a number, or a variable into the «print» block."
                ),
                "demo_xml": gx.IO_HELLO_EN,
                "examples": [
                    {
                        "task": "Print the phrase «Welcome!» on the screen.",
                        "result": "Welcome!",
                        "solution_xml": gx.IO_WELCOME_EN,
                    },
                ],
            },
            {
                "title": "What is a variable",
                "text": (
                    "A variable is a named «box» that stores a value: a word, a number, "
                    "or other data. The name lets you use the value again and again.\n\n"
                    "First put a value into a variable with the «set» block, "
                    "then you can print it or use it in other blocks.\n\n"
                    "Variable names should be clear: **city**, **age**, **score**."
                ),
                "demo_xml": gx.IO_VARIABLE_EN,
                "examples": [
                    {
                        "task": (
                            "Store the value «Anna» in variable **name** "
                            "and print it on the screen."
                        ),
                        "result": "Anna",
                        "solution_xml": gx.IO_VARIABLE_EN,
                    },
                ],
            },
            {
                "title": "Why input matters",
                "text": (
                    "Input lets a program receive data from the user: a name, "
                    "an answer to a question, or a chosen number. Then the same "
                    "program can behave differently for different people.\n\n"
                    "The pattern: **ask** → **save the answer in a variable** → "
                    "**use it** (for example, print a greeting).\n\n"
                    "The «input» block can include a prompt — the question text "
                    "the user will see."
                ),
                "demo_xml": gx.IO_GREETING_EN,
                "examples": [
                    {
                        "task": (
                            "Ask for the user's name, save the answer in a variable, "
                            "and print «Hello, <name>!». If the user enters «Masha», "
                            "the screen should show: Hello, Masha!"
                        ),
                        "result": "User enters «Masha» → Hello, Masha!",
                        "solution_xml": gx.IO_GREETING_EN,
                    },
                ],
            },
            {
                "title": "Joining text",
                "text": (
                    "To build a phrase from several parts, use the «join» block. "
                    "It concatenates strings: «Hello» + «, world!» → "
                    "«Hello, world!».\n\n"
                    "You can insert text, variables, and results of other blocks "
                    "into a join."
                ),
                "tip": "The order of parts in «join» matters — it determines "
                "how the final string will look.",
            },
            {
                "title": "How to build a program from blocks",
                "text": (
                    "A program runs from top to bottom — block by block. "
                    "The «Start» and «End» blocks mark the boundaries of the program. "
                    "Between them, commands are placed in the order they should run.\n\n"
                    "On the left is the block palette. Drag the block you need into "
                    "the workspace and connect it to others, like building blocks."
                ),
            },
        ],
    },
    "numbers": {
        "title": "Numbers and Operations",
        "intro": (
            "Computers can calculate quickly. Numbers and arithmetic operations "
            "are needed for calculations: shopping totals, room area, game scores."
        ),
        "sections": [
            {
                "title": "Numbers in programs",
                "text": (
                    "Numbers can be integers (1, 42, −7) or floats (3.14, 2.5). "
                    "You can store them in variables just like text.\n\n"
                    "A number can be printed or used in expressions. "
                    "To read a number from an «input» block, you need conversion — "
                    "see the separate section below."
                ),
            },
            {
                "title": "Basic operations",
                "text": (
                    "Addition (+), subtraction (−), multiplication (×), division (÷) — "
                    "just like in math. There are also:\n\n"
                    "• ** — exponentiation (2³ = 8)\n"
                    "• // — integer division (how many whole times it fits)\n"
                    "• % — remainder (leftover items in a pack)\n\n"
                    "You can print the result right away or save it in a variable."
                ),
                "demo_xml": gx.NUMS_ADD,
                "examples": [
                    {
                        "task": "Calculate and print the sum of 7 and 5.",
                        "result": "12",
                        "solution_xml": gx.NUMS_ADD,
                    },
                ],
            },
            {
                "title": "Expressions and order of operations",
                "text": (
                    "You can combine numbers and operations in one expression. "
                    "Parentheses are evaluated first, then multiplication and "
                    "division, then addition and subtraction — as in algebra.\n\n"
                    "You can print the result right away or save it in a variable."
                ),
                "demo_xml": gx.NUMS_PERIMETER_EN,
                "examples": [
                    {
                        "task": (
                            "A rectangle has sides 7 and 3. Find the perimeter "
                            "using the formula 2 × (a + b) and print the result."
                        ),
                        "result": "20",
                        "solution_xml": gx.NUMS_PERIMETER_EN,
                    },
                ],
            },
            {
                "title": "Numbers from input",
                "text": (
                    "A user's answer from an «input» block first arrives as text. "
                    "To calculate with it, convert it to a number using the "
                    "«integer» or «float» block.\n\n"
                    "This way you can ask for two numbers and find their sum or difference."
                ),
                "demo_xml": gx.NUMS_INPUT_SUM_EN,
                "tip": "Without conversion, «5» + «3» may concatenate as text instead of giving 8.",
                "examples": [
                    {
                        "task": (
                            "Ask for two integers, convert them, and print "
                            "their sum. When the user enters 4 and 6, the screen should show 10."
                        ),
                        "result": "User enters 4 and 6 → 10",
                        "solution_xml": gx.NUMS_INPUT_SUM_EN,
                    },
                ],
            },
            {
                "title": "Remainder of division",
                "text": (
                    "The **%** (remainder) operation is useful for checking evenness: "
                    "if number % 2 = 0, the number is even.\n\n"
                    "It also helps split numbers into «packs»: 17 % 5 = 2 — "
                    "from 17 items in boxes of 5, 2 are left over."
                ),
            },
        ],
    },
    "conditions": {
        "title": "Conditional Statements",
        "intro": (
            "A program can make decisions: perform different actions "
            "depending on the situation — like a traffic light or the rule "
            "«if it rains — take an umbrella». For this you need **logical expressions** "
            "and the «if — else» block."
        ),
        "sections": [
            {
                "title": "Logical expressions",
                "text": (
                    "A logical expression is a question the program answers with "
                    "**true** or **false**. Such questions form conditions in the «if» block.\n\n"
                    "Example questions:\n"
                    "• 15 ≥ 10? → true\n"
                    "• «cat» = «dog»? → false\n"
                    "• is the number even? → depends on the number\n\n"
                    "The result of a comparison or logical operation always "
                    "has a yes/no type (True/False)."
                ),
            },
            {
                "title": "Comparing values",
                "text": (
                    "The **compare** block checks two values and returns "
                    "true or false. Operators:\n\n"
                    "• **=** — equal\n"
                    "• **≠** — not equal\n"
                    "• **>** — greater than\n"
                    "• **<** — less than\n"
                    "• **≥** — greater than or equal\n"
                    "• **≤** — less than or equal\n\n"
                    "You can compare numbers, text, and results of other blocks. "
                    "Text is compared character by character: «abc» < «abd»."
                ),
                "demo_xml": gx.COND_COMPARE_DEMO_EN,
                "examples": [
                    {
                        "task": "Check that 15 ≥ 10 (you can print the result or use it in «if»).",
                        "result": "The condition is true (True)",
                        "solution_xml": gx.COND_COMPARE_DEMO_EN,
                    },
                ],
            },
            {
                "title": "Logical operations: and, or, not",
                "text": (
                    "You can combine several conditions:\n\n"
                    "• **and (AND)** — both conditions must be true. "
                    "«Warm **and** no rain» → go out only when both are true.\n"
                    "• **or (OR)** — one true condition is enough. "
                    "«Weekend **or** vacation» → rest if at least one is true.\n"
                    "• **not (NOT)** — inverts the result. "
                    "«**not** rain» → true when there is no rain.\n\n"
                    "The «and/or» block takes two logical values. "
                    "The «not» block flips one value."
                ),
                "demo_xml": gx.COND_LOGIC_AND_EN,
                "examples": [
                    {
                        "task": (
                            "Build a condition: the number is greater than 10 **and** "
                            "4 equals 2×2. Both comparisons must be true at the same time."
                        ),
                        "result": "True (15 > 10 and 4 = 4)",
                        "solution_xml": gx.COND_LOGIC_AND_EN,
                    },
                ],
            },
            {
                "title": "The «if — else» condition",
                "text": (
                    "The «if — else» block checks a logical expression. "
                    "If **true** — the top branch (DO) runs, "
                    "if **false** — the bottom branch (ELSE).\n\n"
                    "Put a compare or logic block into the condition slot. "
                    "Inside the branches — commands: print, assignment, loops."
                ),
                "demo_xml": gx.COND_IF_ELSE_AGE_EN,
                "examples": [
                    {
                        "task": (
                            "Variable **age** = 15. If age ≥ 18, "
                            "print «allowed», otherwise — «not allowed»."
                        ),
                        "result": "not allowed",
                        "solution_xml": gx.COND_IF_ELSE_AGE_EN,
                    },
                ],
            },
            {
                "title": "Multiple options: «elif»",
                "text": (
                    "When there are more than two options, use a chain: "
                    "if… elif… elif… else.\n\n"
                    "Checks run top to bottom — only the first matching branch runs. "
                    "The rest are skipped.\n\n"
                    "Example: grade 5 → «excellent», 4 → «good», 3 → «satisfactory», "
                    "else → «needs improvement»."
                ),
                "tip": "Check rarer or stricter conditions first.",
            },
            {
                "title": "Practice: evenness and compound conditions",
                "text": (
                    "Evenness is checked via remainder: **n % 2 = 0**.\n\n"
                    "Compound conditions are built from comparisons and «and», «or», «not» blocks. "
                    "First think through the question in words, then assemble the blocks."
                ),
                "examples": [
                    {
                        "task": (
                            "Variable **n** = 8. If n is even (remainder when divided "
                            "by 2 equals 0), print «even», otherwise — «odd»."
                        ),
                        "result": "even",
                        "solution_xml": gx.COND_EVEN_EN,
                    },
                    {
                        "task": (
                            "Variables: **warm** = yes, **rain** = no. "
                            "If warm **and** not rain — print «let's go for a walk!», "
                            "otherwise — «staying home»."
                        ),
                        "result": "let's go for a walk!",
                        "solution_xml": gx.COND_WEATHER_EN,
                    },
                ],
            },
        ],
    },
    "while": {
        "title": "while Loop",
        "intro": (
            "A «while» loop repeats the same actions as long as the condition is true. "
            "Like doing an exercise until you've done it 10 times."
        ),
        "sections": [
            {
                "title": "How a «while» loop works",
                "text": (
                    "1. The condition is checked.\n"
                    "2. If true — blocks inside the loop run.\n"
                    "3. The condition is checked again.\n"
                    "4. When the condition is false — the loop ends and "
                    "the program continues.\n\n"
                    "Important: something inside the loop must change the situation "
                    "(for example, a counter increases), otherwise it never stops."
                ),
                "demo_xml": gx.WHILE_COUNTER,
                "examples": [
                    {
                        "task": (
                            "Print the numbers 1, 2, and 3. Start with i = 1, "
                            "repeat while i ≤ 3: print i, then increase i by 1."
                        ),
                        "result": "1\n2\n3",
                        "solution_xml": gx.WHILE_COUNTER,
                    },
                ],
            },
            {
                "title": "Counter",
                "text": (
                    "Often you create a counter variable:\n"
                    "• **initial value** (for example, 1 or 0)\n"
                    "• **increment** on each step (+1)\n"
                    "• **stop condition** (i ≤ n)\n\n"
                    "This is handy for repeating an action a fixed number of times or "
                    "stepping through numbers in order."
                ),
            },
            {
                "title": "Accumulating a sum",
                "text": (
                    "A «sum» variable starts at 0. On each loop step "
                    "a new value is added to it. At the end you have the total.\n\n"
                    "The same approach works for a product (start with 1)."
                ),
                "demo_xml": gx.WHILE_SUM_EN,
                "examples": [
                    {
                        "task": (
                            "Find the sum of numbers from 1 to 5 using a «while» loop. "
                            "Print the total."
                        ),
                        "result": "15",
                        "solution_xml": gx.WHILE_SUM_EN,
                    },
                ],
            },
            {
                "title": "When to choose while",
                "text": (
                    "A «while» loop fits when you don't know in advance "
                    "how many repetitions you'll need — only the continuation condition matters.\n\n"
                    "If you need exactly N repetitions or to iterate over a ready list — "
                    "a «for» loop is often more convenient."
                ),
            },
        ],
    },
    "for": {
        "title": "for Loop",
        "intro": (
            "A «for» loop iterates over elements of a sequence or "
            "repeats an action a fixed number of times. It's handy when "
            "you know «how many» or «which list» to go through."
        ),
        "sections": [
            {
                "title": "Iterating over a range of numbers",
                "text": (
                    "A «for» block with a range sets start, end, and step. "
                    "On each step the loop variable takes the next number.\n\n"
                    "Example: from 1 to 5 — the variable is 1, 2, 3, 4, 5 in turn."
                ),
                "demo_xml": gx.FOR_RANGE,
                "examples": [
                    {
                        "task": "Print numbers from 1 to 5 using a «for» loop and a range.",
                        "result": "1\n2\n3\n4\n5",
                        "solution_xml": gx.FOR_RANGE,
                    },
                ],
            },
            {
                "title": "Iterating over a list",
                "text": (
                    "You can put a list into the «sequence» slot — "
                    "then the loop variable takes each element's value in turn.\n\n"
                    "Handy for printing all items, summing, or searching."
                ),
            },
            {
                "title": "Accumulating in a «for» loop",
                "text": (
                    "Before the loop, create a variable (sum = 0). "
                    "Update it inside the loop. After the loop, print the result.\n\n"
                    "This is how you compute sums, count matching elements, "
                    "and products."
                ),
                "demo_xml": gx.FOR_SUM_EN,
                "examples": [
                    {
                        "task": (
                            "Using a «for» loop from 1 to 5, find the sum "
                            "of all numbers and print it."
                        ),
                        "result": "15",
                        "solution_xml": gx.FOR_SUM_EN,
                    },
                ],
            },
            {
                "title": "for vs while — what's the difference",
                "text": (
                    "**for** — when the iteration is known: N times, a range, a list.\n\n"
                    "**while** — when you repeat while a condition holds, "
                    "and the number of steps may be unknown in advance.\n\n"
                    "Both loops solve the problem of «not writing the same thing many times»."
                ),
            },
        ],
    },
    "strings": {
        "title": "Strings",
        "intro": (
            "A string is text: a word, phrase, or sentence. "
            "Almost all programs work with text: names, messages, "
            "word search, password checks."
        ),
        "sections": [
            {
                "title": "What is a string",
                "text": (
                    "A string is a sequence of characters: letters, digits, spaces, "
                    "punctuation. You can store a string in a variable, "
                    "print it, or join it with another.\n\n"
                    "Joining strings is called concatenation: «Hello» + «, world!» "
                    "→ «Hello, world!»"
                ),
                "demo_xml": gx.STR_JOIN_EN,
                "examples": [
                    {
                        "task": "Print the string «Hello, world!» by joining «Hello» and «, world!».",
                        "result": "Hello, world!",
                        "solution_xml": gx.STR_JOIN_EN,
                    },
                ],
            },
            {
                "title": "Length and case",
                "text": (
                    "• **Length** — how many characters are in the string (the «length» block)\n"
                    "• **Upper case** — all letters capitalized\n"
                    "• **Lower case** — all letters lowercase\n"
                    "• **Trim spaces** — remove extra spaces at the edges\n\n"
                    "Case matters when comparing: «Python» and «python» are different strings."
                ),
                "demo_xml": gx.STR_UPPER_EN,
                "examples": [
                    {
                        "task": (
                            "Store «python» in a variable and print "
                            "the word in upper case."
                        ),
                        "result": "PYTHON",
                        "solution_xml": gx.STR_UPPER_EN,
                    },
                ],
            },
            {
                "title": "Search and replace",
                "text": (
                    "You can search for a substring (whether a word appears inside a phrase), "
                    "count how many times a character appears, or replace one "
                    "part of text with another.\n\n"
                    "Example: replace spaces with underscores for "
                    "a file name or tag."
                ),
            },
            {
                "title": "String from input",
                "text": (
                    "The «input» block returns a string. You can process it right away: "
                    "change case, trim spaces, or join it with other text."
                ),
                "examples": [
                    {
                        "task": (
                            "Ask the user for a word and print it "
                            "in upper case."
                        ),
                        "result": "User enters «hello» → HELLO",
                        "solution_xml": gx.STR_INPUT_UPPER_EN,
                    },
                ],
            },
            {
                "title": "Splitting into parts",
                "text": (
                    "A string can be split by a delimiter (for example, a space) "
                    "to get a list of words. This helps process phrases "
                    "in parts: take the first word, count words, and so on."
                ),
                "tip": "After splitting you get a list — use blocks from the «Lists» topic.",
            },
        ],
    },
    "lists": {
        "title": "Lists",
        "intro": (
            "A list is an ordered collection of elements under one name. "
            "Like a shopping list or a game's high-score table."
        ),
        "sections": [
            {
                "title": "What is a list",
                "text": (
                    "A list stores several values: numbers, words, or mixed "
                    "data. Each element has an **index (number)** — "
                    "usually starting at zero: first element — 0, second — 1, etc.\n\n"
                    "In «get element» blocks, numbering from 1 is often used "
                    "for beginners' convenience."
                ),
                "demo_xml": gx.LIST_CREATE_EN,
                "examples": [
                    {
                        "task": (
                            "Create the list [«apple», «banana», «pear»] "
                            "and print the first element."
                        ),
                        "result": "apple",
                        "solution_xml": gx.LIST_CREATE_EN,
                    },
                ],
            },
            {
                "title": "Adding and removing",
                "text": (
                    "• **append** — add to the end of the list\n"
                    "• **insert** — at a chosen position\n"
                    "• **remove** — delete a value\n"
                    "• **pop** — take an element and remove it from the list\n\n"
                    "After changing a list, element indices may shift."
                ),
            },
            {
                "title": "Iterating over a list",
                "text": (
                    "A «for each element» loop goes through the whole list. "
                    "Handy for printing all values, finding a sum, or "
                    "selecting matching elements."
                ),
                "demo_xml": gx.LIST_SUM_EN,
                "examples": [
                    {
                        "task": (
                            "Given the list [10, 20, 30]. Find the sum of all elements "
                            "using a «for» loop and print the result."
                        ),
                        "result": "60",
                        "solution_xml": gx.LIST_SUM_EN,
                    },
                ],
            },
            {
                "title": "Sorting and other methods",
                "text": (
                    "• **sort** — order the elements\n"
                    "• **reverse** — reverse the order\n"
                    "• **len** — how many elements\n"
                    "• **count** — how many times a value appears\n"
                    "• **index** — at which position an element is\n\n"
                    "Lists are often combined with loops and conditions for "
                    "filtering and searching."
                ),
            },
        ],
    },
}

"""English translation tables for strings and lists tasks."""

from __future__ import annotations

_FIX_INTRO = (
    "A program is already assembled in the workspace, but it behaves incorrectly when checked. "
    "Find the mistake in the blocks and fix it."
)

# ---------------------------------------------------------------------------
# Strings tasks (str-01 .. str-35)
# ---------------------------------------------------------------------------
STRINGS: dict[str, dict] = {
    "str-01": {
        "title": "Uppercase",
        "condition": (
            "A store price tag shows the word in lowercase: python. "
            "Format the shop window sign — print the word with the uppercase block."
        ),
        "tests": [{"expected_output": "PYTHON"}],
    },
    "str-02": {
        "title": "Lowercase",
        "condition": (
            "A loud ad is written in capitals: HELLO. "
            "Convert the text to calm lowercase and show it on screen."
        ),
        "tests": [{"expected_output": "hello"}],
    },
    "str-03": {
        "title": "Strip spaces",
        "condition": (
            "When copying from a document, the word cat picked up extra spaces: «  cat  ». "
            "Clean the string with the strip block and print the result."
        ),
        "tests": [{"expected_output": "cat"}],
    },
    "str-04": {
        "title": "Capitalize",
        "condition": (
            "On a café menu the fruit name is lowercase: apple. "
            "Format it nicely — with a capital letter at the start."
        ),
        "tests": [{"expected_output": "Apple"}],
    },
    "str-05": {
        "title": "Title case",
        "condition": (
            "A magazine article is called: big green house. "
            "Turn the title into title format (title block)."
        ),
        "tests": [{"expected_output": "Big Green House"}],
    },
    "str-06": {
        "title": "Is it digits?",
        "condition": (
            "On a form the «Year of birth» field contains 2024. "
            "Check with the is digits? block whether the value consists only of digits."
        ),
        "tests": [{"expected_output": "True"}],
        "hint": "Python prints True or False for logical checks.",
    },
    "str-07": {
        "title": "Letters only?",
        "condition": (
            "The entry code word is abc. "
            "Make sure it has no digits or symbols: print the result of the letters only? block."
        ),
        "tests": [{"expected_output": "True"}],
    },
    "str-08": {
        "title": "Find substring",
        "condition": (
            "In the word Friend you need to find where the part end starts. "
            "With the find block, print the substring position (expected 3)."
        ),
        "tests": [{"expected_output": "3"}],
    },
    "str-09": {
        "title": "How many times «n»",
        "condition": (
            "A linguist counts letters in the word banana. "
            "Print how many times the letter n appears (count block)."
        ),
        "tests": [{"expected_output": "2"}],
    },
    "str-10": {
        "title": "Starts with «fro»",
        "condition": (
            "A weather report checks the word frost. "
            "Print the result of the check: does it start with fro?"
        ),
        "tests": [{"expected_output": "True"}],
    },
    "str-11": {
        "title": "Ends with «ma»",
        "condition": (
            "A librarian looks for books whose titles end with ma. "
            "Check the word sigma and print the result of the check."
        ),
        "tests": [{"expected_output": "True"}],
    },
    "str-12": {
        "title": "Replace a letter",
        "condition": (
            "In the word cot there is a typo: replace o with a to get a different word. "
            "Make the replacement and print the result."
        ),
        "tests": [{"expected_output": "cat"}],
    },
    "str-13": {
        "title": "Join words",
        "condition": (
            "Build a greeting from two parts: Hello and , world! "
            "Join them with the join text block and print the finished phrase."
        ),
        "tests": [{"expected_output": "Hello, world!"}],
    },
    "str-14": {
        "title": "Swap case",
        "condition": (
            "The label PyThOn is written in mixed case. "
            "Swap each letter's case with the swap case block and show the result."
        ),
        "tests": [{"expected_output": "pYtHoN"}],
    },
    "str-15": {
        "title": "Spaces only?",
        "condition": (
            "A form field is filled with three spaces — empty to the eye, but not to the program. "
            "Check with the spaces only? block and print the answer."
        ),
        "tests": [{"expected_output": "True"}],
    },
    "str-16": {
        "title": "Word length",
        "condition": (
            "In a crossword you need the length of the word informatics. "
            "Count it with the length block and print the number."
        ),
        "tests": [{"expected_output": "11"}],
    },
    "str-17": {
        "title": "Word in uppercase",
        "condition": (
            "The user enters a word for a box stamp. "
            "Ask for the word and print it in uppercase."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "CAT"},
            {"stdin": "world\n", "expected_output": "WORLD"},
        ],
    },
    "str-18": {
        "title": "Second word",
        "condition": (
            "An address line has two words separated by a space (for example red house). "
            "Ask for the line, split with the split by space block and print the second word."
        ),
        "tests": [
            {"stdin": "red house\n", "expected_output": "house"},
            {"stdin": "big ship\n", "expected_output": "ship"},
        ],
        "hint": "After splitting, save the parts in variables or print the needed element.",
    },
    "str-19": {
        "title": "Spaces to underscores",
        "condition": (
            "Spaces are not allowed in a file name. "
            "Ask for a phrase (for example I learn python) and replace spaces with _."
        ),
        "tests": [
            {"stdin": "I learn python\n", "expected_output": "I_learn_python"},
            {"stdin": "good day\n", "expected_output": "good_day"},
        ],
    },
    "str-20": {
        "title": "Three word properties",
        "condition": (
            "A dictionary builds a word card. Ask for a word and print on three lines: "
            "1) length "
            "2) word in uppercase "
            "3) word in lowercase"
        ),
        "tests": [
            {"stdin": "Friend\n", "expected_output": "6\nFRIEND\nfriend"},
            {"stdin": "Python\n", "expected_output": "6\nPYTHON\npython"},
        ],
    },
    "str-21": {
        "title": "Three-letter palindrome",
        "condition": (
            "Mirror game: ask for a three-letter word. "
            "If the first and last letters match — palindrome, otherwise — not a palindrome."
        ),
        "tests": [
            {"stdin": "pop\n", "expected_output": "palindrome"},
            {"stdin": "cat\n", "expected_output": "not a palindrome"},
        ],
        "hint": "Compare the first and third letters of the word.",
    },
    "str-22": {
        "title": "How many words",
        "condition": (
            "An editor counts words in a headline. "
            "Ask for a phrase, split by space and print the number of words."
        ),
        "tests": [
            {"stdin": "I learn python\n", "expected_output": "3"},
            {"stdin": "good day\n", "expected_output": "2"},
        ],
    },
    "str-23": {
        "title": "Article title",
        "condition": (
            "A blogger formats a post title. "
            "Ask for a phrase of several words and convert it to title format (title)."
        ),
        "tests": [
            {"stdin": "study at school\n", "expected_output": "Study At School"},
            {"stdin": "my first code\n", "expected_output": "My First Code"},
        ],
    },
    "str-24": {
        "title": "First letters",
        "condition": (
            "Build an abbreviation from two words. "
            "Ask for a pair of words separated by a space and print their first letters in a row."
        ),
        "tests": [
            {"stdin": "data code\n", "expected_output": "dc"},
            {"stdin": "big world\n", "expected_output": "bw"},
        ],
    },
    "str-25": {
        "title": "String type",
        "condition": (
            "A form filter determines the input type. Ask for a string: "
            "if all characters are digits, print all digits; "
            "if only letters — letters only; otherwise — mixed."
        ),
        "tests": [
            {"stdin": "123\n", "expected_output": "all digits"},
            {"stdin": "python\n", "expected_output": "letters only"},
            {"stdin": "abc123\n", "expected_output": "mixed"},
        ],
        "hint": "Use the isdigit and isalpha blocks for the whole string.",
    },
    "str-26": {
        "title": "Words with a hyphen",
        "condition": (
            "For a URL two words are joined with a hyphen. "
            "Ask for two words separated by a space and print them as word1-word2."
        ),
        "tests": [
            {"stdin": "red house\n", "expected_output": "red-house"},
            {"stdin": "I learn\n", "expected_output": "I-learn"},
        ],
    },
    "str-27": {
        "title": "Strip and uppercase",
        "condition": (
            "The user accidentally entered a word with spaces at the edges. "
            "Remove them (strip) and print the word in uppercase."
        ),
        "tests": [
            {"stdin": "  python  \n", "expected_output": "PYTHON"},
            {"stdin": "  code \n", "expected_output": "CODE"},
        ],
    },
    "str-28": {
        "title": "How many spaces",
        "condition": (
            "A text editor counts spaces in a line. "
            "Ask for a phrase and print how many times a space appears."
        ),
        "tests": [
            {"stdin": "I learn python\n", "expected_output": "2"},
            {"stdin": "one\n", "expected_output": "0"},
        ],
    },
    "str-29": {
        "title": "Period to exclamation",
        "condition": (
            "An editor replaces a boring period with an exclamation mark. "
            "Ask for a sentence ending with a period and print it with ! at the end."
        ),
        "tests": [
            {"stdin": "Hello.\n", "expected_output": "Hello!"},
            {"stdin": "Hooray.\n", "expected_output": "Hooray!"},
        ],
    },
    "str-30": {
        "title": "Full word analysis",
        "condition": (
            "A linguistic analyzer: ask for a word and print on four lines: "
            "1) length "
            "2) capitalize "
            "3) letters only? (True/False) "
            "4) word in lowercase"
        ),
        "tests": [
            {"stdin": "Python\n", "expected_output": "6\nPython\nTrue\npython"},
            {"stdin": "123\n", "expected_output": "3\n123\nFalse\n123"},
        ],
    },
    "str-31": {
        "title": "How many vowels",
        "condition": (
            "Ask for a word. Count in a for loop how many letters from the set "
            "aeiou appear in the word, and print the number."
        ),
        "tests": [
            {"stdin": "mama\n", "expected_output": "2"},
            {"stdin": "animal\n", "expected_output": "3"},
        ],
    },
    "str-32": {
        "title": "Full palindrome",
        "condition": (
            "Ask for a word. If it reads the same left to right and right to left — "
            "print palindrome, otherwise — not a palindrome."
        ),
        "tests": [
            {"stdin": "radar\n", "expected_output": "palindrome"},
            {"stdin": "cat\n", "expected_output": "not a palindrome"},
        ],
        "hint": "Compare the string with its reversal s[::-1].",
    },
    "str-33": {
        "title": "In brackets",
        "condition": (
            "Format a word as a label: ask for a word and print it in square brackets — "
            "[word]."
        ),
        "tests": [{"stdin": "python\n", "expected_output": "[python]"}],
    },
    "str-34": {
        "title": "Echo double",
        "condition": (
            "Ask for a word and print it repeated twice in a row with no space "
            "(the word glued to itself)."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "catcat"},
            {"stdin": "hi\n", "expected_output": "hihi"},
        ],
    },
    "str-35": {
        "title": "Mirror word",
        "condition": (
            "Ask for a word and print its letters in reverse order."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "tac"},
            {"stdin": "Python\n", "expected_output": "nohtyP"},
        ],
    },
    "str-36": {
        "title": "Word edges",
        "condition": (
            "Ask for a non-empty word. Print its first and last letters on two lines."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "c\nt"},
            {"stdin": "Python\n", "expected_output": "P\nn"},
            {"stdin": "I\n", "expected_output": "I\nI"},
        ],
        "hint": "The first letter is s[0], the last is s[-1] or s[len(s) - 1].",
    },
    "str-37": {
        "title": "No spaces",
        "condition": (
            "Ask for a phrase and print it with all spaces removed."
        ),
        "tests": [
            {"stdin": "I learn python\n", "expected_output": "Ilearnpython"},
            {"stdin": "one\n", "expected_output": "one"},
        ],
        "hint": "Replace a space with an empty string using replace.",
    },
    "str-38": {
        "title": "Same edges",
        "condition": (
            "Ask for a non-empty word. If the first and last letters match — "
            "print yes, otherwise — no."
        ),
        "tests": [
            {"stdin": "anna\n", "expected_output": "yes"},
            {"stdin": "cat\n", "expected_output": "no"},
            {"stdin": "A\n", "expected_output": "yes"},
        ],
    },
    "str-39": {
        "title": "Double the letters",
        "condition": (
            "Ask for a word. Build a new string where each letter is repeated twice "
            "and print it (cat → ccaatt)."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "ccaatt"},
            {"stdin": "ab\n", "expected_output": "aabb"},
        ],
        "hint": "In a for loop append the character to the result twice.",
    },
    "str-40": {
        "title": "Without vowels",
        "condition": (
            "Ask for a lowercase word. Remove all vowels from the set aeiou "
            "and print the remaining letters joined together. If there were no vowels — print the word as is."
        ),
        "tests": [
            {"stdin": "banana\n", "expected_output": "bnn"},
            {"stdin": "rhythm\n", "expected_output": "rhythm"},
            {"stdin": "test\n", "expected_output": "tst"},
        ],
        "hint": "In a loop add to the result only letters that are not in the vowel set.",
    },
    "str-41": {
        "title": "How many consonants",
        "condition": (
            "Ask for a lowercase word. Count the letters that are not in the vowel set "
            "aeiou and print that number."
        ),
        "tests": [
            {"stdin": "mama\n", "expected_output": "2"},
            {"stdin": "cat\n", "expected_output": "2"},
            {"stdin": "au\n", "expected_output": "0"},
        ],
    },
    "str-42": {
        "title": "Swap the edges",
        "condition": (
            "Ask for a non-empty word. Swap the first and last letters and print the result. "
            "If there is only one letter — print it as is."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "tac"},
            {"stdin": "ab\n", "expected_output": "ba"},
            {"stdin": "I\n", "expected_output": "I"},
        ],
        "hint": "Build s[-1] + the middle + s[0]; for length 1 the middle is empty.",
    },
    "str-43": {
        "title": "The longer word",
        "condition": (
            "Ask for two words. Print the one that has more letters. "
            "If the lengths are equal — print the first."
        ),
        "tests": [
            {"stdin": "cat\nelephant\n", "expected_output": "elephant"},
            {"stdin": "yes\nno\n", "expected_output": "yes"},
            {"stdin": "sun\ndog\n", "expected_output": "sun"},
        ],
    },
    "str-44": {
        "title": "Three-word abbreviation",
        "condition": (
            "Ask for three words separated by spaces on one line. Print the abbreviation: "
            "the first letters joined together, with no spaces."
        ),
        "tests": [
            {"stdin": "red orange tart\n", "expected_output": "rot"},
            {"stdin": "Big Green House\n", "expected_output": "BGH"},
        ],
        "hint": "Split the string by space and take [0] of each part.",
    },
    "str-45": {
        "title": "Vowels to stars",
        "condition": (
            "Ask for a lowercase word. Replace each vowel from the set "
            "aeiou with the * character and print the result."
        ),
        "tests": [
            {"stdin": "mama\n", "expected_output": "m*m*"},
            {"stdin": "rhythm\n", "expected_output": "rhythm"},
            {"stdin": "elm\n", "expected_output": "*lm"},
        ],
    },
    "str-46": {
        "title": "Letters in a column",
        "condition": "Ask for a word and print each letter on a separate line.",
        "tests": [
            {"stdin": "cat\n", "expected_output": "c\na\nt"},
            {"stdin": "I\n", "expected_output": "I"},
        ],
    },
    "str-47": {
        "title": "Palindrome ignoring case",
        "condition": (
            "Ask for a word. Convert it to lowercase and check whether it is a palindrome. "
            "Print palindrome or not palindrome."
        ),
        "tests": [
            {"stdin": "Topot\n", "expected_output": "palindrome"},
            {"stdin": "Cat\n", "expected_output": "not palindrome"},
            {"stdin": "A\n", "expected_output": "palindrome"},
        ],
    },
    "str-48": {
        "title": "Words longer than three",
        "condition": (
            "Ask for a phrase of several words. Count how many words are longer than 3 letters and print the number."
        ),
        "tests": [
            {"stdin": "I love python\n", "expected_output": "2"},
            {"stdin": "yes no\n", "expected_output": "0"},
            {"stdin": "I am coding\n", "expected_output": "1"},
        ],
        "hint": "Split by space and in a loop check the length of each word.",
    },
    "str-49": {
        "title": "The last word",
        "condition": (
            "Ask for a phrase of several words separated by spaces and print only the last word."
        ),
        "tests": [
            {"stdin": "red house by river\n", "expected_output": "river"},
            {"stdin": "one\n", "expected_output": "one"},
        ],
    },
    "str-50": {
        "title": "The middle of a word",
        "condition": (
            "Ask for a non-empty word. If the length is odd — print the middle letter. "
            "If even — the two middle letters joined together."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "a"},
            {"stdin": "cats\n", "expected_output": "at"},
            {"stdin": "I\n", "expected_output": "I"},
        ],
        "hint": "For an odd length the middle index is len // 2.",
    },
}

# Strings fix tasks
STRINGS_FIX: dict[str, dict] = {
    "str-fix-01": {
        "title": "Fix: uppercase",
        "condition": (
            "The price tag python stays lowercase — "
            "the method for the opposite case was applied. " + _FIX_INTRO
        ),
        "hint": "You need the upper method, not lower.",
        "tests": [{"expected_output": "PYTHON"}],
    },
    "str-fix-02": {
        "title": "Fix: strip",
        "condition": (
            "The word cat with spaces at the edges is not cleaned — "
            "instead of strip the string is converted to uppercase. " + _FIX_INTRO
        ),
        "hint": "You need to remove spaces at the edges, not change case.",
        "tests": [{"expected_output": "cat"}],
    },
    "str-fix-03": {
        "title": "Fix: find",
        "condition": (
            "Searching for a substring in the word Friend returns position of fri (0), "
            "not end (3). " + _FIX_INTRO
        ),
        "hint": "Check the argument of the find method.",
        "tests": [{"expected_output": "3"}],
    },
    "str-fix-04": {
        "title": "Fix: replace",
        "condition": (
            "From cot you should get cat, "
            "but the wrong letter is replaced. " + _FIX_INTRO
        ),
        "hint": "You need to replace o, not t.",
        "tests": [{"expected_output": "cat"}],
    },
    "str-fix-05": {
        "title": "Fix: input to uppercase",
        "condition": (
            "The entered word for a stamp is printed in lowercase — "
            "lower was chosen instead of upper. " + _FIX_INTRO
        ),
        "hint": "After input you need to convert the string to uppercase.",
        "tests": [
            {"stdin": "cat\n", "expected_output": "CAT"},
            {"stdin": "world\n", "expected_output": "WORLD"},
        ],
    },
    "str-fix-06": {
        "title": "Fix: vowels",
        "condition": (
            "The counter counts consonants instead of vowels — "
            "the condition in the loop is inverted. " + _FIX_INTRO
        ),
        "hint": "You need to count letters from the vowel set.",
        "tests": [
            {"stdin": "mama\n", "expected_output": "2"},
            {"stdin": "animal\n", "expected_output": "3"},
        ],
    },
    "str-fix-07": {
        "title": "Fix: palindrome",
        "condition": (
            "The palindrome check always answers palindrome — "
            "comparison with the reversed string is missing. " + _FIX_INTRO
        ),
        "hint": "Compare the word with its reversal s[::-1].",
        "tests": [
            {"stdin": "radar\n", "expected_output": "palindrome"},
            {"stdin": "cat\n", "expected_output": "not a palindrome"},
        ],
    },
    "str-fix-08": {
        "title": "Fix: in brackets",
        "condition": (
            "Brackets are printed after the word, not around it: cat[] "
            "instead of [cat]. " + _FIX_INTRO
        ),
        "hint": "Brackets should wrap the word: [word].",
        "tests": [{"stdin": "python\n", "expected_output": "[python]"}],
    },
    "str-fix-09": {
        "title": "Fix: echo double",
        "condition": (
            "The doubled word is separated by a space — cat cat "
            "instead of catcat. " + _FIX_INTRO
        ),
        "hint": "The two copies should be joined with no space.",
        "tests": [
            {"stdin": "cat\n", "expected_output": "catcat"},
            {"stdin": "hi\n", "expected_output": "hihi"},
        ],
    },
    "str-fix-10": {
        "title": "Fix: mirror word",
        "condition": (
            "The mirror changes letter case but not their order. " + _FIX_INTRO
        ),
        "hint": "You need to reverse the order of letters, not change case.",
        "tests": [
            {"stdin": "cat\n", "expected_output": "tac"},
            {"stdin": "Python\n", "expected_output": "nohtyP"},
        ],
    },
}

# ---------------------------------------------------------------------------
# Lists tasks (list-01 .. list-35)
# ---------------------------------------------------------------------------
LISTS: dict[str, dict] = {
    "list-01": {
        "title": "First fruit",
        "condition": (
            "On a store display the fruits stand in a row: apple, banana, pear. "
            "Store them in list fruits and show only the first fruit."
        ),
        "tests": [{"expected_output": "apple"}],
        "hint": "The first element — in the get element block choose «from 1».",
    },
    "list-02": {
        "title": "How many numbers",
        "condition": (
            "A grade book records scores: 5, 10, 15. "
            "Save them in list numbers and print how many entries are in the book."
        ),
        "tests": [{"expected_output": "3"}],
    },
    "list-03": {
        "title": "Add four",
        "condition": (
            "To the row of numbers 1, 2, 3 a new participant arrived — 4. "
            "Add it to the end of list numbers and show the updated row."
        ),
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-04": {
        "title": "Empty list",
        "condition": (
            "Start with an empty list of alphabet letters. "
            "Add a and b to it in order, then print the list."
        ),
        "tests": [{"expected_output": "['a', 'b']"}],
    },
    "list-05": {
        "title": "Loop over a list",
        "condition": (
            "A scoreboard shows numbers 1, 2, 3, 4, 5. "
            "Save them in a list and in a for loop print each number on a new line."
        ),
        "tests": [{"expected_output": "1\n2\n3\n4\n5"}],
    },
    "list-06": {
        "title": "Sum of a list",
        "condition": (
            "A cashier adds receipts: 10, 20 and 30 dollars. "
            "Write the amounts in a list and in a for loop find the total — 60."
        ),
        "tests": [{"expected_output": "60"}],
    },
    "list-07": {
        "title": "Insert 99",
        "condition": (
            "An urgent client with ticket 99 joined the front of the queue. "
            "In list numbers = [1, 2, 3] insert 99 at position 0 and show the queue."
        ),
        "tests": [{"expected_output": "[99, 1, 2, 3]"}],
    },
    "list-08": {
        "title": "Remove two",
        "condition": (
            "In list numbers = [1, 2, 3, 2] an extra two gets in the way. "
            "Remove the first occurrence of 2 and print the list."
        ),
        "tests": [{"expected_output": "[1, 3, 2]"}],
    },
    "list-09": {
        "title": "Pop last",
        "condition": (
            "The last part is taken off the conveyor. "
            "From list numbers = [5, 6, 7] pop the last element and print it."
        ),
        "tests": [{"expected_output": "7"}],
        "hint": "For the last element use position -1 or pop without an index.",
    },
    "list-10": {
        "title": "How many twos",
        "condition": (
            "At a warehouse they count boxes marked 2. "
            "In list [1, 2, 2, 3, 2] print how many times the number 2 appears."
        ),
        "tests": [{"expected_output": "3"}],
    },
    "list-11": {
        "title": "Index of «cat»",
        "condition": (
            "At the zoo animals stand in a row: dog, cat, bird. "
            "Find the position of cat in list animals and print its index."
        ),
        "tests": [{"expected_output": "1"}],
    },
    "list-12": {
        "title": "Sorting",
        "condition": (
            "A teacher arranges grades in ascending order. "
            "Sort list [3, 1, 4, 2] and print the result."
        ),
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-13": {
        "title": "Reverse",
        "condition": (
            "A parade goes backwards. "
            "Reverse list [1, 2, 3] with the reverse block and show the new order."
        ),
        "tests": [{"expected_output": "[3, 2, 1]"}],
    },
    "list-14": {
        "title": "Extend list",
        "condition": (
            "Two groups merge: a = [1, 2] and [3, 4]. "
            "Extend list a with the second group and print the combined roster."
        ),
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-15": {
        "title": "Animal sounds",
        "condition": (
            "The zoo holds a concert: meow, woof, crunch. "
            "Store the sounds in a list and in a for loop «play» each — print on a new line."
        ),
        "tests": [{"expected_output": "meow\nwoof\ncrunch"}],
    },
    "list-16": {
        "title": "Sum of five numbers",
        "condition": (
            "Five dice rolls gave numbers 1, 2, 3, 4, 5. "
            "Add them in a for loop and print the total score."
        ),
        "tests": [{"expected_output": "15"}],
    },
    "list-17": {
        "title": "Clear list",
        "condition": (
            "The to-do list is done — [10, 20] can be erased. "
            "Clear it with the clear block and print how many items remain (length)."
        ),
        "tests": [{"expected_output": "0"}],
    },
    "list-18": {
        "title": "Pop at position 1",
        "condition": (
            "From a stack of books they take the second from the top (position 1). "
            "In list [10, 20, 30, 40] pop the element at position 1 and show it."
        ),
        "tests": [{"expected_output": "20"}],
    },
    "list-19": {
        "title": "Add a letter",
        "condition": (
            "Alphabet list [a, b] is missing a letter. "
            "Ask the user for one letter, append it to the end and print the list."
        ),
        "tests": [
            {"stdin": "c\n", "expected_output": "['a', 'b', 'c']"},
            {"stdin": "d\n", "expected_output": "['a', 'b', 'd']"},
        ],
    },
    "list-20": {
        "title": "List marathon",
        "condition": (
            "Collect statistics: create an empty list numbers, "
            "ask for three integers and append each one. "
            "Print: 1) list length 2) sum (for loop) 3) the list itself."
        ),
        "tests": [
            {"stdin": "2\n4\n6\n", "expected_output": "3\n12\n[2, 4, 6]"},
            {"stdin": "1\n1\n1\n", "expected_output": "3\n3\n[1, 1, 1]"},
        ],
    },
    "list-21": {
        "title": "Minimum in a list",
        "condition": (
            "Among race results [15, 3, 42, 7] you need the best (minimum) result. "
            "Find it in a for loop and print it."
        ),
        "tests": [{"expected_output": "3"}],
    },
    "list-22": {
        "title": "Maximum from input",
        "condition": (
            "Judges give scores: ask for n, then n integers, "
            "save them in a list and find the maximum score with a for loop."
        ),
        "tests": [
            {"stdin": "3\n2\n8\n5\n", "expected_output": "8"},
            {"stdin": "4\n1\n9\n3\n7\n", "expected_output": "9"},
        ],
    },
    "list-23": {
        "title": "Evens only",
        "condition": (
            "From set [1, 2, 3, 4, 5, 6] pick even numbers. "
            "Create an empty list evens and in a for loop append only even elements."
        ),
        "tests": [{"expected_output": "[2, 4, 6]"}],
    },
    "list-24": {
        "title": "Sum and average",
        "condition": (
            "In a grade book: 4, 5, 3, 5, 4. "
            "Print on two lines the total score and the average (sum / len)."
        ),
        "tests": [{"expected_output": "21\n4.2"}],
    },
    "list-25": {
        "title": "Sort words",
        "condition": (
            "Words on a shelf are mixed up: apple, pear, banana. "
            "Sort the list alphabetically and print it."
        ),
        "tests": [{"expected_output": "['apple', 'banana', 'pear']"}],
    },
    "list-26": {
        "title": "Merge lists",
        "condition": (
            "Two squads merge: a = [1, 2] and b = [3, 4]. "
            "Extend list a with elements from b (extend) and show the combined squad."
        ),
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-27": {
        "title": "Double elements",
        "condition": (
            "Each element of list [1, 2, 3] must be duplicated. "
            "Create an empty double list and in a for loop append each element twice."
        ),
        "tests": [{"expected_output": "[1, 1, 2, 2, 3, 3]"}],
    },
    "list-28": {
        "title": "Two pops in a row",
        "condition": (
            "From stack [10, 20, 30, 40] two top sheets are removed in a row. "
            "Call pop() twice and print what remains in the stack."
        ),
        "tests": [{"expected_output": "[10, 20]"}],
    },
    "list-29": {
        "title": "Search in a list",
        "condition": (
            "At a pet shop they search for an animal by name. "
            "Ask for a word and check list [cat, dog, hamster]: "
            "found or not found."
        ),
        "tests": [
            {"stdin": "cat\n", "expected_output": "found"},
            {"stdin": "fish\n", "expected_output": "not found"},
        ],
    },
    "list-30": {
        "title": "Sort and sum",
        "condition": (
            "Enter 4 integers into an empty list, sort them "
            "and print on two lines: the sorted list and the sum (for loop)."
        ),
        "tests": [{"stdin": "3\n1\n4\n2\n", "expected_output": "[1, 2, 3, 4]\n10"}],
    },
    "list-31": {
        "title": "Reversed list",
        "condition": (
            "Given list numbers = [1, 2, 3, 4]. Create an empty rev and in a for loop "
            "collect elements in reverse order (insert each at the beginning). "
            "Print rev."
        ),
        "tests": [{"expected_output": "[4, 3, 2, 1]"}],
    },
    "list-32": {
        "title": "Greater than five",
        "condition": (
            "From list [2, 8, 5, 11, 3] pick only elements greater than 5. "
            "Create an empty list and in a for loop append matching ones. Print the result."
        ),
        "tests": [{"expected_output": "[8, 11]"}],
    },
    "list-33": {
        "title": "Access by index",
        "condition": (
            "List nums = [10, 20, 30, 40, 50]. Ask for an index (integer). "
            "If the index is from 0 to len − 1 — print the element, otherwise — error."
        ),
        "tests": [
            {"stdin": "2\n", "expected_output": "30"},
            {"stdin": "0\n", "expected_output": "10"},
            {"stdin": "9\n", "expected_output": "error"},
        ],
    },
    "list-34": {
        "title": "Without edges",
        "condition": (
            "From list [1, 2, 3, 4, 5] remove the first and last element "
            "(pop twice — first from the end, then from the beginning) and print the remaining list."
        ),
        "tests": [{"expected_output": "[2, 3, 4]"}],
        "hint": "After pop() from the end the indices shift — the order of operations matters.",
    },
    "list-35": {
        "title": "Even positions",
        "condition": (
            "In list [10, 20, 30, 40, 50] print elements at even positions "
            "(0, 2, 4…) — each on a new line, using a for loop and range with step 2."
        ),
        "tests": [{"expected_output": "10\n30\n50"}],
    },
    "list-36": {
        "title": "Sum of even elements",
        "condition": (
            "Given the list [1, 2, 3, 4, 5, 6]. In a for loop add only the even elements "
            "and print the sum."
        ),
        "tests": [{"expected_output": "12"}],
        "hint": "Check evenness with the remainder of division by 2.",
    },
    "list-37": {
        "title": "Second largest",
        "condition": (
            "Given the list [15, 3, 42, 7]. Find the second-largest element and print it. "
            "You may sort the list."
        ),
        "tests": [{"expected_output": "15"}],
        "hint": "After sorting in ascending order the second maximum is in the second-to-last place.",
    },
    "list-38": {
        "title": "Shift left",
        "condition": (
            "Given the list [10, 20, 30, 40]. Shift it left by one step: "
            "the first element moves to the end. Print the resulting list."
        ),
        "tests": [{"expected_output": "[20, 30, 40, 10]"}],
        "hint": "Remove the first element with pop(0) and append it at the end.",
    },
    "list-39": {
        "title": "Product of elements",
        "condition": (
            "Given the list [2, 3, 4]. Multiply all elements in a for loop and print the product."
        ),
        "tests": [{"expected_output": "24"}],
        "hint": "Start the product at 1, not 0.",
    },
    "list-40": {
        "title": "Above average",
        "condition": (
            "Given the grade list [4, 5, 3, 5, 4]. Compute the arithmetic mean "
            "and print how many elements are strictly greater than that mean."
        ),
        "tests": [{"expected_output": "2"}],
        "hint": "First find the sum and the mean, then in a second loop count matching elements.",
    },
    "list-41": {
        "title": "Common elements",
        "condition": (
            "Given lists [1, 2, 3, 4] and [3, 4, 5, 3]. Print the elements of the first list "
            "that appear in the second, each on a new line (no duplicates from the first: 3, then 4)."
        ),
        "tests": [{"expected_output": "3\n4"}],
        "hint": "For each element of the first list check in and print immediately.",
    },
    "list-42": {
        "title": "Prefix sums",
        "condition": (
            "Given the list [1, 2, 3, 4]. Build the list of prefix sums "
            "[1, 1+2, 1+2+3, 1+2+3+4] and print it."
        ),
        "tests": [{"expected_output": "[1, 3, 6, 10]"}],
        "hint": "Keep a running sum variable and on each step append it to a new list.",
    },
    "list-43": {
        "title": "Shift right",
        "condition": (
            "Given the list [10, 20, 30, 40]. Shift it one step to the right: "
            "the last element moves to the beginning. Print the list."
        ),
        "tests": [{"expected_output": "[40, 10, 20, 30]"}],
        "hint": "Pop the last element with pop() and insert it at the beginning with insert(0, …).",
    },
    "list-44": {
        "title": "Negatives to zeros",
        "condition": (
            "Given the list [2, -3, 5, -1, 0]. Replace all negative elements with 0 "
            "and print the resulting list."
        ),
        "tests": [{"expected_output": "[2, 0, 5, 0, 0]"}],
        "hint": "Build a new list: append 0 for negatives and the original value otherwise.",
    },
    "list-45": {
        "title": "Second minimum",
        "condition": (
            "Given the list [15, 3, 42, 7]. Find the second smallest element "
            "(you may sort the list). Print it."
        ),
        "tests": [{"expected_output": "7"}],
    },
    "list-46": {
        "title": "Index of the maximum",
        "condition": (
            "Given the list [3, 9, 4, 9, 1]. Print the index of the first occurrence of the maximum (0-based)."
        ),
        "tests": [{"expected_output": "1"}],
        "hint": "Remember both the current maximum and its index.",
    },
    "list-47": {
        "title": "Odds only",
        "condition": (
            "From the list [1, 2, 3, 4, 5, 6] build a new list of odd elements only "
            "and print it."
        ),
        "tests": [{"expected_output": "[1, 3, 5]"}],
    },
    "list-48": {
        "title": "Neighbor products",
        "condition": (
            "Given the list [2, 3, 4, 5]. Print the products of adjacent pairs "
            "(2×3, 3×4, 4×5) — each on a new line."
        ),
        "tests": [{"expected_output": "6\n12\n20"}],
    },
    "list-49": {
        "title": "Gap from the maximum",
        "condition": (
            "Given the list [1, 5, 3]. Find the maximum and print for each element "
            "the difference maximum − element (each number on a new line)."
        ),
        "tests": [{"expected_output": "4\n0\n2"}],
    },
    "list-50": {
        "title": "Evens to the front",
        "condition": (
            "Given the list [1, 2, 3, 4, 5]. Build a new list: first all even numbers in original order, "
            "then all odd numbers. Print it."
        ),
        "tests": [{"expected_output": "[2, 4, 1, 3, 5]"}],
        "hint": "You can keep two lists and then extend.",
    },
}

# Lists fix tasks
LISTS_FIX: dict[str, dict] = {
    "list-fix-01": {
        "title": "Fix: first element",
        "condition": (
            "Only the first fruit from the display is needed, "
            "but the loop prints the whole list. " + _FIX_INTRO
        ),
        "hint": "Only the first fruit is needed — apple.",
        "tests": [{"expected_output": "apple"}],
    },
    "list-fix-02": {
        "title": "Fix: append",
        "condition": (
            "The number 4 should end up at the end of the list, "
            "but it is inserted at the beginning. " + _FIX_INTRO
        ),
        "hint": "You need the append method, not insert at the beginning.",
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-fix-03": {
        "title": "Fix: sum of a list",
        "condition": (
            "The sum of receipts 10+20+30 is computed with multiplication "
            "instead of addition. " + _FIX_INTRO
        ),
        "hint": "For the sum accumulate the value with +.",
        "tests": [{"expected_output": "60"}],
    },
    "list-fix-04": {
        "title": "Fix: sorting",
        "condition": (
            "Grades should be arranged in ascending order, "
            "but the list is simply reversed. " + _FIX_INTRO
        ),
        "hint": "You need the sort method, not reverse.",
        "tests": [{"expected_output": "[1, 2, 3, 4]"}],
    },
    "list-fix-05": {
        "title": "Fix: length after clear",
        "condition": (
            "After «clearing» the list one element remains — "
            "only one item was removed instead of all. " + _FIX_INTRO
        ),
        "hint": "To make the list empty, use clear.",
        "tests": [{"expected_output": "0"}],
    },
    "list-fix-06": {
        "title": "Fix: reversed list",
        "condition": (
            "Reversing list [1,2,3,4] did not work — "
            "elements are appended at the end in the same order. " + _FIX_INTRO
        ),
        "hint": "To reverse, insert each element at the beginning.",
        "tests": [{"expected_output": "[4, 3, 2, 1]"}],
    },
    "list-fix-07": {
        "title": "Fix: greater than five",
        "condition": (
            "The «greater than five» filter only lets through numbers greater than 10 — "
            "the threshold is too high. " + _FIX_INTRO
        ),
        "hint": "You need numbers strictly greater than 5.",
        "tests": [{"expected_output": "[8, 11]"}],
    },
    "list-fix-08": {
        "title": "Fix: index",
        "condition": (
            "Access by index always prints error, "
            "even for a valid index 2. " + _FIX_INTRO
        ),
        "hint": "For a valid index you need to print the list element.",
        "tests": [
            {"stdin": "2\n", "expected_output": "30"},
            {"stdin": "0\n", "expected_output": "10"},
            {"stdin": "9\n", "expected_output": "error"},
        ],
    },
    "list-fix-09": {
        "title": "Fix: without edges",
        "condition": (
            "From list [1,2,3,4,5] only the last element was removed — "
            "the first one stayed in place. " + _FIX_INTRO
        ),
        "hint": "You need to remove both the last and the first element.",
        "tests": [{"expected_output": "[2, 3, 4]"}],
    },
    "list-fix-10": {
        "title": "Fix: even positions",
        "condition": (
            "Elements at positions 0, 2, 4 are needed, "
            "but the loop prints all five values. " + _FIX_INTRO
        ),
        "hint": "Loop over indices with step 2.",
        "tests": [{"expected_output": "10\n30\n50"}],
    },
}

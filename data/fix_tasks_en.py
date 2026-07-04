"""English buggy Python for «fix the code» tasks."""

from __future__ import annotations

BUGGY_CODE_EN = {
    "cond-fix-01": """number = 15
if number < 10:
    print('yes')
else:
    print('no')""",
    "cond-fix-02": """n = int(input())
if n > 0:
    print('negative')
elif n == 0:
    print('zero')
else:
    print('positive')""",
    "cond-fix-03": """v = int(input())
if v < 18:
    print('adult')
else:
    print('child')""",
    "cond-fix-04": """age = 10
warm = True
if age >= 11 and warm:
    print('can go out')
else:
    print('stay home')""",
    "cond-fix-05": """n = int(input())
if n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
elif n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
else:
    print(n)""",
    "cond-fix-06": """x = int(input())
a = int(input())
b = int(input())
if x >= a:
    print('in range')
else:
    print('out of range')""",
    "cond-fix-07": """a = int(input())
b = int(input())
c = int(input())
if a > b:
    print('first')
else:
    print('second')""",
    "cond-fix-08": """a = int(input())
b = int(input())
if a // b == 0:
    print('divides')
else:
    print('does not divide')""",
    "cond-fix-09": """a = int(input())
b = int(input())
c = int(input())
if b + c > a:
    print('possible')
else:
    print('impossible')""",
    "cond-fix-10": """o1 = int(input())
o2 = int(input())
if o1 >= o2:
    d = o1 - o2
else:
    d = o2 - o1
if d >= 3:
    print('jump')
else:
    print('stable')""",
    "for-fix-01": """for i in range(1, 5, 1):
    print(i)""",
    "for-fix-02": """for _ in range(0, 3, 1):
    print('Python')""",
    "for-fix-03": """s = 0
for i in range(1, 11, 1):
    s = s * i
print(s)""",
    "for-fix-04": """for i in range(1, 6, 1):
    print(i)""",
    "for-fix-05": """n = int(input())
for i in range(1, n, 1):
    print(i)""",
    "for-fix-06": """n = int(input())
for i in range(2, 2 * n + 1, 2):
    print(i)""",
    "for-fix-07": """n = int(input())
k = int(input())
for i in range(0, n + 1, k):
    print(i)""",
    "for-fix-08": """a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1, 1):
    s = s + i
print(s)""",
    "for-fix-09": """ch = input()
s = input()
c = 0
for x in s:
    if x == s:
        c = c + 1
print(c)""",
    "for-fix-10": """n = int(input())
for i in range(1, n + 1, 1):
    if i % 2 == 0:
        print(i)""",
    "io-fix-01": 'print("Hello, world")',
    "io-fix-02": """subject = "math"
print(subject)""",
    "io-fix-03": """name = input()
print("Hello!")""",
    "io-fix-04": """print("How are you?")
print("Hello!")""",
    "io-fix-05": """name = input()
print("Glad to see you, " + name)""",
    "io-fix-06": """surname = input()
name = input()
print("Then: " + name)
print("First: " + surname)""",
    "io-fix-07": """a = input()
b = input()
c = input()
print(a + " " + b + " " + c)""",
    "io-fix-08": """dish = input()
price = input()
print("Dish: " + dish + ", price: " + price)""",
    "io-fix-09": """w1 = input()
w2 = input()
print(len(w1))
print(w1)
print(len(w2))
print(w2)""",
    "io-fix-10": """name = input()
number = input()
print("Batch " + name + ": " + number + " — OK")""",
    "list-fix-01": """fruits = ["apple", "banana", "pear"]
for x in fruits:
    print(x)""",
    "list-fix-02": """numbers = [1, 2, 3]
numbers.insert(0, 4)
print(numbers)""",
    "list-fix-03": """numbers = [10, 20, 30]
s = 0
for x in numbers:
    s = s * x
print(s)""",
    "list-fix-04": """numbers = [3, 1, 4, 2]
numbers.reverse()
print(numbers)""",
    "list-fix-05": """a = [10, 20]
a.remove(10)
print(len(a))""",
    "list-fix-06": """numbers = [1, 2, 3, 4]
rev = []
for x in numbers:
    rev.append(x)
print(rev)""",
    "list-fix-07": """nums = [2, 8, 5, 11, 3]
big = []
for x in nums:
    if x > 10:
        big.append(x)
print(big)""",
    "list-fix-08": """nums = [10, 20, 30, 40, 50]
i = int(input())
print('error')""",
    "list-fix-09": """nums = [1, 2, 3, 4, 5]
nums.remove(5)
print(nums)""",
    "list-fix-10": """nums = [10, 20, 30, 40, 50]
for x in nums:
    print(x)""",
    "numbers-fix-01": 'print(8 + 12)',
    "numbers-fix-02": """n = input()
print(n + 10)""",
    "numbers-fix-03": """a = int(input())
b = int(input())
print((a + b) / 3)""",
    "numbers-fix-04": 'print(6 * 2)',
    "numbers-fix-05": 'print(17 // 5)',
    "numbers-fix-06": """km = int(input())
print(50 + 15 + km)""",
    "numbers-fix-07": """m = int(input())
print(m / 60)
print(m % 60)""",
    "numbers-fix-08": """n = 528
print(n % 100)""",
    "numbers-fix-09": """price = int(input())
discount = int(input())
print(price - discount)""",
    "numbers-fix-10": """n = int(input())
print(n - 1)
print(n + 1)
print(n)""",
    "str-fix-01": """word = "python"
print(word.lower())""",
    "str-fix-02": """s = "  cat  "
print(s.upper())""",
    "str-fix-03": """word = "Friend"
print(word.find("fri"))""",
    "str-fix-04": """word = "cot"
print(word.replace("t", "a"))""",
    "str-fix-05": """s = input()
print(s.lower())""",
    "str-fix-06": """s = input()
c = 0
for ch in s:
    if ch == 'a':
        c = c + 1
print(c)""",
    "str-fix-07": """s = input()
print('palindrome')""",
    "str-fix-08": """s = input()
print(s + '[]')""",
    "str-fix-09": """s = input()
print(s + ' ' + s)""",
    "str-fix-10": """s = input()
print(s.upper())""",
    "while-fix-01": """i = 1
while i <= 4:
    print(i)
    i = i + 1""",
    "while-fix-02": """t = 5
while t > 0:
    print(t)
    t = t + 1""",
    "while-fix-03": """i = 1
s = 0
while i <= 5:
    s = s + i
    i = i + 2
print(s)""",
    "while-fix-04": """n = 1
while n <= 10:
    print(n)
    n = n + 2""",
    "while-fix-05": """n = int(input())
i = 0
while i <= n:
    print('step')
    i = i + 1""",
    "while-fix-06": """n = int(input())
while n > 0:
    print(n % 10)
    n = n // 10""",
    "while-fix-07": """s = 0
x = int(input())
while x != 0:
    x = int(input())
    s = s + x
print(s)""",
    "while-fix-08": """a = int(input())
b = int(input())
while b != 0:
    t = a % b
    a = a % b
    b = t
print(a)""",
    "while-fix-09": """base = int(input())
exp = int(input())
result = 1
i = 0
while i <= exp:
    result = result * base
    i = i + 1
print(result)""",
    "while-fix-10": """n = int(input())
d = 1
count = 0
while d <= n:
    count = count + 1
    d = d + 1
print(count)""",
}

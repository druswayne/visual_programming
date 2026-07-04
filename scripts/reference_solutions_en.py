"""English reference solutions for base tasks used by fix tasks."""

from __future__ import annotations

REFERENCE_SOLUTIONS_EN = {
    "cond-01": """number = 15
print('yes' if number > 10 else 'no')""",
    "cond-06": """v = int(input())
print('adult' if v >= 18 else 'child')""",
    "cond-07": """n = int(input())
if n > 0:
    print('positive')
elif n == 0:
    print('zero')
else:
    print('negative')""",
    "cond-12": """age = 10
warm = True
print('can go out' if age >= 6 and warm else 'stay home')""",
    "cond-26": """n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)""",
    "cond-31": """x = int(input())
a = int(input())
b = int(input())
print('in range' if a <= x <= b else 'out of range')""",
    "cond-32": """a = int(input())
b = int(input())
c = int(input())
if b >= a and b >= c:
    print('second')
elif a >= b and a >= c:
    print('first')
else:
    print('third')""",
    "cond-33": """a = int(input())
b = int(input())
print('divides' if a % b == 0 else 'does not divide')""",
    "cond-34": """a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('possible')
else:
    print('impossible')""",
    "cond-35": """o1 = int(input())
o2 = int(input())
d = o1 - o2 if o1 >= o2 else o2 - o1
print('jump' if d >= 2 else 'stable')""",
    "for-01": """for i in range(1, 6, 1):
    print(i)""",
    "for-02": """for _ in range(0, 4, 1):
    print('Python')""",
    "for-05": """s = 0
for i in range(1, 11, 1):
    s = s + i
print(s)""",
    "for-06": """for i in range(1, 6, 1):
    print(i * i)""",
    "for-07": """n = int(input())
for i in range(1, n + 1, 1):
    print(i)""",
    "for-31": """n = int(input())
for i in range(1, 2 * n, 2):
    print(i)""",
    "for-32": """n = int(input())
k = int(input())
for i in range(k, n + 1, k):
    print(i)""",
    "for-33": """a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1, 1):
    if i % 2 == 0:
        s = s + i
print(s)""",
    "for-34": """ch = input()
s = input()
c = 0
for x in s:
    if x == ch:
        c = c + 1
print(c)""",
    "for-35": """n = int(input())
for i in range(1, n + 1, 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)""",
    "io-01": 'print("Hello, world!")',
    "io-04": """subject = "computer science"
print(subject)""",
    "io-06": """print("Hello!")
print("How are you?")""",
    "io-09": """name = input()
print("Hello, " + name)""",
    "io-19": """name = input()
print("Glad to see you, " + name + "!")""",
    "io-31": """surname = input()
name = input()
print("First: " + surname)
print("Then: " + name)""",
    "io-32": """a = input()
b = input()
c = input()
print(a + b + c)""",
    "io-33": """dish = input()
price = input()
print("Dish: " + dish + ", price: " + price + " USD.")""",
    "io-34": """w1 = input()
w2 = input()
print(w1)
print(len(w1))
print(w2)
print(len(w2))""",
    "io-35": """name = input()
number = input()
print("Batch " + number + ": " + name + " — OK")""",
    "list-01": """fruits = ["apple", "banana", "pear"]
print(fruits[0])""",
    "list-03": """numbers = [1, 2, 3]
numbers.append(4)
print(numbers)""",
    "list-06": """numbers = [10, 20, 30]
s = 0
for x in numbers:
    s = s + x
print(s)""",
    "list-12": """numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)""",
    "list-17": """a = [10, 20]
a.clear()
print(len(a))""",
    "list-31": """numbers = [1, 2, 3, 4]
rev = []
for x in numbers:
    rev.insert(0, x)
print(rev)""",
    "list-32": """nums = [2, 8, 5, 11, 3]
big = []
for x in nums:
    if x > 5:
        big.append(x)
print(big)""",
    "list-33": """nums = [10, 20, 30, 40, 50]
i = int(input())
if i >= 0 and i < len(nums):
    print(nums[i])
else:
    print('error')""",
    "list-34": """nums = [1, 2, 3, 4, 5]
nums.pop()
nums.pop(0)
print(nums)""",
    "list-35": """nums = [10, 20, 30, 40, 50]
for i in range(0, len(nums), 2):
    print(nums[i])""",
    "numbers-03": 'print(8 * 12)',
    "numbers-06": 'print(6 ** 2)',
    "numbers-07": 'print(17 % 5)',
    "numbers-10": """n = int(input())
print(n + 10)""",
    "numbers-12": """a = int(input())
b = int(input())
print((a + b) / 2)""",
    "numbers-31": """km = int(input())
print(50 + 15 * km)""",
    "numbers-32": """m = int(input())
print(m // 60)
print(m % 60)""",
    "numbers-33": """n = 528
print(n // 100)""",
    "numbers-34": """price = int(input())
discount = int(input())
print(price * (100 - discount) / 100)""",
    "numbers-35": """n = int(input())
print(n - 1)
print(n)
print(n + 1)""",
    "str-01": """word = "python"
print(word.upper())""",
    "str-03": """s = "  cat  "
print(s.strip())""",
    "str-08": """word = "Friend"
print(word.find("end"))""",
    "str-12": """word = "cot"
print(word.replace("o", "a"))""",
    "str-17": """s = input()
print(s.upper())""",
    "str-31": """s = input()
v = 'aeiou'
c = 0
for ch in s:
    if ch in v:
        c = c + 1
print(c)""",
    "str-32": """s = input()
print('palindrome' if s == s[::-1] else 'not a palindrome')""",
    "str-33": """s = input()
print('[' + s + ']')""",
    "str-34": """s = input()
print(s + s)""",
    "str-35": """s = input()
print(s[::-1])""",
    "while-01": """i = 1
while i <= 5:
    print(i)
    i = i + 1""",
    "while-03": """t = 5
while t > 0:
    print(t)
    t = t - 1""",
    "while-04": """n = 2
while n <= 10:
    print(n)
    n = n + 2""",
    "while-05": """i = 1
s = 0
while i <= 5:
    s = s + i
    i = i + 1
print(s)""",
    "while-18": """n = int(input())
i = 0
while i < n:
    print('step')
    i = i + 1""",
    "while-31": """n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)""",
    "while-32": """s = 0
x = int(input())
while x != 0:
    s = s + x
    x = int(input())
print(s)""",
    "while-33": """a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)""",
    "while-34": """base = int(input())
exp = int(input())
result = 1
i = 0
while i < exp:
    result = result * base
    i = i + 1
print(result)""",
    "while-35": """n = int(input())
d = 1
count = 0
while d <= n:
    if n % d == 0:
        count = count + 1
    d = d + 1
print(count)""",
}

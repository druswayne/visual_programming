"""Эталонные решения для проверки задач."""

REFERENCE_SOLUTIONS = {
    # --- io ---
    "io-01": 'print("Привет, мир!")',
    "io-02": 'print("Аня")',
    "io-03": 'print("Школа")',
    "io-04": 'предмет = "информатика"\nprint(предмет)',
    "io-05": 'город = "Казань"\nprint(город)',
    "io-06": 'print("Привет!")\nprint("Как дела?")',
    "io-07": 'print("Раз")\nprint("Два")\nprint("Три")',
    "io-08": 'print("Я учу Python")',
    "io-09": 'имя = input()\nprint("Привет, " + имя)',
    "io-10": "print(input())",
    "io-11": "город = input()\nprint(город)",
    "io-12": "print(input())\nprint(input())",
    "io-13": "x = input()\nprint(x)\nprint(x)",
    "io-14": "print(input())\nprint(input())",
    "io-15": "слово = input()\nprint(слово)",
    "io-16": 'print("Беги!")\nprint("Беги!")',
    "io-17": 'print("— Привет!")\nprint("— Привет!")\nprint("— Пойдём гулять?")',
    "io-18": 'print("Герой")\nprint("смелый")',
    "io-19": 'имя = input()\nprint("Рад тебя видеть, " + имя + "!")',
    "io-20": 'print(input())\nprint(input())\nprint("Удачи в учёбе!")',
    # --- numbers ---
    "numbers-01": "print(7 + 5)",
    "numbers-02": "print(50 - 18)",
    "numbers-03": "print(8 * 12)",
    "numbers-04": "print(9 / 4)",
    "numbers-05": "очки = 100\nprint(очки)",
    "numbers-06": "print(6 ** 2)",
    "numbers-07": "print(17 % 5)",
    "numbers-08": "print(47 // 6)",
    "numbers-09": "s = 10 + 4\nprint(s * 3)",
    "numbers-10": "n = int(input())\nprint(n + 10)",
    "numbers-11": "a = int(input())\nb = int(input())\nprint(a + b)",
    "numbers-12": "a = int(input())\nb = int(input())\nprint((a + b) / 2)",
    "numbers-13": "k = int(input())\nprint(k * 150)",
    "numbers-14": "y = int(input())\nprint(2026 - y)",
    "numbers-15": "a = float(input())\nb = float(input())\nprint(a * b)",
    "numbers-16": "x = int(input())\nprint(x - 73)",
    "numbers-17": "n = int(input())\nprint(n % 8)",
    "numbers-18": "print(2 ** 10)",
    "numbers-19": "a = 7\nb = 3\nprint(2 * (a + b))",
    "numbers-20": "n = int(input())\nprint(n + 5)\nprint(n * n)\nprint(n // 2)",
    # --- conditions ---
    "cond-01": "число = 15\nprint('да' if число > 10 else 'нет')",
    "cond-02": "температура = -4\nprint('мороз' if температура < 0 else 'не мороз')",
    "cond-03": "a = 8\nb = 8\nprint('равны' if a == b else 'разные')",
    "cond-04": "n = 14\nprint('чётное' if n % 2 == 0 else 'нечётное')",
    "cond-05": "print('верно' if True else 'неверно')",
    "cond-06": "v = int(input())\nprint('взрослый' if v >= 18 else 'ребёнок')",
    "cond-07": """n = int(input())
if n > 0:
    print('положительное')
elif n == 0:
    print('ноль')
else:
    print('отрицательное')""",
    "cond-08": "o = int(input())\nprint('сдал' if o >= 4 else 'не сдал')",
    "cond-09": """o = int(input())
if o == 5:
    print('отлично')
elif o == 4:
    print('хорошо')
elif o == 3:
    print('удовлетворительно')
else:
    print('неудовлетворительно')""",
    "cond-10": """h = int(input())
if 6 <= h <= 11:
    print('утро')
elif 12 <= h <= 17:
    print('день')
elif 18 <= h <= 22:
    print('вечер')
else:
    print('ночь')""",
    "cond-11": """a = int(input())
b = int(input())
if a > b:
    print('первое')
elif b > a:
    print('второе')
else:
    print('равны')""",
    "cond-12": "возраст = 10\nтепло = True\nprint('можно гулять' if возраст >= 6 and тепло else 'остаёмся дома')",
    "cond-13": "дождь = False\nветер = True\nprint('возьми зонт' if дождь or ветер else 'зонт не нужен')",
    "cond-14": "c = input()\nprint('дверь открыта' if c == 'Python' else 'неверный код')",
    "cond-15": "b = input()\nprint('гласная' if b in 'аеиоуыэюя' else 'согласная')",
    "cond-16": "t = input()\nprint('про животное' if 'собака' in t else 'другая тема')",
    "cond-17": """n = int(input())
if n == 1:
    print('автобус')
elif n == 2:
    print('поезд')
elif n == 3:
    print('самолёт')
else:
    print('неизвестно')""",
    "cond-18": """t = int(input())
if t > 30:
    print('жарко')
elif t > 15:
    print('тепло')
elif t > 0:
    print('прохладно')
else:
    print('холодно')""",
    "cond-19": """a = int(input())
r = int(input())
print('можно' if a >= 12 and r >= 140 else 'нельзя')""",
    "cond-20": """name = input()
age = int(input())
print('Привет, ' + name + '!')
print('совершеннолетний' if age >= 18 else 'несовершеннолетний')
print('школьник' if 6 <= age <= 17 else 'не школьник')""",
    # --- while ---
    "while-01": """i = 1
while i <= 5:
    print(i)
    i = i + 1""",
    "while-02": """r = 0
while r < 3:
    print('Готов!')
    r = r + 1""",
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
    "while-06": """i = 1
while i <= 4:
    print(i * 10)
    i = i + 1""",
    "while-07": """k = 0
while k < 5:
    print('★')
    k = k + 1""",
    "while-08": """n = int(input())
i = 1
while i <= n:
    print(i)
    i = i + 1""",
    "while-09": """x = 1
while x <= 5:
    print(x * x)
    x = x + 1""",
    "while-10": """n = 1
while n <= 32:
    print(n)
    n = n * 2""",
    "while-11": """i = 1
s = 0
while i <= 10:
    s = s + i
    i = i + 1
print(s)""",
    "while-12": """n = 10
while n >= 6:
    print(n)
    n = n - 1""",
    "while-13": """o = 20
while o > 0:
    print(o)
    o = o - 5""",
    "while-14": """n = int(input())
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print(s)""",
    "while-15": """m = 7
while m <= 35:
    print(m)
    m = m + 7""",
    "while-16": """c = 0
while c < 3:
    print('привет')
    c = c + 1""",
    "while-17": """v = 1
while v < 100:
    print(v)
    v = v * 3""",
    "while-18": """n = int(input())
i = 0
while i < n:
    print('шаг')
    i = i + 1""",
    "while-19": """n = int(input())
while n > 0:
    print(n)
    n = n - 1""",
    "while-20": """n = int(input())
print(n)
print(n * 2)
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print(s)""",
    # --- for ---
    "for-01": "for i in range(1, 6, 1):\n    print(i)",
    "for-02": "for _ in range(0, 4, 1):\n    print('Python')",
    "for-03": "for x in range(0, 10, 2):\n    print(x)",
    "for-04": "for i in range(10, 0, -1):\n    print(i)",
    "for-05": """s = 0
for i in range(1, 11, 1):
    s = s + i
print(s)""",
    "for-06": "for i in range(1, 6, 1):\n    print(i * i)",
    "for-07": """n = int(input())
for i in range(1, n + 1, 1):
    print(i)""",
    "for-08": "for i in range(5, 16, 1):\n    print(i)",
    "for-09": "for x in range(3, 8, 1):\n    print(x * 3)",
    "for-10": "for i in range(1, 10, 3):\n    print(i)",
    "for-11": """p = 1
for i in range(1, 6, 1):
    p = p * i
print(p)""",
    "for-12": """n = int(input())
for i in range(0, n, 1):
    print(i)""",
    "for-13": "for i in range(20, 10, -2):\n    print(i)",
    "for-14": """a = int(input())
b = int(input())
for i in range(a, b, 1):
    print(i)""",
    "for-15": """s = 0
for i in range(2, 11, 2):
    s = s + i
print(s)""",
    "for-16": "for i in range(1, 6, 1):\n    print(i + 10)",
    "for-17": """n = int(input())
for i in range(1, n + 1, 1):
    print(i * 5)""",
    "for-18": "for i in range(100, 0, -25):\n    print(i)",
    "for-19": """n = int(input())
for _ in range(n):
    print('звезда')""",
    "for-20": """n = int(input())
s = 0
p = 1
for i in range(1, n + 1, 1):
    s = s + i
    p = p * i
print(s)
print(p)
print(n)""",
    # --- strings ---
    "str-01": 'слово = "python"\nprint(слово.upper())',
    "str-02": 'текст = "HELLO"\nprint(текст.lower())',
    "str-03": 'с = "  кот  "\nprint(с.strip())',
    "str-04": 'фрукт = "яблоко"\nprint(фрукт.capitalize())',
    "str-05": 'дом = "большой зеленый дом"\nprint(дом.title())',
    "str-06": 'год = "2024"\nprint(год.isdigit())',
    "str-07": 'буквы = "abc"\nprint(буквы.isalpha())',
    "str-08": 'слово = "Привет"\nprint(слово.find("вет"))',
    "str-09": 'слово = "банан"\nprint(слово.count("а"))',
    "str-10": 'слово = "мороз"\nprint(слово.startswith("мор"))',
    "str-11": 'слово = "книга"\nprint(слово.endswith("га"))',
    "str-12": 'слово = "кот"\nprint(слово.replace("о", "а"))',
    "str-13": 'print("Привет" + ", мир!")',
    "str-14": 'слово = "PyThOn"\nprint(слово.swapcase())',
    "str-15": 'пусто = "   "\nprint(пусто.isspace())',
    "str-16": 'слово = "информатика"\nprint(len(слово))',
    "str-17": "s = input()\nprint(s.upper())",
    "str-18": "parts = input().split()\nprint(parts[1])",
    "str-19": "s = input()\nprint(s.replace(' ', '_'))",
    "str-20": """s = input()
print(len(s))
print(s.upper())
print(s.lower())""",
    # --- lists ---
    "list-01": 'фрукты = ["яблоко", "банан", "груша"]\nprint(фрукты[0])',
    "list-02": 'числа = [5, 10, 15]\nprint(len(числа))',
    "list-03": 'числа = [1, 2, 3]\nчисла.append(4)\nprint(числа)',
    "list-04": 'a = []\na.append("а")\na.append("б")\nprint(a)',
    "list-05": 'числа = [1, 2, 3, 4, 5]\nfor x in числа:\n    print(x)',
    "list-06": """числа = [10, 20, 30]
s = 0
for x in числа:
    s = s + x
print(s)""",
    "list-07": 'числа = [1, 2, 3]\nчисла.insert(0, 99)\nprint(числа)',
    "list-08": 'числа = [1, 2, 3, 2]\nчисла.remove(2)\nprint(числа)',
    "list-09": 'числа = [5, 6, 7]\nprint(числа.pop())',
    "list-10": 'числа = [1, 2, 2, 3, 2]\nprint(числа.count(2))',
    "list-11": 'животные = ["собака", "кот", "птица"]\nprint(животные.index("кот"))',
    "list-12": 'числа = [3, 1, 4, 2]\nчисла.sort()\nprint(числа)',
    "list-13": 'числа = [1, 2, 3]\nчисла.reverse()\nprint(числа)',
    "list-14": 'а = [1, 2]\nа.extend([3, 4])\nprint(а)',
    "list-15": 'звуки = ["мяу", "гав", "хрум"]\nfor z in звуки:\n    print(z)',
    "list-16": """числа = [1, 2, 3, 4, 5]
s = 0
for x in числа:
    s = s + x
print(s)""",
    "list-17": 'a = [10, 20]\na.clear()\nprint(len(a))',
    "list-18": 'числа = [10, 20, 30, 40]\nprint(числа.pop(1))',
    "list-19": 'буквы = ["а", "б"]\nбуквы.append(input())\nprint(буквы)',
    "list-20": """числа = []
for _ in range(3):
    числа.append(int(input()))
print(len(числа))
s = 0
for x in числа:
    s = s + x
print(s)
print(числа)""",
    # --- io advanced (21-30) ---
    "io-21": """имя = input()
класс = input()
город = input()
print("Ученик: " + имя)
print("Класс: " + класс)
print("Город: " + город)""",
    "io-22": """слово = input()
print("Вы сказали: " + слово)
print("Вы сказали: " + слово)""",
    "io-23": """a = input()
b = input()
c = input()
print(a + ", " + b + ", " + c)""",
    "io-24": """пароль = input()
print(пароль)
print(len(пароль))""",
    "io-25": """a = input()
b = input()
print(b)
print(a)""",
    "io-26": """a = input()
b = input()
c = input()
print("1) " + a)
print("2) " + b)
print("3) " + c)""",
    "io-27": """слово = input()
print(слово + "!")""",
    "io-28": """a = input()
b = input()
print(a + " - " + b)""",
    "io-29": """фраза = input()
print(фраза)
print(фраза)
print(фраза)""",
    "io-30": """имя = input()
мечта = input()
print("Привет, " + имя + "!")
print("Твоя мечта: " + мечта)
print("Удачи!")""",
    # --- numbers advanced (21-30) ---
    "numbers-21": """a = int(input())
b = int(input())
print(a * b)
print(2 * (a + b))""",
    "numbers-22": """c = int(input())
print(c * 9 / 5 + 32)""",
    "numbers-23": """a = int(input())
b = int(input())
print(a // b)
print(a % b)""",
    "numbers-24": """n = int(input())
print(n ** 2)
print(n ** 3)
print(n ** 4)""",
    "numbers-25": """a = int(input())
b = int(input())
c = int(input())
print((a + b + c) / 3)""",
    "numbers-26": """k = int(input())
print(k // 100)
print(k % 100)""",
    "numbers-27": """n = 3
print(n ** 1)
print(n ** 2)
print(n ** 3)""",
    "numbers-28": """a = int(input())
b = int(input())
print(a ** 3 - b ** 3)""",
    "numbers-29": """x = int(input())
print(-x if x < 0 else x)""",
    "numbers-30": """n = int(input())
print(2 * n + 1)
print(n ** 2 - n)
print(n // 3)""",
    # --- conditions advanced (21-30) ---
    "cond-21": """y = int(input())
print('високосный' if y % 4 == 0 else 'обычный')""",
    "cond-22": """a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('равносторонний')
elif a == b or b == c or a == c:
    print('равнобедренный')
else:
    print('разносторонний')""",
    "cond-23": """b = int(input())
if b >= 90:
    print('отлично')
elif b >= 70:
    print('хорошо')
elif b >= 50:
    print('удовлетворительно')
else:
    print('неуд')""",
    "cond-24": """login = input()
password = input()
print('доступ разрешён' if login == 'admin' and password == '12345' else 'отказ')""",
    "cond-25": """n = int(input())
print('подходит' if n > 0 and n % 2 == 0 else 'не подходит')""",
    "cond-26": """n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)""",
    "cond-27": """m = int(input())
if m in (12, 1, 2):
    print('зима')
elif 3 <= m <= 5:
    print('весна')
elif 6 <= m <= 8:
    print('лето')
elif 9 <= m <= 11:
    print('осень')
else:
    print('ошибка')""",
    "cond-28": """op = input()
a = int(input())
b = int(input())
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print('ошибка')""",
    "cond-29": """p = input()
print('надёжный' if len(p) >= 8 else 'слабый')""",
    "cond-30": """name = input()
age = int(input())
score = int(input())
print('Ученик: ' + name)
print('сдал' if score >= 80 else 'не сдал')
print('младший' if age < 10 else 'старший')""",
    # --- while advanced (21-30) ---
    "while-21": """n = 48291
c = 0
while n > 0:
    c = c + 1
    n = n // 10
print(c)""",
    "while-22": """n = 123
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
print(s)""",
    "while-23": """n = int(input())
i = 1
while i <= 10:
    print(i * n)
    i = i + 1""",
    "while-24": """n = int(input())
p = 1
while p <= n:
    p = p * 2
print(p)""",
    "while-25": """n = 6
while n > 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1""",
    "while-26": """n = int(input())
p = 1
i = 1
while i <= n:
    p = p * i
    i = i + 1
print(p)""",
    "while-27": """n = int(input())
s = 0
i = 1
while i <= n:
    s = s + i * i
    i = i + 1
print(s)""",
    "while-28": """n = 5000
while n % 10 == 0:
    n = n // 10
print(n)""",
    "while-29": """n = int(input())
d = 2
while n % d != 0:
    d = d + 1
print(d)""",
    "while-30": """n = int(input())
p = 1
i = 1
while i <= n:
    p = p * i
    i = i + 1
print(p)
x = n
s = 0
while x > 0:
    s = s + x % 10
    x = x // 10
print(s)""",
    # --- for advanced (21-30) ---
    "for-21": "for i in range(1, 11, 1):\n    print(i * 7)",
    "for-22": """n = int(input())
s = 0
for i in range(1, n + 1, 1):
    s = s + i * i
print(s)""",
    "for-23": """a = int(input())
b = int(input())
c = 0
for i in range(a, b + 1, 1):
    if i % 2 == 0:
        c = c + 1
print(c)""",
    "for-24": """p = 1
for i in range(1, 8, 2):
    p = p * i
print(p)""",
    "for-25": """for i in range(1, 5, 1):
    print('*' * i)""",
    "for-26": """n = int(input())
s = 0
for i in range(2, n + 1, 2):
    s = s + i
print(s)""",
    "for-27": """n = int(input())
a, b = 1, 1
for _ in range(n):
    print(a)
    a, b = b, a + b""",
    "for-28": """a = int(input())
b = int(input())
m = a
for i in range(a, b + 1, 1):
    if i > m:
        m = i
print(m)""",
    "for-29": """n = int(input())
for i in range(n, 0, -1):
    print(i)""",
    "for-30": """n = int(input())
s = 0
sq = 0
c = 0
for i in range(1, n + 1, 1):
    s = s + i
    sq = sq + i * i
    if i % 3 == 0:
        c = c + 1
print(s)
print(sq)
print(c)""",
    # --- strings advanced (21-30) ---
    "str-21": """s = input()
print('палиндром' if len(s) == 3 and s[0] == s[2] else 'не палиндром')""",
    "str-22": """parts = input().split()
print(len(parts))""",
    "str-23": "print(input().title())",
    "str-24": """parts = input().split()
print(parts[0][0] + parts[1][0])""",
    "str-25": """s = input()
if s.isdigit():
    print('все цифры')
elif s.isalpha():
    print('только буквы')
else:
    print('смешанная')""",
    "str-26": """parts = input().split()
print(parts[0] + '-' + parts[1])""",
    "str-27": "print(input().strip().upper())",
    "str-28": "print(input().count(' '))",
    "str-29": "print(input().replace('.', '!'))",
    "str-30": """s = input()
print(len(s))
print(s.capitalize())
print(s.isalpha())
print(s.lower())""",
    # --- lists advanced (21-30) ---
    "list-21": """числа = [15, 3, 42, 7]
m = числа[0]
for x in числа:
    if x < m:
        m = x
print(m)""",
    "list-22": """n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
m = nums[0]
for x in nums:
    if x > m:
        m = x
print(m)""",
    "list-23": """nums = [1, 2, 3, 4, 5, 6]
чётные = []
for x in nums:
    if x % 2 == 0:
        чётные.append(x)
print(чётные)""",
    "list-24": """оценки = [4, 5, 3, 5, 4]
s = 0
for x in оценки:
    s = s + x
print(s)
print(s / len(оценки))""",
    "list-25": """слова = ['яблоко', 'груша', 'банан']
слова.sort()
print(слова)""",
    "list-26": """a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)""",
    "list-27": """nums = [1, 2, 3]
double = []
for x in nums:
    double.append(x)
    double.append(x)
print(double)""",
    "list-28": """nums = [10, 20, 30, 40]
nums.pop()
nums.pop()
print(nums)""",
    "list-29": """word = input()
animals = ['кот', 'собака', 'хомяк']
print('найдено' if word in animals else 'не найдено')""",
    "list-30": """nums = []
for _ in range(4):
    nums.append(int(input()))
nums.sort()
print(nums)
s = 0
for x in nums:
    s = s + x
print(s)""",
}

from data.fix_tasks_defs import FIX_TASK_DEFS

for _topic_id, _defs in FIX_TASK_DEFS.items():
    for _fix in _defs:
        _base_id = _fix["based_on"]
        if _base_id in REFERENCE_SOLUTIONS:
            REFERENCE_SOLUTIONS[_fix["id"]] = REFERENCE_SOLUTIONS[_base_id]

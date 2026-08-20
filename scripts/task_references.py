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
    "io-31": """фам = input()
имя = input()
print("Сначала: " + фам)
print("Потом: " + имя)""",
    "io-32": """a = input()
b = input()
c = input()
print(a + b + c)""",
    "io-33": """блюдо = input()
цена = input()
print("Блюдо: " + блюдо + ", цена: " + цена + " руб.")""",
    "io-34": """w1 = input()
w2 = input()
print(w1)
print(len(w1))
print(w2)
print(len(w2))""",
    "io-35": """название = input()
номер = input()
print("Партия " + номер + ": " + название + " — OK")""",
    "io-36": """имя = input()
класс = input()
город = input()
хобби = input()
print("Имя: " + имя)
print("Класс: " + класс)
print("Город: " + город)
print("Хобби: " + хобби)""",
    "io-37": """имя = input()
город = input()
желание = input()
print("Привет, " + имя + "!")
print("Город: " + город)
print("Пожелание: " + желание)""",
    "io-38": """a = input()
b = input()
c = input()
print("1. " + a)
print("2. " + b)
print("3. " + c)
print("Всего позиций: 3")""",
    "io-39": """имя = input()
роль = input()
строка = имя + " — " + роль
print(строка)
print(строка)""",
    "io-40": """a = input()
b = input()
c = input()
print(a + "-" + b + "-" + c)""",
    "io-41": """фам = input()
имя = input()
класс = input()
город = input()
школа = input()
print("Фамилия: " + фам)
print("Имя: " + имя)
print("Класс: " + класс)
print("Город: " + город)
print("Школа: " + школа)""",
    "io-42": """a = input()
b = input()
c = input()
d = input()
print("— " + a)
print("— " + b)
print("— " + c)
print("— " + d)""",
    "io-43": """a = input()
b = input()
print("Привет, " + a + " и " + b + "!")
print("До встречи, " + b + " и " + a + "!")""",
    "io-44": """folder = input()
name = input()
ext = input()
print(folder + "/" + name + "." + ext)""",
    "io-45": """login = input()
domain = input()
print(login + "@" + domain)""",
    "io-46": """s = input()
print("«" + s + "»")""",
    "io-47": """subj = input()
grade = input()
student = input()
print("Предмет: " + subj + " | Оценка: " + grade + " | Ученик: " + student)""",
    "io-48": """a = input()
b = input()
c = input()
d = input()
print("1. " + a)
print("2. " + b)
print("3. " + c)
print("4. " + d)
print("Всего позиций: 4")""",
    "io-49": """фам = input()
имя = input()
отч = input()
print(фам + " " + имя + " " + отч)
print(фам)""",
    "io-50": """день = input()
u1 = input()
u2 = input()
u3 = input()
print("День: " + день)
print("1) " + u1)
print("2) " + u2)
print("3) " + u3)""",
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
    "numbers-31": """км = int(input())
print(50 + 15 * км)""",
    "numbers-32": """м = int(input())
print(м // 60)
print(м % 60)""",
    "numbers-33": """n = 528
print(n // 100)""",
    "numbers-34": """цена = int(input())
скидка = int(input())
print(цена * (100 - скидка) / 100)""",
    "numbers-35": """n = int(input())
print(n - 1)
print(n)
print(n + 1)""",
    "numbers-36": """n = int(input())
print(n // 100)
print((n // 10) % 10)
print(n % 10)""",
    "numbers-37": """t = int(input())
print(t // 3600)
print((t % 3600) // 60)
print(t % 60)""",
    "numbers-38": """n = int(input())
print(n // 100 + (n // 10) % 10 + n % 10)""",
    "numbers-39": """n = int(input())
print(n // 100)
n = n % 100
print(n // 10)
print(n % 10)""",
    "numbers-40": """a = int(input())
b = int(input())
c = int(input())
print(1000 - (a + b + c))""",
    "numbers-41": """n = int(input())
print(n // 1000)
print((n // 100) % 10)
print((n // 10) % 10)
print(n % 10)""",
    "numbers-42": """n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
print(c * 100 + b * 10 + a)""",
    "numbers-43": """n = int(input())
print(n // 7)
print(n % 7)""",
    "numbers-44": """h = int(input())
m = int(input())
add = int(input())
total = h * 60 + m + add
print((total // 60) % 24)
print(total % 60)""",
    "numbers-45": """n = int(input())
print((n * n) % 100)""",
    "numbers-46": """a = int(input())
d = int(input())
n = int(input())
print(a + (n - 1) * d)""",
    "numbers-47": """a = int(input())
b = int(input())
print(a * 100 / b)""",
    "numbers-48": """a = int(input())
b = int(input())
print(2 * a * b / (a + b))""",
    "numbers-49": """n = int(input())
print(n // 500)
n = n % 500
print(n // 100)
n = n % 100
print(n // 10)
print(n % 10)""",
    "numbers-50": """n = int(input())
print(n // 1000 + (n // 100) % 10 + (n // 10) % 10 + n % 10)""",
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
    "cond-31": """x = int(input())
a = int(input())
b = int(input())
print('в диапазоне' if a <= x <= b else 'вне диапазона')""",
    "cond-32": """a = int(input())
b = int(input())
c = int(input())
if b >= a and b >= c:
    print('второе')
elif a >= b and a >= c:
    print('первое')
else:
    print('третье')""",
    "cond-33": """a = int(input())
b = int(input())
print('делится' if a % b == 0 else 'не делится')""",
    "cond-34": """a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('возможен')
else:
    print('невозможен')""",
    "cond-35": """o1 = int(input())
o2 = int(input())
d = o1 - o2 if o1 >= o2 else o2 - o1
print('скачок' if d >= 2 else 'стабильно')""",
    "cond-36": """x = int(input())
y = int(input())
if x == 0 or y == 0:
    print('ось')
elif x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')""",
    "cond-37": """age = int(input())
if age < 6:
    print(0)
elif age < 18:
    print(500)
elif age < 60:
    print(1000)
else:
    print(700)""",
    "cond-38": """y = int(input())
if y % 400 == 0:
    print('високосный')
elif y % 100 == 0:
    print('обычный')
elif y % 4 == 0:
    print('високосный')
else:
    print('обычный')""",
    "cond-39": """a = int(input())
b = int(input())
if a <= b:
    print(a)
    print(b)
else:
    print(b)
    print(a)""",
    "cond-40": """n = int(input())
a = n // 100000
b = (n // 10000) % 10
c = (n // 1000) % 10
d = (n // 100) % 10
e = (n // 10) % 10
f = n % 10
if a + b + c == d + e + f:
    print('счастливый')
else:
    print('обычный')""",
    "cond-41": """a = input()
b = input()
if a == b:
    print('ничья')
elif (a == 'камень' and b == 'ножницы') or (a == 'ножницы' and b == 'бумага') or (a == 'бумага' and b == 'камень'):
    print('первый')
else:
    print('второй')""",
    "cond-42": """x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 <= x <= x2 and y1 <= y <= y2:
    print('да')
else:
    print('нет')""",
    "cond-43": """a = int(input())
b = int(input())
c = int(input())
mn = a
if b < mn:
    mn = b
if c < mn:
    mn = c
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
mid = a + b + c - mn - mx
print(mn)
print(mid)
print(mx)""",
    "cond-44": """age = int(input())
score = int(input())
if age >= 14 and score >= 70:
    print('да')
else:
    print('нет')""",
    "cond-45": """h = int(input())
m = int(input())
if 0 <= h <= 23 and 0 <= m <= 59:
    print('верно')
else:
    print('ошибка')""",
    "cond-46": """a = int(input())
b = int(input())
if a > b:
    print('первый')
elif b > a:
    print('второй')
else:
    print('ничья')""",
    "cond-47": """a = int(input())
b = int(input())
c = int(input())
d = b * b - 4 * a * c
if d > 0:
    print('положительный')
elif d == 0:
    print('ноль')
else:
    print('отрицательный')""",
    "cond-48": """money = int(input())
price = int(input())
qty = int(input())
if money >= price * qty:
    print('хватает')
else:
    print('не хватает')""",
    "cond-49": """n = int(input())
if n == 0:
    print('ноль')
elif n < 0:
    print('отрицательное')
elif n % 2 == 0:
    print('положительное чётное')
else:
    print('положительное нечётное')""",
    "cond-50": """x = int(input())
a = int(input())
b = int(input())
lo = a
hi = b
if b < a:
    lo = b
    hi = a
if lo <= x <= hi:
    print('внутри')
else:
    print('снаружи')""",
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
    "while-36": """n = int(input())
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
print(s)""",
    "while-37": """n = int(input())
p = 1
while p <= n:
    print(p)
    p = p * 2""",
    "while-38": """n = int(input())
d = 1
count = 0
while d <= n:
    if n % d == 0:
        count = count + 1
    d = d + 1
if count == 2:
    print('простое')
else:
    print('составное')""",
    "while-39": """n = int(input())
steps = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    steps = steps + 1
print(steps)""",
    "while-40": """n = int(input())
c = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        c = c + 1
    n = n // 10
print(c)""",
    "while-41": """n = int(input())
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if orig == rev:
    print('да')
else:
    print('нет')""",
    "while-42": """n = int(input())
c = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        c = c + 1
    n = n // 10
print(c)""",
    "while-43": """a = int(input())
b = int(input())
x = a
y = b
while y != 0:
    t = x % y
    x = y
    y = t
print(a * b // x)""",
    "while-44": """n = int(input())
while n > 9:
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    n = s
print(n)""",
    "while-45": """n = int(input())
mx = 0
while n > 0:
    digit = n % 10
    if digit > mx:
        mx = digit
    n = n // 10
print(mx)""",
    "while-46": """n = int(input())
while n % 2 == 0:
    n = n // 2
if n == 1:
    print('да')
else:
    print('нет')""",
    "while-47": """n = int(input())
a = 1
b = 1
print(a)
while b <= n:
    print(b)
    t = a + b
    a = b
    b = t""",
    "while-48": """n = int(input())
c = 0
while n % 2 == 0:
    n = n // 2
    c = c + 1
print(c)""",
    "while-49": """n = int(input())
p = 1
while n > 0:
    p = p * (n % 10)
    n = n // 10
print(p)""",
    "while-50": """n = int(input())
s = 0
i = 0
while s <= n:
    i = i + 1
    s = s + i
print(i)""",
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
    "for-36": """n = int(input())
p = 1
for i in range(1, n + 1, 1):
    p = p * i
print(p)""",
    "for-37": """n = int(input())
s = 0
for i in range(1, n + 1, 1):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print(s)""",
    "for-38": """n = int(input())
count = 0
for d in range(1, n + 1, 1):
    if n % d == 0:
        count = count + 1
if count == 2:
    print('простое')
else:
    print('составное')""",
    "for-39": """n = int(input())
s = ""
for i in range(1, n + 1, 1):
    s = s + str(i)
    print(s)""",
    "for-40": """n = int(input())
s = 0
for i in range(1, n + 1, 1):
    if i % 2 == 0:
        s = s - i
    else:
        s = s + i
print(s)""",
    "for-41": """n = int(input())
s = 0
for d in range(1, n, 1):
    if n % d == 0:
        s = s + d
if s == n:
    print('совершенное')
else:
    print('нет')""",
    "for-42": """n = int(input())
for x in range(2, n + 1, 1):
    c = 0
    for d in range(1, x + 1, 1):
        if x % d == 0:
            c = c + 1
    if c == 2:
        print(x)""",
    "for-43": """n = int(input())
m = int(input())
for i in range(0, n, 1):
    print('*' * m)""",
    "for-44": """a = int(input())
b = int(input())
m = a
if b < a:
    m = b
ans = 1
for d in range(1, m + 1, 1):
    if a % d == 0 and b % d == 0:
        ans = d
print(ans)""",
    "for-45": """n = int(input())
c = 0
for i in range(1, n + 1, 1):
    if i * i <= n:
        c = c + 1
print(c)""",
    "for-46": """n = int(input())
for i in range(1, n + 1, 1):
    if i % 4 == 0 and i % 6 != 0:
        print(i)""",
    "for-47": """n = int(input())
p = 1
for i in range(1, n + 1, 1):
    p = p * i
    print(p)""",
    "for-48": """n = int(input())
s = 0
for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        s = s + j
print(s)""",
    "for-49": """n = int(input())
count = 0
for x in range(2, n + 1, 1):
    c = 0
    for d in range(1, x + 1, 1):
        if x % d == 0:
            c = c + 1
    if c == 2:
        count = count + 1
print(count)""",
    "for-50": """n = int(input())
for i in range(n, 0, -1):
    print('*' * i)""",
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
    "str-31": """s = input()
v = 'аеиоуыэюя'
c = 0
for ch in s:
    if ch in v:
        c = c + 1
print(c)""",
    "str-32": """s = input()
print('палиндром' if s == s[::-1] else 'не палиндром')""",
    "str-33": """s = input()
print('[' + s + ']')""",
    "str-34": """s = input()
print(s + s)""",
    "str-35": """s = input()
print(s[::-1])""",
    "str-36": """s = input()
print(s[0])
print(s[-1])""",
    "str-37": """s = input()
print(s.replace(" ", ""))""",
    "str-38": """s = input()
if s[0] == s[-1]:
    print('да')
else:
    print('нет')""",
    "str-39": """s = input()
res = ""
for ch in s:
    res = res + ch + ch
print(res)""",
    "str-40": """s = input()
vowels = "аеиоуыэюя"
res = ""
for ch in s:
    if ch not in vowels:
        res = res + ch
print(res)""",
    "str-41": """s = input()
vowels = "аеиоуыэюя"
c = 0
for ch in s:
    if ch not in vowels:
        c = c + 1
print(c)""",
    "str-42": """s = input()
if len(s) == 1:
    print(s)
else:
    print(s[-1] + s[1:-1] + s[0])""",
    "str-43": """a = input()
b = input()
if len(a) >= len(b):
    print(a)
else:
    print(b)""",
    "str-44": """parts = input().split()
print(parts[0][0] + parts[1][0] + parts[2][0])""",
    "str-45": """s = input()
vowels = "аеиоуыэюя"
res = ""
for ch in s:
    if ch in vowels:
        res = res + "*"
    else:
        res = res + ch
print(res)""",
    "str-46": """s = input()
for ch in s:
    print(ch)""",
    "str-47": """s = input().lower()
if s == s[::-1]:
    print('палиндром')
else:
    print('не палиндром')""",
    "str-48": """parts = input().split()
c = 0
for w in parts:
    if len(w) > 3:
        c = c + 1
print(c)""",
    "str-49": """parts = input().split()
print(parts[-1])""",
    "str-50": """s = input()
n = len(s)
if n % 2 == 1:
    print(s[n // 2])
else:
    print(s[n // 2 - 1] + s[n // 2])""",
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
    "list-31": """числа = [1, 2, 3, 4]
rev = []
for x in числа:
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
    print('ошибка')""",
    "list-34": """nums = [1, 2, 3, 4, 5]
nums.pop()
nums.pop(0)
print(nums)""",
    "list-35": """nums = [10, 20, 30, 40, 50]
for i in range(0, len(nums), 2):
    print(nums[i])""",
    "list-36": """nums = [1, 2, 3, 4, 5, 6]
s = 0
for x in nums:
    if x % 2 == 0:
        s = s + x
print(s)""",
    "list-37": """a = [15, 3, 42, 7]
a.sort()
print(a[-2])""",
    "list-38": """nums = [10, 20, 30, 40]
first = nums.pop(0)
nums.append(first)
print(nums)""",
    "list-39": """nums = [2, 3, 4]
p = 1
for x in nums:
    p = p * x
print(p)""",
    "list-40": """nums = [4, 5, 3, 5, 4]
s = 0
for x in nums:
    s = s + x
avg = s / len(nums)
c = 0
for x in nums:
    if x > avg:
        c = c + 1
print(c)""",
    "list-41": """a = [1, 2, 3, 4]
b = [3, 4, 5, 3]
for x in a:
    if x in b:
        print(x)""",
    "list-42": """nums = [1, 2, 3, 4]
res = []
s = 0
for x in nums:
    s = s + x
    res.append(s)
print(res)""",
    "list-43": """nums = [10, 20, 30, 40]
last = nums.pop()
nums.insert(0, last)
print(nums)""",
    "list-44": """nums = [2, -3, 5, -1, 0]
res = []
for x in nums:
    if x < 0:
        res.append(0)
    else:
        res.append(x)
print(res)""",
    "list-45": """a = [15, 3, 42, 7]
a.sort()
print(a[1])""",
    "list-46": """nums = [3, 9, 4, 9, 1]
mx = nums[0]
idx = 0
i = 0
for x in nums:
    if x > mx:
        mx = x
        idx = i
    i = i + 1
print(idx)""",
    "list-47": """nums = [1, 2, 3, 4, 5, 6]
odd = []
for x in nums:
    if x % 2 != 0:
        odd.append(x)
print(odd)""",
    "list-48": """nums = [2, 3, 4, 5]
i = 0
while i < len(nums) - 1:
    print(nums[i] * nums[i + 1])
    i = i + 1""",
    "list-49": """nums = [1, 5, 3]
mx = nums[0]
for x in nums:
    if x > mx:
        mx = x
for x in nums:
    print(mx - x)""",
    "list-50": """nums = [1, 2, 3, 4, 5]
even = []
odd = []
for x in nums:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
even.extend(odd)
print(even)""",
}

from data.fix_tasks_defs import FIX_TASK_DEFS

for _topic_id, _defs in FIX_TASK_DEFS.items():
    for _fix in _defs:
        _base_id = _fix["based_on"]
        if _base_id in REFERENCE_SOLUTIONS:
            REFERENCE_SOLUTIONS[_fix["id"]] = REFERENCE_SOLUTIONS[_base_id]

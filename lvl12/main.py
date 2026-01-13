# def sum(x: int, y: int) -> int:
#     return x + y
#
# # 1. Можна зберігати функцію в змінну
# suma = sum # alias
# suma(1,2)
#
# def print_func(func, *args, **kwargs):
#     print(func(*args, **kwargs))
#
# # 2. Можна передавати функцію як аргумент
# print_func(suma, x=1, y=2)
#
#
# # 3. Можна повертати функцію з функції
# def calculator(action):
#     def add(a, b):
#         return a + b
#
#     def sub(a, b):
#         return a -b
#
#     if action == "add":
#         return add
#     elif action == "sub":
#         return sub
#
# func = calculator("add")
# print(func(10, 5))
# print(func(10, 123))
# print(func(10, -12))
#
#
# # 4. Можна використовувати функції як аргументи в колекціях
# functions = [suma, func, "string"]
# for func in functions:
#     if callable(func):
#         print(func(10, 5))
# import time
#
#
#
# # id() - повертає ідентифікатор об'єкта
# a = [1, 2]
# b = a
# c = [1, 2]
#
# print(id(a) == id(b))  # True (це той самий об’єкт)
# print(id(a) == id(c))
#
#
# hash() — хеш-значення (працює для “хешованих” типів: str, int, tuple...)
# print(hash("hello"))
# print(hash(123))
# print(hash((1, 2, 3)))
# print(hash([1, 2, 3]))  # помилка: list не хешується
#
# dir() — список атрибутів/методів об’єкта
# text = "hi"
# print(dir(text))
# print("upper" in dir(text))  # True
#
# # без аргументів — що є в поточній області видимості
# x = 10
# print("x" in dir())  # True
#
# suma = lambda  x,y: x+y
# print(suma(10,15))
#
# is_even = lambda n: n % 2 == 0
# print(is_even(10))  # True
# print(is_even(7))   # False
#
#
# # map() — застосувати функцію до кожного елемента
# nums = [1, 2, 3, 4]
# squares = map(square, nums)
# print(squares)
# print(list(squares))  # [1, 4, 9, 16]
#
# def square(num):
#     return num * num
#
# squares = []
# for num in nums:
#     squares.append(square(num))
#
#
# filter(condition, collection) — залишити тільки те, що проходить умову
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4, 6]
#
#
# words = ["banana", "kiwi", "apple", "date"]
# by_len = sorted(words, key=lambda w: len(w))
# print(by_len)  # ['kiwi', 'date', 'apple', 'banana']
#
#
# import string
# for l in string.ascii_letters:
#     print(l, ord(l))
#
#
# def create_multiplier(factor):
#     """Створює функцію, яка множить на заданий коефіцієнт"""
#     def multiplier(x):
#         return x * factor
#     return multiplier
#
# # Створюємо різні функції-множники
# multiply_by_2 = create_multiplier(2)
# multiply_by_5 = create_multiplier(5)
# multiply_by_10 = create_multiplier(10)
#
# # Використовуємо створені функції
# print(f"5 * 2 = {multiply_by_2(5)}")
# print(f"3 * 5 = {multiply_by_5(3)}")
# print(f"7 * 10 = {multiply_by_10(7)}")
#
#
# def create_validator(min_value, max_value):
#     """Створює функцію для валідації значень у заданому діапазоні"""
#     def validator(value):
#         return min_value <= value <= max_value
#     return validator
#
# # Створюємо різні валідатори
# age_validator = create_validator(0, 120)
# percentage_validator = create_validator(0, 100)
# temperature_validator = create_validator(-50, 50)
#
# # Тестуємо валідатори
# print(f"Вік 25 валідний: {age_validator(25)}")
# print(f"Вік 150 валідний: {age_validator(150)}")
# print(f"Відсоток 85 валідний: {percentage_validator(85)}")
# print(f"Температура -60 валідна: {temperature_validator(-60)}")
#
# lst = [1,2,3]
# it_lst = iter(lst)
# print(next(it_lst))
# print(it_lst)
# for i in it_lst:
#     print(i)
#
#
# def infinite_output():
#     count = 1
#     while True:
#         yield count
#         count += 1
#
# counter = infinite_output()
#
# while True:
#     if not input():
#         print(next(counter), end="")
#     else:
#         break
#
#
# def read_lines(path):
#     with open(path, encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()
#
# counter = 0
# for line in read_lines("./file.txt"):
#     print(line)
#     counter += 1
#
#     if counter % 10 == 0:
#         if input():
#             break
#
#
# def chunks(data, size):
#     for i in range(0, len(data), size):
#         yield data[i:i + size]
#
#
# users = list(range(1, 101))
#
# for batch in chunks(users, 10):
#     print(batch)


# def order_status_flow():
#     yield "created"
#     yield "paid"
#     yield "shipped"
#     yield "delivered"
# status = order_status_flow()
# print(next(status))  # created
# print(next(status))  # paid
# print(next(status))  # paid
# print(next(status))  # paid


# def traffic_light():
#     while True:
#         yield "red"
#         yield "yellow"
#         yield "green"
#
#
# gen = traffic_light()
#
# import time
# for color in gen:
#     print(color)
#     time.sleep(1)
#
#     gen.close()

# def running_total():
#     total = 0
#     while True:
#         x = yield total
#         if x is None:
#             continue
#         total += x
#
#
# g = running_total()
# print(next(g))     # 0 (перший запуск до першого yield)
# print(g.send(5))   # 5
# print(g.send(10))  # 15


#
# def payment_monitor(initial_limit: int = 500):
#     limit = initial_limit
#     processed = 0
#
#     payload = yield {"type": "ready", "limit": limit}
#     while True:
#         # Команди керування приходять через send()
#         if isinstance(payload, dict) and payload.get("cmd") == "set_limit":
#             limit = int(payload["value"])
#             payload = yield {"type": "limit_updated", "limit": limit}
#             continue
#
#         if isinstance(payload, dict) and payload.get("cmd") == "reset":
#             processed = 0
#             payload = yield {"type": "reset_done"}
#             continue
#
#         # “Робочі” події: платежі/замовлення
#         order_id = payload.get("order_id")
#         amount = int(payload.get("amount", 0))
#         processed += 1
#
#         if amount >= limit:
#             payload = yield {
#                 "type": "ALERT",
#                 "order_id": order_id,
#                 "amount": amount,
#                 "limit": limit,
#                 "processed": processed,
#             }
#         else:
#             payload = yield {
#                 "type": "ok",
#                 "order_id": order_id,
#                 "amount": amount,
#                 "limit": limit,
#                 "processed": processed,
#             }
#
#
# mon = payment_monitor(500)
# print(next(mon))  # старт: {"type": "ready", "limit": 500}
#
# # Прилітають події:
# print(mon.send({"order_id": 101, "amount": 120}))
# print(mon.send({"order_id": 102, "amount": 700}))  # ALERT
#
# # Адмін/конфіг-сервіс змінив поріг "на льоту":
# print(mon.send({"cmd": "set_limit", "value": 1000}))
# print(mon.send({"order_id": 103, "amount": 700}))  # вже ok (бо поріг 1000)
#
# # Можна скинути статистику без створення нового генератора:
# print(mon.send({"cmd": "reset"}))
# print(mon.send({"order_id": 104, "amount": 1500}))  # ALERT при порозі 1000
#
# mon.close()


# def generator1():
#     yield from range(10)
#     yield from (1,2,3)
#     yield from [1,2,3]
#
#
# for value in generator1():
#     print(value)


#
# inventory = [
#     {"name": "Apple", "price": 15, "rating": 4.5},
#     {"name": "Banana", "price": 10, "rating": 4.0},
#     {"name": "Cherry", "price": 15, "rating": 4.8},
#     {"name": "Date", "price": 30, "rating": 3.5}
# ]
#
#
# print(sorted(inventory, key=lambda item: (item["price"], -item["rating"]) ))
#
# text = "Hello World 123"
#
# print(
#     list(
#         map(
#             lambda l:
#                 l.swapcase() if l.isalpha()
#                 else "*" if  l.isdigit()
#                 else l,
#             text
#         )
#     )
# )
#
#
# words = ["madam", "level", "python", "racecar", "data", "civic"]
#
# print(
#     list(
#         filter(
#             lambda word: word==word[::-1] and len(word)>4,
#             words
#         )
#     )
# )


def frange(start: int|float, stop: int|float, step: int|float = 0.1):
    while start < stop:
        yield start
        start = round(start + step, 2)



for i in frange(0.1, 1.8, 0.005):
    print(i)
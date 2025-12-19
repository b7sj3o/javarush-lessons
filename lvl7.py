# def print_sum(a, b):
#     """
#     Функція, яка виводить суму двох чисел.
#     """
#     print(f"Сума {a} і {b} рівна {a + b}")
#
# result = print_sum(100, 200)
# print_sum(-100, 120)

# from random import randint
#
# def deal_damage(hp, damage):
#     if randint(1,5) == 1:
#         damage *= 2
#
#     return hp - damage
#
# result = deal_damage(150, 50) # 100
# print(result)

# def shout(text):
#     return text.upper()
#
# # Присвоюємо функцію змінній
# yell = shout # alias
#
# print(yell("hello"))
# print(shout("hi"))

# def check_password(password):
#     if len(password) < 8:
#         return "Занадто короткий пароль "
#     return "Пароль прийнято"
#
# print(check_password("saw"))
# print(check_password("mystrongpassword"))

# PASS - нічого не робить
def future_function():
    pass

def future_function2():
    ...


# Створення декількох змінних через кому
# a, b, c = 10, 20, 30
#
# def get_user():
#     name = "Олесь "
#     age = 25
#     return name, age
#
# user_name, user_age = get_user()
# print(user_name, user_age) # Виведе: Олесь 25


# def greet_player(name="Unknown"):
#     print(f"Привіт, {name}")
#
# greet_player()
# greet_player("Alex")

# def print_user_info(name, age):
#     print(f"Ім'я: {name}, Вік: {age}, Повнолітній: {age >= 18}")
#
#
# user = {
#     "name": "Jim",
#     "age": 18,
# }
#
# print_user_info(**user)
# print_user_info(age=15, name="Jane")
# print_user_info("Jim", 30)


# name = "vitalik" # Глобальна
#
# print(name)
#
# def test():
#     name2 = "andriy" # Локальна
#
#     print(name2)
#
#     def inner():
#         name3 = "mykola" # Вкладена

# Порядок: Локальна -> Вкладена -> Глобальна -> Вбудована


# user_hp = 100
#
#
# def deal_damage(damage):
#     global user_hp
#     user_hp -= damage
#
# deal_damage(10)
# deal_damage(20)
#
# def outer():
#     """Функція -лічильник."""
#     count = 0
#
#     def inner():
#         """Вкладена функція."""
#
#         nonlocal count # Вказуємо, що хочемо змінити count із outer
#         count += 1
#         return count
#     return inner
#
# counter = outer() # Повертає inner
# print(counter()) # Виведе 1
# print(counter()) # Виведе 2


# def exam(subject):
#     min_score = 60  # правило іспиту
#
#     def check_student(name, score):
#         if score >= min_score:
#             print(f"{name} склав {subject}")
#         else:
#             print(f"{name} не склав {subject}")
#
#     check_student("Андрій", 75)
#     check_student("Оля", 50)
#
# exam("Математика")


# ARGS - tuple
# def sum_nums(*nums):
#     suma = 0
#     for num in nums:
#         suma += num
#     return suma
#
#
# print(sum_nums(1,5,7,8,2,2,5,67,8))


# KWARGS - dict
# def show_profile(**info):
#     for k, v in info.items():
#         print(k, v)
#
# show_profile(
#     name="Alex",
#     level=5,
#     hp=100,
#     tssawaswaws="wsaaswawsasw",
#     hey=123
# )

# items=("item1", "item2", "item3")
#
# print(items)
# print("item1", "item2", "item3")


def add(a: int, b: int) -> int:
    return a+b

result: int = add(10, 20)
# LIST: Змінюваний, неунікальний
random_lst = ["String", 25, [1,2,3], 2.52, True]
users = ["Andriy", "Matviy", "Mykola"]

# TUPLE (кортеж): Незмінний, неунікальний
coordinates = (100, 200)

# SET - Змінний, унікальний, зберігає лише незмінні типи даних
empty_set = set()
nums = {1, 2, 3, 4, 5}

# DICT (словник): ключі унікальні, змінний
user = {
    "name": "Andriy",
    "age": 25,
    "height": 1.78,
    "is_married": True,
}
# print(user["name"]) # Якщо немає - помилка
# print(user.get("name", "Невідомо")) # Якщо немає - None або вказане значення


# FROZENSET - незмінний, унікальний,  зберігає лише незмінні типи даних
permissions = frozenset(["read", "write"])

# dct = {
#     permissions: "123",
#     [1,2,3]: True # TypeError: unhashable type: 'list'
# }

#
# x = 1
#
# print(type(x)) # <class 'int'>
# print(type(users)) # <class 'list'>
# print(type(coordinates)) # <class 'tuple'>

# dict([
#     (1, 2),
#     (3, 4)
# ]) ->

# {
#     1: 2,
#     3: 4
# }

#
# name = "Maria"
#
# print(list(name)) # ["M", "a", "r", "i", "a"]
#
# for letter in name:
#     print(letter)


# BOOL
# age = 25
# is_adult = age > 18 # True


# and
# age = 25
# is_ticket_bought = True
# if age > 18 and is_ticket_bought:
#     print("Ви повнолтіній і купили квиток!")

# or
# is_card_brought = False
# is_security_recognized = False
#
# if is_card_brought or is_security_recognized:
#     print("Надано доступ!")


# not
# lights_on = True
# if not lights_on:
#     print("У вас темно")

# num1 = 10
# num2 = num1
# num2 += 20
#
# print(num1, num2)

# lst1 = [1,2,3]
# lst1[0] = 6
# print(lst1)

# name = "alex"
# name[0] = "Alex" # TypeError: 'str' object does not support item assignment

# 1 спосіб копії
# lst2 = lst1.copy()

# 2 спосіб копії
# lst2 = lst1[:]

# lst2.append(4)

# print(lst1, lst2)


result = True

lst1 = [1,2,3]
lst2= [1,2,3]

print([] is []) # порівнюються комірки
print(lst1 == lst2) # порівнюються значення елементів

if result is None:
    print("Ще не розраховано")


# def create_user(name, age=None):
#     if age is None:
#         age = 18
#     return {"name": name, "age": age}
#
#
# user_email = None
#
# if user_email is None:
#     ask_user_for_email()
# user = {
#     "name": "Alice",
#     "age": 25,
#     "is_admin": False
# }
#
# user2 = {
#     "name": "Vitalik",
#     "age": 30,
#     "is_admin": True
# }
#
#
# keys = ["name", "age", "city"]
# default_value = None
# person = dict.fromkeys(keys, None)
# print(person)
#
# fields = ["name", "age", "email"]
# user_field = dict.fromkeys(fields, None)
# print(user_field)
#
# dct = {
#     "user": None,
#     "age": None
# }

# -----

user = {
    "name": "Alice",
    "age": 25,
    "is_admin": True
}

# user2 = user.copy() # Повертає поверхневу копію словника
# print(user2)

# print(user.keys()) # dict_keys
# print(user.values()) # dict_values
# print(user.items()) # dict_items


# for key, value in user.items():
#     print(key, value)

# keys = user.keys()
# print(keys)
# user["city"] = "Kyiv"
# print(keys) # оновляється в реальному часі


# print(user.get("name", "Не знайдено")) # не рейзить, повертає default значення
# print(user["name"]) # рейзить KeyError якщо ключа не знайдено
#
# name = user.pop("name")
# print(name)
# print(user)

# user = {
#     "name": "Alice",
#     "age": 25,
#     "is_admin": True
# }
#
# print(user.popitem()) # ('is_admin', True)
# print(user.popitem()) # ('age', 25)
# print(user.popitem()) # ('name', 'Alice')
#
# print(user)

# user = {
#     "name": "Alice",
#     "age": 25,
#     "is_admin": True
# }
#
# del user["name"]
# print(user)
#
# user.clear()
# print(user)
#
# user = {
#     "name": "Alice",
#     "age": 25,
#     "is_admin": True,
# }
# user.setdefault("city")
# print(user)


# default_config = {
#     "theme": "light",
#     "lang": "en",
#     "debug": False,
# }
#
# user_config = {
#     "theme": "dark",
#     "debug": True
# }
#
# default_config.update(user_config)
# print(default_config)


# user = {
#     "name": "Alice",
#     "age": 25,
#     "admin": {
#         "is_admin": True,
#         "is_staff": True
#     }
# }
# user["admin"]["is_admin"] = False

# for key in user.keys():
#     print(key)
#
# for value in user.values():
#     print(value)
#
# for key, value in user.items():
#     print(key, value)

user = {
    "name": "Alice",
    "age": 25,
    "city": "lviv"
}

# key_to_find = "city"
# print(key_to_find in user) # шукаємо по ключах

#
# person = {"name": "Alice", "age": 25, "city": "New York"}
# value_to_find = 25
#
# if all(value == value_to_find for value in person.values()):
#     print(f"Значення {value_to_find} присутнє в словнику.")
# else:
#     print(f"Значення {value_to_find} відсутнє в словнику.")
#
# users = [
#     {"name": "Alice",'age': 25,},
#     {"name": "Alice2",'age': 15,},
#     {"name": "Alice3",'age': 19,},
# ]
#
# print(all(user.get("age") > 18 for user in users))

# lst = ["a", "b"]

# data = dict.fromkeys(lst, []) # В ЗНАЧЕННЯ ВСТАВЛЯЄМО ЛИШЕ НЕЗМІННІ ТИПИ ДАНИХ
# lst_data = list(data["a"])
# lst_data.append(1)
# data["a"] = tuple(lst_data)
# print(data)  # {'a': [1], 'b': [1]}

# data = {key: [] for key in lst}
# data["a"].append(1)
# print(data)

# user = {
#     "name": "Alice",
#     "age": 25,
#     "city": "lviv"
# }

# [(0, ("name", "Alice")), (1, ("age", 25)), (2, ("city", "lviv"))]
# for i, (key, value) in enumerate(user.items()):
#     print(i, key, value)

# squares = {x: x**2 for x in range(1, 6)}

# print(dict([(0, 1), (2,3)]))


# nested_pairs = [
#     [("a", 1), ("b", 2)], [("c", 3), ("d", 4)],
#     [("e", 5), ("f", 6)], [("h", 7), ("z", 8)]
# ]

# 1 варіант
# nested_dict = {
#     key: value
#     for sublist in nested_pairs
#     for key, value in sublist
# }
# print(nested_dict)
#
# # 2 варіант
# nested_dict = {}
# for sublist in nested_pairs:
#     for key, value in sublist:
#         nested_dict[key] = value
# print(nested_dict)

#
# dict1 = {"name": "John", "age": 30}
# dict2 = {"city": "New York", "country": "USA", "age": 35}
# combined_dict = {**dict1, **dict2}
# print(combined_dict)

# import json
# file = open("data.json", "r")
# data = json.load(file)
# print(data["electronics"]["laptops"]["prod_001"])

# user = {
#     "name": "Alice",
#     "address": {
#         "city": {
#             "country": "USA",
#             "name": "New York"
#         },
#         "zip": "1000"
#     }
# }

# рекурсивний метод витягнення всіх значень з вкладеного словника
# def get_all_values(dct: dict):
#     for value in dct.values():
#         if type(value) == dict:
#             get_all_values(value)
#         else:
#             print(value)
# get_all_values(user)


recipes = {
    frozenset({"борошно", "яйця", "молоко"}): "млинці",
    frozenset(["м'ясо", "картопля", "цибуля"]): "котлети з картоплею",
    frozenset(["помідори", "огірки", "зелень"]): "салат"
}

for k,v in recipes.items():
    print(f"Інгридієнти, щоб приготвувати {v}: {",".join(k)}")


# BIG O нотації
# Рекурсія
# JSON
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
#
# print(a.intersection(b)) # {4,5}
# print(a.symmetric_difference(b)) # {1,2,3,6,7,8}
# print(a.difference(b)) # {1,2,3}
# print(a.union(b)) # {1,2,3,4,5,6,7,8}
#
#
# # emails = [
# #     "test@gmail.com",
# #     "admin@gmail.com",
# #     "test@gmail.com",
# #     "info@gmail.com"
# # ]
# #
# unique_emails = list(set(emails))
# print(unique_emails)


# 2 різних хеші
# print(hash("a"))
# print(hash("A"))
#
# my_set = set()

# МЕТОДИ
users = {"Mykola", "Ivan", "Dmytro"}

# users.add("Nazar")
# print(users)

# users.remove("Nazar2") # KeyError якщо такого елементу немає
# print(users)
#
# try:
#     users.remove("Nazar")
# except KeyError:
#     print("Такого юзера немає")
#
# if "Nazar" not in users:
#     print("Такого юзера немає")
#
# users.discard("Ivan2") # Не rais-ить помилку, якщо такого елементу немає
# print(users)


# user = users.pop() # Повертає випадкове значення з сету
# print(user)
#
# users.clear()
# print(users)

# new_users = {"Viktoria", "Ivanna"}
# users.update(new_users)
# print(users)

# tuple, int, float, bool, str

# print(hash("hello"))
# print(hash("hello"))
# print(hash("hello"))

# ages = {14,17,20,21,25}
# valid_ages = {age for age in ages if age >= 18 }
# print(valid_ages)
#
# print(valid_ages.issubset(ages))
# print(valid_ages <= ages)

# def similarity_of_two_sets(set1: set, set2: set) -> tuple[float, float]:
#     len_set1 = len(set1)
#     len_set2 = len(set2)
#     intersection_amount = len(set1.intersection(set2))
#
#     intersection_percentage1 = round(intersection_amount / len_set1 * 100, 2)
#     intersection_percentage2 = round(intersection_amount / len_set2 * 100, 2)
#
#     return intersection_percentage1, intersection_percentage2
#
#
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8,9,10,11,12,13}
#
# print(similarity_of_two_sets(set1, set2))

# users = {"Mykola", "Ivan", "Dmytro"}
#
# for idx, num in enumerate(users):
#     print(idx, num)


# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
#
# # print(set1 | set2 | set3)
# print(set1 | set2)
# print(set1 - set2)
# print(set1 & set2)
# print(set1 ^ set2)

# text = "Hello, my name is Ivan"

# Повертає індекс підрядка (першого елементу) у рядку, якщо не знайдено: -1
# print(text.find("is")) # 15

# users = "Михайло Грушевський"
# start:stop(+1):step
# print(users[0]) # М
# print(users[1]) # и
# print(users[:3]) # Мих
# print(users[2:6]) # хайл
# print(users[::3]) # Мао...
# print(users[1:7:2]) # иал
# print(users[-1]) # й
# print(users[-3:]) # кий
# print(users[::-1]) # перевернули рядок

# МЕТОДИ РЯДКІВ
# some_text = "  Привіт   "
# print(some_text.strip()) # видаляє пробіли справа і зліва від рядка

# name = "привіт, мене звати Віталік привіт привіт"
# print(name.title())
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
#
# prices = "100,500,250, 600, 120, 100"
#
# print(prices.replace(" ", "").split(","))

# fruits = ["Банан", "Диня", "Вишні"]
#
# print(f"Список фруктів: {",".join(fruits)}")

def clean_guest_list(guest_list: list) -> list:
    return list(set(guests))


guests = ["Anna", "Oleg", "Anna", "Maria", "Oleg", "Ivan", "Anna"]
print(clean_guest_list(guests))


def count_symbols(text: str) -> int:
    text_set = set(text)
    text_set.discard(" ")
    return len(text_set)

print(count_symbols("hello world"))
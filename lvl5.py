# my_age = 50
# my_name = "Vitalik"
#
# print(f"Мені {my_age} років")
# print("Мене звати {}. Мені {} років".format(50, "Vitalik"))
# print("Мене звати {name}. Мені {age} років".format(age=my_age, name=my_name))
#
# person = {"name": "Alice", "age": 30}
#
# print("Мене звати {name}. Мені {age} років".format(**person))
#
# pi = 3.1415923213213
# print(f"Число п={pi:.2f}")
#
# money = 3.5
# print(f"Ціна становить ${money:.2f}")

# print("5", "6", "7", sep=", ")
#
# print("Привіт", end=", ")
# print("Світ", end="")
# print("!")

# players = ["Віталік", "Андрій", "Микола", "Марія"]
#
# for player in players:
#     print(player)
#
# print("Ми перерахували всіх гравців!")


# range(start, stop, step)

# ВІД 0 ДО 9
# for i in range(10):
#     print(i, end=" ")


# ВІД 10 ДО 20
# for i in range(10, 21):
#     print(i, end=" ")

# amount = int(input("Введіть до якого діапазону виведуться парні числа"))
#
# 0 2 4 6 8 10 12 14 16 18 20
# for i in range(0, amount+1, 2):
#     print(i, end=" ")

# 10 9 8 7 6 5 4 3 2 1
# for i in range(10, -1, -1):
#     print(i, end=" ")
#

# step = 0.1
# num = 1
# to_num = 2 + step
#
# while num <= to_num:
#     print(f"{num:.1f}")
#     num += step



# cookies = ["печення 1", "печення 2", "печення 3", "печення 4"]
#
# while cookies:
#     cookie = cookies.pop(0)
#     print(f"Я їм {cookie}")
#
# print(cookies)

# for cookie in cookies:
#     print(f"Я їм {cookie}")


# energy = 5
# while energy > 0:
#     energy -= 1
#     print(f"Пробігли коло, залишилось {energy} од. енергії")


# apples = ["хороше яблуко", "хороше яблуко", "гниле яблуко", "хороше яблуко"]
#
# for apple in apples:
#     if apple == "гниле яблуко":
#         print("Гниле яблуко знайдене, зупиняюсь")
#         break
#     print("Все добре, продовжуємо пошук гнилого яблука...")
#
#
# apples = ["хороше яблуко", "хороше яблуко", "гниле яблуко", "хороше яблуко"]
# count = 0
#
# for apple in apples:
#     if apple == "гниле яблуко":
#         print("Гниле яблуко знайдене")
#         continue
#     print("Все добре, продовжуємо пошук гнилого яблука...")
#     count += 1
#
# print(f"Хороших яблук знайдено: {count}")

#
# pockets = ["ліва", "права", "задня", "кишеня куртки"]
#
# for pocket in pockets:
#     if pocket == "задня ліва":
#         print(f"Я знайшов ключі в {pocket}!")
#         break
#
#     print(f"Кишеня: {pocket} - не знайшов ключі")
# else:
#     print("Я не знайшов ключі ні в одній з кишень")


# n = 5
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(f"{i}x{j}={i*j}", end=" ")
#     print()


# days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
# days = {
#     "Понеділок": ["Математика", "Фізкультура", "Культурознавство"],
#     "Вівторок": []
# }

# for day in days:
#     print(f"Сьогодні {day}")
#     for i in range(1, 5):
#         print(f"Пара {i}", end=", ")
#     print("\n")



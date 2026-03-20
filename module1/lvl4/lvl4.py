# ІНПУТ ЗАВЖДИ ПОВЕРТАЄ РЯДОК (str)
birthday = input("Введіть вашу дату народження: ")

print("Ваша дата народження: " + birthday)

age = int(input("Введіть ваш вік: "))
print(f"Ваш вік {age}")

height = 1.85
print(int(height)) # 1

name = "Віталік"
print("Ваше ім'я " + name + "!")
print(f"Ваше ім'я {name}!")

is_student = False
score = 70
print("Ваша оцінка " + str(score) + str(is_student))

height = float(input("Введіть ваш зріст: "))
print(f"Ваш зріст: {height}")

# int -> float
# 5 -> 5.0

# Округлення на певну кількість знаків після коми
print(round(1.23456, 2))

year = int(input("Введіть ваш рік народження"))

if 2025 - year >= 18:
    print("Ви повнолітній")
else:
    turn_18_in = 18 - (2025 - year)
    print(f"Вам буде 18 через: {turn_18_in} років")


age = int(input("Введіть ваш вік: "))
price = 100

if age < 12:
    if age < 6:
        price -= price * 0.5
    else:
        price -= price * 0.3
else:
    price -= price * 0.1

print(f"Ви купили товар за {price} грн")


age = int(input("Enter your age: "))

if age <= 6:
    print("Вам не можна дивитись Netflix")
elif age <= 14:
    print("Вам доступні мультфільми")
elif age <= 18:
    print("Вам доступні фільми 14+")
else:
    print("Ви можете дивитись будь-які жанри фільмів")


color = input("Введіть колір світлофору (red / yellow / green): ")

if color == "red":
    print("СТІЙ!")
elif color == "yellow":
    print("Приготуйся")
elif color == "green":
    print("Можна йти")
else:
    print("Невідомий сигнал")


score = int(input("Введіть вашу оцінку "))

result = "Здав!" if score >= 60 else "Не здав"

if score >= 60:
    result = "Здав!"
else:
    result = "Не здав"

print(f"Ваш результат: {result}")

age = 25
print("Привіт " + str(age) + " років")
print("Привіт", age, "років")
print(f"Привіт {age} років")
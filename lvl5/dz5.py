from random import randint

number_to_guess = randint(1, 100)
N = 7

for attempt in range(1, N+1):
    while True:
        user_input = input(f"Введіть число від 1 до 100 (спроба {attempt}): ")

        if not user_input.isdigit():
            print("Введіть валідне число!")
            continue

        if not 1 <= int(user_input) <= 100:
            print("Введіть число в межах від 1 до 100")
            continue

        break

    user_number = int(user_input)

    if user_number > number_to_guess:
        print("Загадане число менше!")
    elif user_number < number_to_guess:
        print("Загадане число більше!")
    else:
        print("Ви перемогли!")
        break
else:
    print(f"Ви програли! Загадане число: {number_to_guess}")




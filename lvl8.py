

# 1
# people: list = ["nazar", "andriy", "zahar", "zahar", 0, True]

# 2
# numbers = list({1,2,3})
# numbers2 = list((1,2,3,4,5))

# str_numbers = ["1", "2", "3", "4"]

# map - перетворює кожен елемент списку у заданий тип даних
# у цьому випадку - в int (ціле число)
# print(list(map(int, str_numbers)))

# print(list("hello")) # ['h', 'e', 'l', 'l', 'o']

# fruits = ["apple"]

# append() Додає елемент в кінець списку.
# fruits.append("banana")
#
# print(fruits)

# extend() Розширює список, додаючи в кінець усі елементи з вказаної послідовності.

# fruits2 = ["peach", "grape"]
#
# fruits.extend(fruits2)
#
# print(fruits)

# insert() Вставляє елемент на вказану позицію.

# fruits.insert(2, "pineapple")
#
# print(fruits)

# remove() Видаляє перше входження елемента.

# fruits.remove("grape") # ValueError якщо елементу немає у списку
# print(fruits)


# pop() Видаляє елемент за індексом і повертає його.

# fruit = fruits.pop(0) # IndexError - якщо елемента на такій позиції н еіснує
# print(fruit)
# print(fruits)

# clear() Видаляє всі елементи зі списку.

# fruits.clear()
# print(fruits)

# del - видаляє змінні, зрізи, певні елементи списку тощо.
# del fruits[0]
# print(fruits)


# index() Повертає індекс першого входження елемента.
# nums = [1,6,612,252, 623,121]
# print(nums.index(121))

# count() Підраховує кількість входжень елемента в списку.
# groups = ["group1", "group2", "group1", "group3", "group1", "group1"]
# print(groups.count("group1"))
# print(groups.count("group2"))
# print(groups.count("group3"))

# sort() Сортує елементи списку на місці.
# nums = [6,2,5,1,3,6,7]
# nums.sort() # сортує вхідний масив і нічого не повертає
# print(nums)
#
# print(sorted(nums)) # повертає посортовану копію

# reverse() Перевертає елементи списку на місці.
# nums = [1,5,7,4,2]
# nums.reverse()
# print(nums)


# users = ["user1", "user2", "user3", "user4", "user5", "user6", "user7"]

# start:stop(+1):step
# print(users[0]) # user1
# print(users[1]) # user2
# print(users[:3]) # ['user1', 'user2', 'user3']
# print(users[2:6]) # ['user3', 'user4', 'user5', 'user6']
# print(users[::3]) # ['user1', 'user4', 'user7']
# print(users[1:7:2]) # ['user2', 'user4', 'user6']
# print(users[-1]) # взяття останього елементу (user7)
# print(users[-3:]) # ['user5', 'user6', 'user7']
# print(users[::-1]) # ['user7', 'user6', 'user5', 'user4', 'user3', 'user2', 'user1']

# Зміна частини списку за допомогою зрізів
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Заміна елементів з 4 по 7 (включно) новими значеннями
# my_list[3:7] = [100, 200, 300]
# my_list[0] = 500
# my_list[1] = 200
# print(my_list)

# Виведе: [1, 2, 3, 100, 200, 300, 8, 9, 10]

# def is_palindrome(word: str) -> bool:
#     return word == word[::-1]

# people = ["Alex", "Bob", "Misha"]
#
# if "A" in people:
#     print("Алекс присутній")
# else:
#     print("Відсутній")
#
# print("hello " in "hello world")

users = [
    {
        "name": "Alex",
        "age": 20,
    },
    {
        "name": "Bob",
        "age": 15,
    },
    {
        "name": "Charlie",
        "age": 16,
    }
]

# for i in range(len(users)):
#     user = users[i]
#     if user["age"] < 18:
#         user["status"] = "underage"
#     else:
#         user["status"] = "overage"

#
# for idx, user in enumerate(users):
#     print(idx, user['name'])
#
people = ["Alex", "Bob", "Misha", "Charlie", "Mykola", "Marta"]

# 1 варіант
# lst2 = []
# for person in people:
#     lst2.append(person.upper())

# 2 варіант (List Comprehension)
lst2 = [person.upper() for person in people]
lst2.sort()
print(lst2)

# print(list(enumerate(people)))


# print(users)


lst1 = [[1, 2], [3, 4]]

# lst2 = list(lst1)
# lst2 = lst1[:]
# lst2 = lst1.copy()
print(lst2)
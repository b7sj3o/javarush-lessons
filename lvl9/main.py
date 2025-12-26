people = [
    {
        "first_name": "Bob",
        "last_name": "Doe",
        "age": 25,
    },
    {
        "first_name": "Tom",
        "last_name": "Hank",
        "age": 50,
    }
]


def get_person(last_name: str) -> tuple[str, int]:
    for person in people:
        if person["last_name"] == last_name:
            return person["first_name"], person["age"]


# name, age = get_person("Hank")
# print(name, age)

# nums = (1,2,3,4,5,6)
# a, *b, c, d = nums # a=1, b=[2,3,4], c=5, d=6
# print(a, b, c, d)


# nums = (1,2,6,7,8,21,51,12,1,2,5,121,12)
# users = ("Bob", "Tom", "Hank")
#
# print(nums.count(1))
# print(users.index("Tom"))
#
# print(type(users))

# users = ("user1", "user2", "user3", "user4", "user5", "user6", "user7")
#
# # start:stop(+1):step
# print(users[0]) # user1
# print(users[1]) # user2
# print(users[:3]) # ['user1', 'user2', 'user3']
# print(users[2:6]) # ['user3', 'user4', 'user5', 'user6']
# print(users[::3]) # ['user1', 'user4', 'user7']
# print(users[1:7:2]) # ['user2', 'user4', 'user6']
#
# print(users[-1]) # взяття останього елементу (user7)
# print(users[-3:]) # ['user5', 'user6', 'user7']
# print(users[::-1]) # ['user7', 'user6', 'user5', 'user4', 'user3', 'user2', 'user1']
#
#
# queue = ("Володимир", "Дмитро", "Іванна", "Микола")
# person = "Антон"
#
# queue_lst = list(queue)
# queue_lst.insert(2, person)
# queue = tuple(queue_lst)
#
# print(queue)
#
# nums = (1,2,3)
#
# nums_lst = list(nums)
# nums_lst.extend((4,5))
# nums = tuple(nums_lst)
# print(nums)

#
# nested_tuple = ((1,2,3), 1, [1,2,6], True)
# # (1, (1,2,3)), (2, (4,5,6), (3, (7,8,9))
# for count, el in enumerate(nested_tuple, start=1):
#     if type(el) == tuple:
#         ...
#     elif type(el) == int:
#         ...
#
# # Виведення порожнього
#
# nums = (1,2,3)
# nums_copy = nums # Це буде копія змінної nums, вона не буде посилатись на ту ж комірку
#
# from itertools import chain
#
# # Визначення вихідних кортежів
# tuple1 = (1, 2, 3)
# tuple2 = (4,5,6)
# tuple3 = (7,8,9)
#
# # Об'єднання кортежів за допомогою chain
# combined_tuple = tuple(chain(tuple1, tuple2, tuple3))
#
# print(combined_tuple)
#
# users = [
#     {
#         "id": 1,
#         "name": "Ivan",
#         "profile": {
#             "email": "ivan@example.com",
#             "settings": {
#                 "theme": "dark",
#                 "language": "ua"
#             }
#         }
#     },
#     {
#         "id": 2,
#         "name": "Anna",
#         "profile": {
#             "email": "anna@example.com",
#             "settings": {
#                 "theme": "light",
#                 "language": "en"
#             }
#         }
#     },
#     {
#         "id": 3,
#         "name": "Oleh",
#         "profile": {
#             "email": "oleh@example.com",
#             "settings": {
#                 "theme": "dark",
#                 "language": "pl"
#             }
#         }
#     }
# ]
#
# print(users[0]["profile"]["settings"]["language"]) # ua
#
# nums = [
#     [1,2,3],
#     [[1,2,3],5,6],
#     [7,8,9]
# ]
#
# print(nums[1][0][2]) # 3



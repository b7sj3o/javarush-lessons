import json

# json.dump() Object -> json file
# json.dumps() Object (python) -> str
# json.load() json file -> Object
# json.loads() str -> Object


data = {
    "name": "Bob",
    "age": 20,
    "is_alive": True,
    "achievements": ["ach1", "ach2", "ach3"],
    "address": {
    "ZIP": 12345,
    "name": "Львів"
    },
    "extra_data": None
}


# str_json = json.dumps(data, indent=4)
# print(str_json)


# with open("user.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4)


# obj = json.loads(str_json)
# print(obj["name"])


# with open("user.json", "r") as f:
#     loaded_data = json.load(f)
#     print(type(loaded_data))


# str_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
# print(str_json)


import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(response.status_code)
print(response.reason)
print(response.ok)


# print(json.dumps(dict(response.headers), indent=4))

# print(response.text) # Виводить тіло відповіді у вигляді тексту
# print(response.json()) # Виводить тіло відповіді у вигляді JSON
# print(response.content) # Виводить тіло відповіді у вигляді байтів


# params = {'userId': 2}
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
# print(response.json())


# import requests
data = {
'title': 'foo222',
'body': 'bar',
'userId': 1
}
# response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
# print(response.status_code)
# print(response.json())


#
# response = requests.put('https://jsonplaceholder.typicode.com/posts/1',
# json=data)
# print(response.status_code)
# print(response.json())
# DELETE-запит

# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)
# print(response.json())

# url = "https://api.github.com/users"
#
# while True:
#     username = input("Enter username: ")
#
#     if not username:
#         break
#
#     response = requests.get(f"{url}/{username}")
#     data = response.json()
#
#     if response.status_code == 404:
#         print("Користувача не знайдено")
#         continue
#
#     message = f"""
# Знайдено користувача: {data["name"]} ({data["login"]})
# Біо: {data["bio"]}
# Акаунт був створений: {data["created_at"]}
# """
#     print(message)

# import requests
# try:
#     response = requests.get('https://api.github.com/users/nonexistentuser') # Неіснуючий користувач
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"Помилка HTTP: {err}")
# except Exception as err:
#     print(f"Виникла інша помилка: {err}")
# else:
#     print("Запит виконано успішно!")


# import requests
# data = {
# 'name': 'John Doe',
# 'email': 'johndoe@example.com'
# }
# response = requests.post('https://httpbin.org/post', json=data)
# print(response.text)


# import requests
from requests.auth import HTTPBasicAuth
# # Аутентифікація за допомогою базової утентифікації
#
# response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
# print(response.text)


import requests
with requests.Session() as session:
    response = session.post('https://httpbin.org/post', auth=HTTPBasicAuth('user', 'pass'))
    response = session.get('https://httpbin.org/get')
    print(response.text)




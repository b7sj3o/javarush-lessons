import json
import requests
api_key = '8cd2171e43ebbc0903a42fdcf60b0f09'
def parse_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    # Парсимо відповідь
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"У місті {city} зараз {temperature}°C")
    else:
        print(response.status_code, response.reason)
        print(response.json())
        print("Помилка при отриманні даних про погоду.")
while True:
    parse_data(input(">>> "))
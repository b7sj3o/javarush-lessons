# 1. Підміна User-Agent
# headers = {
#     'User-Agent': ('Mozilla/5.0'
#                    ' (Windows NT 10.0; Win64; x64)'
#                    ' AppleWebKit/537.36 (KHTML, like Gecko)'
#                    ' Chrome/91.0.4472.124 Safari/537.36'
#    )
# }
#
# session = requests.Session()
# session.headers.update(headers) # Встановлюємо User-Agent для всієї сесії
#
# # Після першого запиту session збереже cookies
# # і автоматично надсилатиме їх з усіма наступними запитами.
# session.get('https://httpbin.org/headers')

import os

PYPPETEER_CHROMIUM_REVISION = '1263111'

os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# url = "https://www.youtube.com/results?search_query=python"
#
# session = HTMLSession()
# response = session.get(url)
#
# response.html.render()
#
# video_titles = [el.text for el in response.html.find('span.yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap')]
# print(video_titles)

# soup = BeautifulSoup(response.content, "html.parser")
#
# names = soup.select("span.yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap")
#
# for name in names:
#     print(name.text)
# session = HTMLSession()
#
# # Сайт з "нескінченною прокруткою"
# response = session.get('https://imgur.com/search?q=cats')
#
# # Прокручуємо сторінку 3 рази і чекаємо по 2 секунди після кожного прокручування
# response.html.render(scrolldown=8, sleep=2)
#
# # Тепер в HTML буде набагато більше зображень, ніж при початковому завантаженні
# image_urls = [img.attrs['src'] for img in response.html.find('img')]
# print(f"Знайдено {len(image_urls)} зображень.")

#
# url = (
#     "https://auto.ria.com/uk/search/"
#     "?search_type=1"
#     "&category=1"
#     "&all[0].any[0].state=10"
#     "&price[0]=1&price[1]=1000&price[2]=1200"
#     "&crashed=0&has_verified_VIN=1"
#     "&is_first_time=1&abroad=0"
#     "&customs_cleared=1"
#     "&page={page}&limit=20"
# )
#
# session = requests.Session()
#
# current_page = 1
# count = 0
#
#
# while True:
#     response = session.get(url.format(page=current_page-1), timeout=5)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     products = soup.select("a.link.product-card.horizontal")
#     count += len(products)
#
#     for product in products:
#         print(product.select_one("div.titleS").text)
#     print("----")
#
#     next_btn = soup.find("button", attrs={"title": "Next"})
#
#     if next_btn.get("disabled") is not None:
#         break
#
#     current_page += 1
#
# print(f"Знайдено {count} авто")




import requests_cache
import time

# Встановлюємо кешування для всіх запитів.
# Кеш зберігатиметься у файлі my_cache.sqlite і діятиме 1 годину.
requests_cache.install_cache('my_cache', expire_after=3600)

# Перший запит буде виконаний реально і займе час
start = time.time()
requests.get('https://httpbin.org/delay/2') # Імітація повільної відповіді
print(f"Перший запит: {time.time() - start:.2f} сек.")

# Другий запит до того ж URL буде взятий із кешу і виконається миттєво
start = time.time()
response = requests.get('https://httpbin.org/delay/2')
print(f"Другий запит: {time.time() - start:.2f} сек.")
print(f"Відповідь взято з кешу: {response.from_cache}")

requests_cache.uninstall_cache() # Вимикаємо кешування
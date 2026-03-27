import logging
import concurrent.futures

import requests
from bs4 import BeautifulSoup

from utils import verify_status_code, save_to_csv, save_to_excel


data = []

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s | %(filename)s:%(lineno)d')

def parse_page(page: str|int) -> BeautifulSoup:
    try:
        response = requests.get(f"https://auto.ria.com/uk/search/?search_type=1&category=1&all[0].any[0].brand=6&abroad=0&customs_cleared=1&page={page-1}&limit=100", timeout=8)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Щось пішло не так: {e}")
        exit()

    success, error_msg = verify_status_code(response)

    if not success:
        logging.error(error_msg)
        exit()

    return BeautifulSoup(response.text, "html.parser")

def parse_data(page: str|int):
    soup = parse_page(page)

    # prices = soup.find_all("p", class_="price_color")
    # items = soup.select("article.product_pod")
    prices = soup.select("span.common-text.titleM.c-green")

    for price in prices:
        print(price.text.strip()[:-2].replace("\xa0", ""))
    #
    # for item in items:
    #     price = float(item.select_one("div.product_price p.price_color").text.strip()[2:])
    #
    #     item_name = item.select_one("h3 a")
    #     name = item_name.get("title")
    #     link = item_name.get("href")
    #     data.append({"name": name, "price": price, "link": link})
    #
    # logging.info(f"Сторінка {page} оброблена...")



# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     executor.map(parse_data, range(1,6))

parse_data(page=1)

save_to_csv(
    filename="data.csv",
    data=data,
    fieldnames=["name", "price", "link"],
)
logging.info("Дані були збережені у файл data.csv")
save_to_excel(
    filename="data.xlsx",
    data=data,
)
logging.info("Дані були збережені у файл data.xlsx")


import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(service=ChromeService(executable_path="data/chromedriver.exe"))

driver.get("https://olx.ua")

prompt = input("Введіть промпт: ")
amount = int(input("Введіть кількість елементів, які потрібно знайти: "))

input_field = driver.find_element(By.ID, "search")
input_field.send_keys(prompt)
input_field.send_keys(Keys.ENTER)

# submit_btn = driver.find_element(By.NAME, "searchBtn")
# submit_btn.click()

time.sleep(5)

items: list[WebElement] = driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")

for item in items[:amount]:
    try:
        item_name: WebElement = item.find_element(By.CLASS_NAME, "css-hzlye5")
        item_price: WebElement = item.find_element(By.CLASS_NAME, "css-blr5zl")

        print(f"Товар: {item_name.text} ({item_price.text})")
    except NoSuchElementException:
        print(item)

driver.quit() # закриваємо браузер
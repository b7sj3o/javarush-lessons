import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(service=ChromeService(executable_path="data/chromedriver.exe"))

driver.get("https://testpages.eviltester.com/pages/forms/html-form/")


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

results_container = wait.until(
    EC.visibility_of_element_located((By.ID, "results"))
)

print("Контейнер з результатами успішно завантажено!")

time.sleep(5)
driver.quit()
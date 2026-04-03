import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(service=ChromeService(executable_path="data/chromedriver.exe"))

driver.get("https://testpages.eviltester.com/pages/forms/html-form/")

username_input : WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input : WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
textarea_input: WebElement = driver.find_element(By.CSS_SELECTOR, "textarea[name='comments']")
file_input: WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='filename']")
checkbox_input: WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='checkboxes[]'][value='cb1']")
radio_input: WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd1']")
multiple_select: WebElement = driver.find_element(By.CSS_SELECTOR, "select[name='multipleselect[]']")
one_select: WebElement = driver.find_element(By.CSS_SELECTOR, "select[name='dropdown']")
submit_btn: WebElement = driver.find_element(By.CSS_SELECTOR, "input[name='submitbutton']")

username_input.send_keys("admin")
time.sleep(1)
password_input.send_keys("12345")
time.sleep(1)
textarea_input.clear()
textarea_input.send_keys("Some text...")
time.sleep(1)
file_input.send_keys(r"C:\Users\admin\PycharmProjects\javarush\module2\lvl7\data\img.png")
time.sleep(1)
checkbox_input.click()
time.sleep(1)
radio_input.click()
time.sleep(1)

Select(multiple_select).select_by_index(0)
Select(multiple_select).select_by_index(1)

time.sleep(1)

Select(one_select).select_by_value("dd2")
time.sleep(1)

submit_btn.click()

driver.quit() # закриваємо браузер
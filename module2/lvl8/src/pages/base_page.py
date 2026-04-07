from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config.settings import settings


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.WAIT_TIMEOUT_SECONDS)


    def open(self, url: str) -> None:
        self.driver.get(url)


    def wait_for_all_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_for_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )


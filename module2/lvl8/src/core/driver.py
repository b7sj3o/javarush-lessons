import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from src.config.settings import settings
from src.core.logging import logger


def create_chrome_driver() -> WebDriver:
    if not os.path.exists(settings.DRIVER_PATH):
        raise FileNotFoundError(f"Chromedriver not found at: {settings.DRIVER_PATH}")

    options = Options()
    options.add_argument("--start-maximized")

    if settings.HEADLESS:
        options.add_argument("--headless")

    logger.info("Creating chrome driver")
    logger.info(f"Headless mode: {settings.HEADLESS}")
    logger.info(f"Path to driver: {settings.DRIVER_PATH}")

    driver = WebDriver(
        service=Service(settings.DRIVER_PATH),
        options=options
    )
    driver.set_page_load_timeout(settings.PAGE_LOAD_TIMEOUT_SECONDS)
    logger.info("Chrome driver created")

    return driver
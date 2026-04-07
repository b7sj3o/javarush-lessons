class Settings:
    BASE_URL = "http://books.toscrape.com/catalogue/page-45.html"
    DRIVER_PATH = "data/chromedriver.exe"
    OUTPUT_CSV_PATH = "books_data.csv"
    WAIT_TIMEOUT_SECONDS = 10
    PAGE_LOAD_TIMEOUT_SECONDS = 30
    HEADLESS = False

settings = Settings()
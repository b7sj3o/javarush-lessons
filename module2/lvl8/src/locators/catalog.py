from selenium.webdriver.common.by import By

class CatalogLocators:
    NEXT_BUTTON = (By.CSS_SELECTOR, "li.next > a")
    BOOK_CARD = (By.CSS_SELECTOR, "article.product_pod")
    BOOK_TITLE = (By.CSS_SELECTOR, "h3 a")
    BOOK_RATING = (By.CSS_SELECTOR, "p.star-rating")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
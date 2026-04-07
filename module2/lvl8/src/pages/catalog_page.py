from urllib.parse import urljoin

from selenium.common import NoSuchElementException

from src.models import Book
from src.pages.base_page import BasePage
from src.locators import CatalogLocators
from src.utils import word_to_number


class CatalogPage(BasePage):
    def extract_books(self) -> list[Book]:
        books: list[Book] = []
        book_cards = self.wait_for_all_elements(CatalogLocators.BOOK_CARD)

        for card in book_cards:
            title_element = card.find_element(*CatalogLocators.BOOK_TITLE)
            price_element = card.find_element(*CatalogLocators.BOOK_PRICE)
            rating_element = card.find_element(*CatalogLocators.BOOK_RATING)

            books.append(
                Book(
                    title=title_element.get_attribute("title").strip(),
                    price=price_element.text.strip(),
                    rating=word_to_number(rating_element.get_attribute("class"))
                )
            )

        return books

    def get_next_page_url(self) -> str | None:
        try:
            next_button = self.driver.find_element(*CatalogLocators.NEXT_BUTTON)
        except NoSuchElementException:
            return None

        return urljoin(self.driver.current_url, next_button.get_attribute("href"))
import csv

from src.core.logging import logger
from src.models import Book

class CSVExporter:
    HEADERS = ("title", "price", "rating")

    def export_books(self, books: list[Book], output_path: str) -> None:
        logger.info(f"Exporting {len(books)} books to '{output_path}'.")

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.HEADERS)

            for book in books:
                writer.writerow((book.title, book.price, book.rating))

        logger.info("CSV export completed.")
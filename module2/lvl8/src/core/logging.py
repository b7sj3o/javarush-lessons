import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Logging path
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def build_logger(
    name: str, level=logging.DEBUG, log_file: str = None, log_format: str = None
):
    """
    Повертає налаштований логер для модуля
    :param name: ім'я логера (__name__ модуля)
    :param level: рівень логування
    :param log_file: шлях до файлу (якщо None, лог лише в консоль)
    """

    logger = logging.Logger(name)
    logger.setLevel(level)
    logger.propagate = False

    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(log_format)

    if log_file:
        file_path = LOG_DIR / log_file
        if not os.path.exists(file_path.parent):
            os.makedirs(file_path.parent, exist_ok=True)

        file_path = LOG_DIR / log_file
        file_handler = RotatingFileHandler(
            filename=file_path,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = build_logger(
    name="scraper",
    log_file="scraper.log",
)
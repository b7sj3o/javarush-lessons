from src.core.logging import logger

def word_to_number(word: str) -> int:
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
    }

    try:
        word = word.split()[1].lower()
    except IndexError:
        logger.error(f"Couldn't get rating word: {word}")
        return 0

    return number_map.get(word, 0)


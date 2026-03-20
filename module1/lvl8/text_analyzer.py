# Очищення тексту
def clean_text(text: str) -> list[str]:
    punctuation = ".,!?"
    for char in punctuation:
        text = text.replace(char, "")
    return text.split()


# Аналіз слів
def analyze_words(words: list[str]) -> tuple[str, str, float]:
    if not words:
        return "", "", 0.0

    longest = words[0]
    shortest = words[0]
    total_length = 0

    for word in words:
        word_length = len(word)
        if word_length > len(longest):
            longest = word
        if word_length < len(shortest):
            shortest = word
        total_length += word_length

    average_length = round(total_length / len(words), 2)
    return longest, shortest, average_length


# Аналіз літер
def count_letters(text: str) -> tuple[int, int]:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if not char.isalpha():
            continue

        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count


# Перевірка слів-паразитів
def check_filler_words(words: list[str]) -> bool:
    fillers = ("ну", "коротше")
    for word in words:
        if word.lower() in fillers:
            return True
    return False


# Головна програма
def main():
    text = input("Введіть текст для аналізу:\n")

    words = clean_text(text)
    total_words = len(words)

    longest, shortest, avg_length = analyze_words(words)
    vowels, consonants = count_letters(text)
    has_fillers = check_filler_words(words)

    print("\n=== Результати аналізу ===\n")
    print("Всього слів:", total_words)

    if total_words > 0:
        print(f"Найдовше слово: '{longest}' ({len(longest)} літер)")
        print(f"Найкоротше слово: '{shortest}' ({len(shortest)} літер)")
        print("Середня довжина слова:", avg_length)

    print("Кількість голосних:", vowels)
    print("Кількість приголосних:", consonants)

    if has_fillers:
        print("УВАГА: Знайдено слова-паразити!")


main()

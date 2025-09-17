# Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
# Используйте для выполнения задачи lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
# Советы
# Работать с регистрами помогут методы строк lower/upper.
# Уникальными считаются буквы, которые повторяются только один раз (например строка «аа» будет содержать
# 0 уникальных букв).
# Пример:
from collections import Counter


def count_unique_characters(txt: str) -> int:
    # temp_list = []
    # filter_result = filter(lambda symbol: symbol.lower() not in temp_list and not temp_list.append(symbol), txt)
    # result = list(set(filter_result))
    letters = list(filter(lambda symbol: symbol.isalpha(), map(lambda x: x.lower(), txt)))
    counts = Counter(letters)
    unique_once = list(filter(lambda count: counts[count] == 1, counts))
    return len(unique_once)

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
# Вывод:
# Количество уникальных символов в строке: 5

def count_unique_characters(string):
    unique_chars = list(filter(lambda c: string.lower().count(c.lower()) == 1, string))
    return len(unique_chars)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
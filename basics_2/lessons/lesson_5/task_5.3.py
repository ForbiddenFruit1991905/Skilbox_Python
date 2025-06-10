# Задача 1. Улучшенная лингвистика 2
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
# который вводится уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя
# встречаются в тексте.

words_to_count = input("Введите три слова через пробел: ").split()
sentence_to_check = input("Введите строку для проверки: ")
# count = [0, 0, 0]
#
# for word in words_to_count:
#     count[words_to_count.index(word)] = sentence_to_check.count(word)
# # # или так:
count = [sentence_to_check.count(word) for word in words_to_count]
print(count)

# Вариант от скилбокса:
words = [input("Введите слово: ") for _ in range(3)]
text = input("Введите текст: ")
words_count = [text.count(word) for word in words]

print(words_count)
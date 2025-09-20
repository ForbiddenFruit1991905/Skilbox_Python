# Задача 1. Согласные
# Дан следующий текст:
# Even if they are djinns, I will get djinns that can outdjinn them.
# Используя регулярные выражения, напишите программу, которая выводит два списка:
# Первый содержит все слова, которые начинаются на гласную букву латинского алфавита (в этот раз
# слово может состоять и из одной буквы, например I).
# Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
# Для получения второго списка за основу используйте шаблон, которым вы получили первый список.
# Ещё небольшая подсказка: посмотрите, чем отличается символ * от символа +. Также, когда будете
# получать второй список, обратите внимание, на какой символ начинаются слова.
# Ожидаемый результат:
# Слова на гласную: ['Even', 'if', 'are', 'I', 'outdjinn']
# Слова на любой символ, кроме гласной: ['they', 'djinns', 'will', 'get', 'djinns', 'that', 'can', 'them']
import re


text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
pattern_vowels = r'\b[aeiouAEIOUyY]\w*'
result_1 = re.findall(pattern_vowels, text)
print(result_1)

pattern_consonants = r'\b[^aeiouAEIOUyY\W]\w*\s'
result_2 = re.findall(pattern_consonants, text)
print(result_2)
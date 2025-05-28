# Задача 4. Текстовый редактор.
# Продолжаем разрабатывать новый текстовый редактор. Теперь нам поручили
# написать для него код, который считает, сколько раз в тексте встречается
# любая выбранная буква или цифра (а не только буква «ы», как было в задаче
# 3 урока «Цикл for: итерирование по строке»).
# Что нужно сделать.
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N. Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определённом формате.
# Пример.
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1

def count_symbols(text, symbol_type):
    count = 0
    symbol_to_find = input(f"Какую {symbol_type} ищем? ")
    for symbol in text:
        if symbol == symbol_to_find:
            count += 1
    print(f"Количество повторений символа '{symbol_to_find}' в тексте: {count}")

def count_letters_or_digits(text):
    choice = int(input("Введите номер действия:\n1 - ищем цифру\n2 - ищем букву\n"))
    if choice == 1:
        count_symbols(text, "цифру")
    elif choice == 2:
        count_symbols(text, "букву")

txt = input("Введите текст: ")
count_letters_or_digits(txt)



# def count_letters_or_digits(text):
#     choice = int(input("Введите номер действия:\n1 - ищем цифру\n2 - ищем букву\n"))
#     if choice == 1:
#         count_d = 0
#         digit = input("Какую цифру ищем? ")
#         for symbol in text:
#             if symbol == digit:
#                 count_d += 1
#         print(count_d)
#         count_symbols(text, "цифру")
#
#     elif choice == 2:
#         count_l = 0
#         letter = input("Какую букву ищем? ")
#         for symbol in text:
#             if symbol == letter:
#                 count_l += 1
#         print(count_l)
#
# txt = input("Введите текст: ")
# count_letters_or_digits(txt)
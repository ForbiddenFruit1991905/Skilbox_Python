# Задача 1. Кубы и квадраты.
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом
# же диапазоне. Выведите списки на экран. Для генерации используйте list comprehensions
# (как и в следующих задачах).
# Пример:
# Левая граница: 5
# Правая граница: 10
# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

# def get_list_of_cubes(mult, i_cube):
#     return i_cube ** mult
#
# def get_list_of_squares(mult, i_square):
#     return i_square ** mult
#
# left_border = int(input("Левая граница: "))
# right_border = int(input("Правая граница: "))
#
# cubes_nums = [get_list_of_cubes(3, num) for num in range(left_border, right_border + 1)]
# print(f'Список кубов чисел в диапазоне от {left_border} до {right_border}: {cubes_nums}')
# squares_nums = [get_list_of_squares(2, num) for num in range(left_border, right_border + 1)]
# print(f'Список квадратов чисел в диапазоне от {left_border} до {right_border}: {squares_nums}')

# Задача 2. Сообщение.
# Илья решил безобидно подшутить над другом и написал программу для смартфона, которая
# при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному
# добавляет ещё один дополнительный.
# Пользователь вводит строку и дополнительный символ. Напишите программу, которая генерирует
# два списка: в первом списке каждый элемент — удвоенная буква первой строки, во втором списке
# каждый элемент — конкатенация элемента первого списка и дополнительного символа.
# Пример:
# Введите строку: привет
# Введите дополнительный символ: !
# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']

# def get_double_letters(mult, i_letter):
#     return i_letter * mult
#
#
# def get_glued_letters(symbol, i_letter):
#     return i_letter + symbol
#
# msg = list(input("Введите строку: "))
# new_symbol = input("Введите дополнительный символ: ")
# double_letters = [get_double_letters(2, i_letter) for i_letter in msg]
# print(f'Список удвоенных символов: {double_letters}')
# glued_letters = [get_glued_letters(new_symbol, i_letter) for i_letter in double_letters]
# print(f'Склейка с дополнительным символом: {glued_letters}')

# Задача 3. Повышение цен.
# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать,
# мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год —
# ещё на Y процентов.
# Напишите программу, которая получает на вход список цен на товары (вещественные числа, список
# генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости
# товаров за каждый год.
# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.21

def get_year_prices(percent, start_price):
    return (1 + percent / 100) * start_price

product_prices = int(input("Введите кол-во товаров: "))
first_percent = int(input("Повышение на первый год: "))
second_percent = int(input("Повышение на второй год: "))
prices = [float(input("Цена на товар: ")) for _ in range(product_prices)]
first_year = [get_year_prices(first_percent, i_price) for i_price in prices]
second_year = [get_year_prices(second_percent, i_price) for i_price in first_year]
print(f'Сумма цен за каждый год: {round(sum(prices), 2)}, {round(sum(first_year), 2)}, {round(sum(second_year), 2)}')
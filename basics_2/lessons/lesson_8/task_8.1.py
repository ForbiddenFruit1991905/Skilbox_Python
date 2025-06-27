# Задача 1. Challenge
# Обычно программисты любят, когда всё просто и понятно. Но Антон не из таких.
# Он любит устраивать себе челлендж, развиваться и сразу применять на практике то,
# что только что узнал. И в этот раз он подумал реализовать подсчёт факториала без
# использования циклов.
# Напишите функцию, которая считает факториал числа с помощью рекурсии.
# Кстати, в Python есть ограничение на количество рекурсивных вызовов. Попробуйте передать
# своей функции, например, число 1000 и посмотрите, что будет.
# import sys
#
#
# def get_factorial(some_number):
#     max_recursion = sys.getrecursionlimit()
#     if some_number >= max_recursion:
#         print(f"Внимание: число слишком большое для рекурсивного вычисления "
#               f"(лимит глубины рекурсии {max_recursion}).")
#         some_number = max_recursion - 1
#         print(f"Вычислим факториал для {some_number} вместо введённого.")
#
#     if some_number == 1 or some_number == 0:
#         return 1
#     minimum_number_factorial = get_factorial(some_number - 1)
#     return some_number * minimum_number_factorial
#
#
# number = int(input("Введите число: "))
# result = get_factorial(number)
# print(result)
from sys import flags


# Задача 2. Степень числа
# На одном из форумов, посвящённых программированию, пользователь выложил такой код для
# расчёта степени числа без использования циклов, ** и функции math.pow().
# Другие пользователи отметили, что это решение нерабочее и в нём есть ошибки. Исправьте
# это решение, не используя циклы, возведение в степень через ** и функцию math.pow().
# Правильный результат:
# Введите вещественное число: 1.5
# Введите степень числа: 5
# 1.5 ** 5 = 7.59375

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))


# Задача 3. Поиск элемента
# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней
# и найти нужный элемент. Для этого в программировании используются специальные алгоритмы поиска.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого
# ключа на экран.
# Пример 1:
# Искомый ключ: h2
# Значение: Здесь будет мой заголовок
# Пример 2:
# Искомый ключ: abc
# Такого ключа в структуре сайта нет.


def get_value(some_key, data):
    found = None
    for key in data.keys():
        if some_key == key:
            return data[some_key]

    for index_key, index_value in data.items():
        if isinstance(index_value, dict):
            found = get_value(some_key, index_value)
            if found:
                return found
    return found


key_to_find = input("Искомый ключ: ")
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
result = get_value(key_to_find, site)

if result:
    print(f'Значение: {result}')
else:
    print('Такого ключа нет')
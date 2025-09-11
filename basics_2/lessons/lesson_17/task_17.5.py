# Задача 1. Однострочный код
# Пользователь вводит неопределённое количество чисел. Напишите код, который запрашивает
# эти числа и сортирует их по возрастанию. Реализуйте решение в одну строку.
# Пример работы консоли:
# Введите числа: 5 8 4 1 0 3
# [0, 1, 3, 4, 5, 8]


# numbers = input('Введите числа через пробел: ')
# result =list(map(int, numbers.split(' ')))
# print(sorted(result))

# result = sorted(list(map(int, input('Введите числа через пробел: ').split(' '))))
# print(result)

# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов. Напишите код, который выводит
# на экран список этих символов, исключая цифры и буквы в верхнем регистре.
# Пример работы консоли:
# Введите строку: qWe456rtY
# ['q', 'e', 'r', 't']

# result = list(map(str, filter(lambda symbol: symbol.islower(), input('Введите строку: '))))
# print(result)


# Задача 3. Функция reduce
# Помимо map и filter, в Python есть ещё одна функция — reduce. Она применяет указанную двухаргументную
# функцию к элементам последовательности, сводя её к единственному значению. Однако используют reduce
# довольно редко. Начиная с третьей версии Python, эту функцию даже вынесли из встроенных функций в модуль
# functools.
# Пример кода с reduce:
# from functools import reduce
# from typing import List
#
#
# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
#
# numbers: List[int] = [0, 1, 2, 3, 4]
# print(reduce(my_add, numbers))
# Результат:
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10
# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
from functools import reduce


sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a "
                                                                                   "Catholic", "or had been"]

def counter(count: int, data: str):

    if 'was' in data:
        count += 1
    return count

print(reduce(counter, sentences, 0))

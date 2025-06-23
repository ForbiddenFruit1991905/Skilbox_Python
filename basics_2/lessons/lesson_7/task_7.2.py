# Задача 1. Создание кортежей.
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав
# тем самым третий кортеж. С помощью метода кортежа определите в нём количество нулей.
# Выведите на экран третий кортеж и количество нулей в нём.

# import random
#
#
# tuple_1 = tuple([random.randint(0, 6) for _ in range(10)])
# tuple_2 = tuple([random.randint(-5, 1) for _ in range(10)])
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
# print(tuple_3.count(0))

# Вариант от скилбокса
# import math
# import random
#
#
# def create_random_tuple(a, b, n):
#     return tuple([random.randint(a, b) for _ in range(n)])
#
#
# first = create_random_tuple(0, 5, 10)
# second = create_random_tuple(-5, 0, 10)
# third = first + second
# nulls_count = third.count(0)
# print(third, nulls_count)

# Задача 2. Цилиндр
# Андрей однажды уже писал функции для расчёта площади сферы и объёма шара. И теперь для
# своей курсовой работы ему пришлось связаться с цилиндрами.
# Пользователь вводит два значения: радиус и высоту. Напишите функцию для расчёта площади
# боковой поверхности цилиндра и его полной площади. Функция должна возвращать два эти значения.
# После этого в основной программе выводятся оба ответа в две строки.
# Площадь боковой поверхности (r — радиус, h — высота):
# side = 2 * pi * r * h
# Полная площадь (S — площадь круга, которая вычисляется по формуле pi * (r ** 2):
# full = side + 2 * S

# import math
#
#
# def find_side_and_full_area(r, h):
#     side = 2 * math.pi * r * h
#     full_area = side + 2 * (math.pi * (r ** 2))
#     return round(side, 2), round(full_area, 2)
#
# radius = int(input("Введите радиус: "))
# height = int(input("Введите высоту: "))
# result = find_side_and_full_area(radius, height)
# print(result)
# print(f'Площадь боковой поверхности: {result[0]}\nПолная площадь: {result[1]}')

# Задача 3. Неправильный код.
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный
# индекс и случайное значение, а затем по этим индексу и значению меняет сам кортеж. Функция
# должна возвращать кортеж и случайное значение.
# В основном коде функция используется два раза, и на экран два раза выводится новый кортеж
# и случайное значение. Причём второй раз выводится сумма первого случайного значения и второго.
# Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.

import random

def change(nums):
    index = random.randint(0, len(nums) - 1)
    value = random.randint(100, 1000)
    new_list = list(nums)
    new_list[index] = value
    return tuple(new_list), value


my_nums = 1, 2, 3, 4, 5
new_nums, rand_val_1 = change(my_nums)
print(f'{new_nums}\n{rand_val_1}')
new_nums, rand_val_2 = change(new_nums)
rand_val_2 += rand_val_1
print(f'{new_nums}\n{rand_val_2}')

# Вариант от скилбокса
# import random
#
#
# def change(nums):
#     index = random.randint(0, 5) % len(nums)
#     value = random.randint(100, 1000)
#     nums = list(nums)
#     nums[index] = value
#     return tuple(nums), value
#
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums_2, rand_val_2 = change(new_nums)
# rand_val += rand_val_2
# print(new_nums_2, rand_val)
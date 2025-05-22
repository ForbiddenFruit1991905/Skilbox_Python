# Задача 1. Грубая математика.
# В одном центре математического анализа работал практикант, который писал
# программы для расчёта функций. Однажды он очень устал и неправильно понял
# техническое задание, поэтому функции стали грубо рассчитываться.
# Его программа работает следующим образом: вводится последовательность из N
# вещественных чисел, при этом положительные числа округляются вверх, а
# отрицательные — вниз.
# Что нужно сделать.
# Напишите программу, которая выводит натуральный логарифм от числа, если оно
# положительное, и экспоненту в степени числа, если оно отрицательное.
# Пример.
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2 log(x) = 0.6931471805599453
# Введите число: -2.1
# x = -3 exp(x) = 0.049787068367863944
# Введите число: -5.9
# x = -6 exp(x) = 0.0024787521766663585
# import math
#
# nums = int(input("Введите кол-во чисел: "))
#
# for _ in range(nums):
#     num = float(input("Введите число: "))
#     if num > 0:
#         print(f"Число положительное, округленное до числа: {math.ceil(num)}, "
#               f"вычисляем натуральный логарифм: {math.log(math.ceil(num))}")
#     if num < 0:
#         print(f"Число отрицательное, округленное до числа: {math.floor(num)}, "
#               f"вычисляем экспоненту в степени числа: {math.exp(math.floor(num))}")

# download_size = 123
# download_speed = 27
# procent = 0
# # {procent}
# for sec in range(1, (download_size // download_speed) + 2):
#     # procent += 100 / (download_size // download_speed)
#     print(f"Прошло {sec} сек. Скачано {download_speed} из {download_size} -  %")
#     download_speed += 27

import math

download_size = 1230
download_speed = 27
size_range = math.ceil(download_size / download_speed)
procent = 0
if download_size < 0 or download_speed < 0:
    print("Размер обновления и скорость соединения не могут быть меньше нуля.")
else:
    for sec in range(1, size_range + 1):
        procent = math.ceil(100 * (download_speed / download_size))
        print(f"Прошло {sec} сек.Скачано {download_speed} из {download_size} - {procent} %")
        download_speed += 27
        if download_speed > download_size:
            download_speed = download_size
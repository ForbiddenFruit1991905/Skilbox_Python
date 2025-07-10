# Пример 1
# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# print()
# sym_count_str = '\n'.join(sym_count)
# print(sym_count_str)
# print(', '.join(sym_count))
# speakers_file.close()
#
# counts_file = open('sym_count.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.write('\n' + str(50))
# counts_file.close()


# Пример 2
# import os
#
#
# def find_file(cur_path, file_name):
#     print('переходим', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('     смотрим', path)
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print('это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# file_path = find_file(os.path.abspath
#                       (os.path.join('..', 'basics_2', '..', 'lesson_9')),
#                       'task_9.2.py')
# # history_file = open('search_history.txt', 'w')
# history_file = open('search_history.txt', 'a')
# if file_path:
#     print('Абсолютный путь к файлу:', file_path)
#     history_file.write(file_path + '\n')
# else:
#     print('Файл не найден.')
# history_file.close()


# Домашнее задание
# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
# Содержимое файла answer.txt
# 20

# import random
#
#
# def sequence_in_file(numbers):
#     sequence_file = open('numbers.txt', 'w', encoding='utf-8')
#     for index_number in numbers:
#         sequence_file.write(str(index_number) + '\n')
#     sequence_file.close()
#
#
# def get_total():
#   file_to_read = open('numbers.txt', 'r', encoding='utf-8')
#     count = 0
#     for index_number in file_to_read:
#         count += int(index_number)
#     file_to_read.close()
#     return str(count)
#
#
# def write_in_file():
#     write_total_in_file = open('answer.txt', 'w', encoding='utf-8')
#     total_str = get_total()
#     write_total_in_file.write(total_str)
#     write_total_in_file.close()
#     return total_str
#
#
# random_numbers = [random.randint(1, 10) for _ in range(5)]
# sequence_in_file(random_numbers)
# result_total = get_total()
# print(result_total)
# result = write_in_file()
# print("Число для записи:", result)


# Задача 2. Всё в одном
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город,
# и там у него случилась беда: его диск пришлось отформатировать, а доступ в интернет
# отсутствует. Остался только телефон с мобильным интернетом. Так как со связью (и с
# памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые
# у вас сейчас есть.
# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в
# файл scripts.txt, разделяя код строкой из 40 символов *.
# Пример содержимого файла scripts.txt:
# import platform
# import sys
#
# info = 'OS info is \n{}\n\nPython version is {} {}'.format(
#     platform.uname(),
#     sys.version,
#     platform.architecture(),
# )
# print(info)
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#     file.write(info)
# ****************************************
# print("Введите первую точку")
# x1 = float(input('X: '))
# y1 = float(input('Y: '))
# print("\nВведите вторую точку")
# x2 = float(input('X: '))
# y2 = float(input('Y: '))
# print("Уравнение прямой, проходящей через эти точки:")
# x_diff = x1 - x2
# y_diff = y1 - y2
# if x_diff == 0:
#     print("x = ", x1)
# elif y_diff == 0:
#     print("y = ", y1)
# else:
#     k = y_diff / x_diff
#     b = y2 - k * x2
#     print("y = ", k, " * x + ", b)
# ****************************************

import os


def copy_files(current_path):
    new_path = open('scripts.txt', 'w', encoding='utf-8')
    for index_element in os.listdir(current_path):
        path = os.path.join(current_path, index_element)
        if os.path.isfile(path) and path.endswith('.py'):
            new_file = open(path, 'r', encoding='utf-8')
            for index_file in new_file:
                line = index_file.rstrip('\n')
                if len(line) == 40:
                    new_path.write('*********************\n')
                new_path.write(index_file)
            new_file.close()
    new_path.close()


files_path = os.path.abspath(os.path.join('..', 'basics_2', '..', 'lesson_9'))
copy_files(files_path)

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
# if file_path:
#     print('Абсолютный путь к файлу:', file_path)
# else:
#     print('Файл не найден.')


# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура
# его диска: папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить,
# какой тип иконки вставить.
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь (на
# директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает
# на файл, то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути
# на существование.
# Подсказка: для вывода размера файла поищите соответствующий метод.
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует

# import os
#
#
# def check_file(some_path, filename):
#     print('Переходим', some_path)
#     if not os.path.isdir(some_path):
#         return None
#     for index in os.listdir(some_path):
#         path = os.path.join(some_path, index)
#         print(f'Путь: {path}')
#
#         if filename == index and os.path.isfile(path):
#             print('Это файл')
#             file_size = os.path.getsize(path)
#             return f"Размер файла: {file_size} байт"
#         elif os.path.isdir(path):
#             print('Это директория')
#             result = check_file(path, filename)
#             if result:
#                 return result
#         elif os.path.islink(path):
#             print('Это ссылка')
#             link_size = os.lstat(path).st_size
#             return f"Размер ссылки: {link_size} байт"
#         else:
#             print('Указанного пути не существует')
#
#     return None
#
#
#
# file_path_1 = check_file(os.path.abspath
#                       (os.path.join('..', 'basics_2', '..', 'lesson_9')),
#                       'task_9.2.py')
# print(file_path_1)


# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
# Однако, как мы понимаем, файлов с таким названием может быть несколько.
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по
# всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

import os


def find_file(current_path, filename):
    print(f'Ищем в: {current_path}')
    print(f'Имя файла: {filename}')
    for index_element in os.listdir(current_path):
        path = os.path.join(current_path, index_element)
        print("Проверяется путь", path)
        if index_element == filename:
            print('\nНайдены следующие пути:', os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, filename)
            if result:
                return result
    return None


file_path = find_file(os.path.abspath
                      (os.path.join('..')),
                      'task_9.2.py')

if file_path is None:
    print("Файл не найден")
else:
    print(file_path)
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

import os


def check_file(some_path, filename):
    print('Переходим', some_path)
    if not os.path.isdir(some_path):
        return None
    for index in os.listdir(some_path):
        path = os.path.join(some_path, index)
        print(f'Путь: {path}')

        if filename == index and os.path.isfile(path):
            print('Это файл')
            file_size = os.path.getsize(path)
            return f"Размер файла: {file_size} байт"
        elif os.path.isdir(path):
            print('Это директория')
            result = check_file(path, filename)
            if result:
                return result
        elif os.path.islink(path):
            print('Это ссылка')
            link_size = os.lstat(path).st_size
            return f"Размер ссылки: {link_size} байт"
        else:
            print('Указанного пути не существует')

    return None



file_path_1 = check_file(os.path.abspath
                      (os.path.join('..', 'basics_2', '..', 'lesson_9')),
                      'task_9.2.py')
print(file_path_1)
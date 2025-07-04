# Задача 1. Сисадмин.
# Вы работаете системным администратором в одной компании. На диске каждого сотрудника
# компании в специальной папке access лежит файл admin.bat. Этот файл предназначен для
# вас, и вам нужен путь до этого файла, причём как относительный, так и абсолютный. Недолго
# думая, вы решили написать небольшой скрипт, который закинете по сети к этому файлу.
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
# Относительный путь до файла: Skillbox\access\admin.bat

import os

# file_name = 'admin.bat'
# folder_name = 'access'
#
# rel_path = os.path.join('Skillbox', folder_name, file_name)
# print(rel_path)
#
# abs_path = os.path.abspath(file_name)
# print(abs_path)


# Задача 2. Содержимое
# Выберите любую директорию на своём диске и затем напишите программу, выводящую на экран абсолютные
# пути к файлам и папкам, которые находятся внутри этой директории.
# Результат программы на примере директории проекта python_basic:
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
#     G:\PycharmProjects\python_basic\Module15
#     G:\PycharmProjects\python_basic\Module16
#     G:\PycharmProjects\python_basic\Module17
#     G:\PycharmProjects\python_basic\Module18
#     G:\PycharmProjects\python_basic\Module19
#     G:\PycharmProjects\python_basic\Module20
#     G:\PycharmProjects\python_basic\Module21
#     G:\PycharmProjects\python_basic\Module22

# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     for index_elem in os.listdir(project):
#         path = os.path.join(project, index_elem)
#         print('     ', path)
#
#
# project_list = ['basics_2', 'basics_2\lessons\lesson_8']
# for index_project in project_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', '..', index_project))
#     print_dirs(path_to_project)


# Вариант от скиллбокса:
# for path in os.listdir('..'):
#     print(os.path.join(os.path.abspath('..'), path))


# Задача 3. Корень диска.
# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
# Результат программы на примере диска G:
# Корень диска: G:\\


current_dir = os.getcwd()
drive, _ = os.path.splitdrive(current_dir)
root = drive + os.sep

print(f"Корень диска: {root}")
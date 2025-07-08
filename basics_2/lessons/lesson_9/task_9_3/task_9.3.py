# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# Вариант 1
# data = speakers_file.read()
# print(data)
# Вариант 2
# for i_line in speakers_file:
#     print(i_line, end='')
#
# speakers_file.close()

# Задача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
# Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt.txt) — в
# папке Additional_info.
# Содержимое файла group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30
# Содержимое файла group_2.txt.txt
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15
# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы
# и напоследок — произведение очков уже второй группы.
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось,
# этот код просто не работает. Вот что он написал:

# import os
#
#
# print(os.listdir())
#
# current_dir = os.path.abspath(os.getcwd())
# print("Текущая директория:", current_dir)
#
# path_to_first = os.path.join(current_dir, 'group_1.txt')
# path_to_second = os.path.join(current_dir, 'additional_info', 'group_2.txt')
#
#
# file = open(path_to_first, 'r', encoding='utf-8')
# file_2 = open(path_to_second, 'r', encoding='utf-8')
#
# summa = 0
# diff = 0
# compose = 1
#
# for i_line in file:
#     info = i_line.split()
#     if len(info) > 2:
#         summa += int(info[2])
#         diff -= int(info[2])
#
# for i_line in file_2:
#     info = i_line.split()
#     if len(info) > 2:
#         compose *= int(info[2])
#
# file.close()
# file_2.close()
#
# print(summa)
# print(diff)
# print(compose)
# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте
# файлы group_1.txt и group_2.txt.txt.


# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту.
# Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри
# указанного пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно
# сгенерировать случайно).
# Подсказка: можно использовать, например, список для сохранения найденного пути.

import random
import os


def find_file(current_path, filename):
    all_paths = []
    print(f'Ищем в: {current_path}')
    print(f'Имя файла: {filename}')
    for index_element in os.listdir(current_path):
        path = os.path.join(current_path, index_element)
        print("Проверяется путь", path)
        if index_element == filename:
            all_paths.append(os.path.abspath(path))
            print('\nНайдены следующие пути:', os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, filename)
            if result:
                return all_paths.extend(result)
    return None



def check_file_inside(path_to_file):
    file = open(path_to_file, "r", encoding="utf8")
    for line in file:
        print(line)
    file.close()


file_path = find_file(os.path.abspath
                      (os.path.join('..')),
                      'task_9.3.py')

if file_path is None:
    print("Файл не найден")
else:
    print(file_path)

check_file_inside(random.choice(file_path))
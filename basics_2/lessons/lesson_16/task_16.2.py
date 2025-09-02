# Задача 1. Таймер
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера: функция должна
# работать с оператором with и замерять время работы вложенного кода.
# import time
# from collections.abc import Iterator
# from contextlib import contextmanager
#
# @contextmanager
# def timer() -> Iterator:
#     start = time.time()
#     try:
#         yield
#     finally:
#         print(time.time() - start)
#
# with timer() as t1:
#     print('Первая часть:')
#     val_1 = 100 * 100 ** 1000000
#
# with timer() as t2:
#     print('Вторая часть:')
#     val_2 = 200 * 200 ** 1000000
#
# with timer() as t3:
#     print('Третья часть:')
#     val_3 = 300 * 300 ** 1000000


# Задача 2. Директории
#
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет
# текущую рабочую директорию на новую. Функция должна быть контекст-менеджером. Также реализуйте
# обработку ошибок (например, если такого пути не существует). Вне зависимости от результата выполнения
# контекст-менеджера нужно возвращаться в изначальную рабочую директорию.
# Пример основного кода:
# with in_dir('C:\\'):
#     print(os.listdir())
# Результат:
# <тут все папки из вашего диска C>
from contextlib import contextmanager
import os


@contextmanager
def in_dir(some_path):
    old_path = os.getcwd()
    try:
        os.chdir(some_path)
        yield
    except FileNotFoundError:
        print("Файл не найден, проверьте путь и имя файла.")
    finally:
        os.chdir(old_path)


with in_dir(r'D:\SKILLBOX\PYTHON\lections\basics_2\lessons\lesson_15') as path:
    print(os.listdir())
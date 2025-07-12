# Задача 1. Пятый элемент
# В курсе по программированию студенту дали простую задачу: умножить константу
# (число 42) на пятый элемент строки, введённой пользователем.
# Модифицируйте этот код, обработав исключения для произвольных входных параметров:
# ValueError — невозможно преобразовать к числу,
# IndexError — выход за границы списка,
# остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.
# Вот код студента:

# BRUCE_WILLIS = 42
# input_data = input('Введите строку: ')
# try:
#     Leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * Leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError as exc:
#     print(type(exc), "— невозможно преобразовать к числу")
# except IndexError as exc:
#     print(type(exc), "— выход за границы списка")
# except Exception as exc:
#     print(type(exc), "поймано исключение")


# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто
# использовать буквы алфавита) и выводит результат в новый файл result.txt в формате «имя
# — возраст». Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:
#   Попытка создания файла, который уже существует.
#   На чтение ожидался файл, но это оказалась директория.
#   Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

import random
import string


def generate_ages(ages):
    try:
        with open('ages.txt', 'w', encoding='utf-8') as file_to_write:
            for index in ages:
                if not isinstance(index, int):
                    print(f"Ошибка: значение '{index}' не является целым числом. Запись прервана.")
                    return
                file_to_write.write(str(index) + '\n')
        return ages
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def generate_names(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).title()


def get_user_info():
    try:
        with open('ages.txt', 'r', encoding='utf-8') as file_to_read, \
            open('result.txt', 'w', encoding='utf-8') as file_to_write:
                lines = file_to_read.readlines()
                result_dict = {}

                for line in lines:
                    age = line.strip()
                    if not age.isdigit():
                        print(f"Ошибка данных: '{age}' — не число")
                        return
                    name = generate_names(length=random.randint(3, 7))
                    result_dict[age] = name
                    file_to_write.write(f'{name} - {age}\n')

                print(result_dict)


    except FileNotFoundError:
        print("Ошибка: файл 'ages.txt' не найден.")
    except IsADirectoryError:
        print("Ошибка: ожидался файл, но получена директория.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


some_ages = [random.randint(1, 35) for _ in range(10)]
some_ages_check_error = [22, 'a', 11, 32, 16, 16, 17, 13, 11, 27]
some_names = [generate_names(random.randint(3, 7)) for _ in range(10)]
result_of_gen = generate_ages(some_ages)
result_of_gen_check_error = generate_ages(some_ages_check_error)
print(result_of_gen)
get_user_info()

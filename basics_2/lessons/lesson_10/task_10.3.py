# Задача 1. Простая программа.
# Напишите программу, которая открывает файл и записывает туда введённую пользователем
# строку. Используйте операторы try except else finally. Обработайте возможные ошибки:
    # Проблема при открытии файла.
    # Нельзя преобразовать данные в целое.
    # Неожиданная ошибка.

# def get_file_to_write(message):
#     try:
#         with open('some_file.txt', 'w', encoding='utf-8') as file_to_write:
#             for symbol in message:
#                 if not isinstance(symbol, int):
#                     print(f'Символ {symbol} не является целочисленным типом данных.')
#                     return
#                 file_to_write.write(str(symbol) + '\n')
#
#     except TypeError as e:
#         print(f"Произошла ошибка при записи в файл: {e} - тип данных не строка")
#     except FileExistsError:
#         print("Ошибка: файл 'some_file.txt' уже существует.")
#     except FileNotFoundError:
#         print("Ошибка: файл 'some_file.txt' не найден.")
#     except ValueError as e:
#         print(f"Ошибка: неверный режим открытия файла. {e}")
#     except OSError as e:
#         print(f"Ошибка ввода-вывода: {e}")
#     else:
#         print("Программа выполнилась без ошибок.")
#         return message
#     finally:
#         try:
#             print(f"Файл закрыт? {file_to_write.closed}")
#         except NameError:
#             print("Файл не был открыт, поэтому закрыть нечего.")
#
#
# some_text = input("Введите строку: ")
# get_file_to_write(some_text)

# Вариант от скилбокса:
import os

# file = None
# try:
#     file = open("23.3.txt", "w", encoding="utf8")
#     number = int(input("Введите текст: "))
#     file.write(str(number))
# except (FileNotFoundError, PermissionError) as exc:
#     print(type(exc), exc)
# except ValueError as exc:
#     print(type(exc), exc)
# except Exception as exc:
#     print(type(exc), exc)
# else:
#     print("Запись прошла без ошибок")
# finally:
#     if file and not file.closed:
#         file.close()


# Задача 2. Старая задача.
# Возьмите любую задачу из домашнего задания, например, предыдущего модуля и оформите её решение
# в виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
# Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос: когда стоит использовать
# обработку исключений и когда она будет излишней?

# Пример 1:

# def find_file(cur_path, file_name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# try:
#     find_file('c:\\', 'hello')
# except (TypeError, PermissionError) as exc:
#     print(exc, type(exc))

# Пример 2:

def copy_files(current_path):
    try:
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
    except FileExistsError:
        print("Ошибка: файл 'some_file.txt' уже существует.")

try:
    files_path = os.path.abspath(os.path.join('..', 'basics_2', '..', 'lesson_9'))
    copy_files(files_path)
except (TypeError, PermissionError) as exc:
    print(f"Ошибка типа или прав доступа: {exc} ({type(exc)})")
except FileNotFoundError:
    print('Файл или директория не найдены.')
else:
    print("Запись прошла без ошибок")
finally:
    print('Завершение работы программы.')
# Пример 1
from logging import exception

# sym_sum = 0
# line_count = 0
# try:
#     people_file = open('people.txt', 'r')
#     for i_line in people_file:
#         length = len(i_line)
#         line_count += 1
#         if i_line.endswith('\n'):
#             length -= 1
#         if length < 3:
#             raise BaseException("Длина {}-ой строки меньше 3 символов".format(line_count))
#         sym_sum += length
#     people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# finally:
#     print('Найденная сумма символов:', sym_sum)

# Пример 2

# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#             names_list = []
#             raise BaseException('Ты сломал программу!')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось.')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#     except BaseException:
#         names_list = []
#         print('Введено стоп слово.')
#         raise ValueError('Пожалуйста,не вводите стоп слово!')
#
# names_file = open('names.txt', 'w')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print('Программа закончена, запись завершена.')

# Задача 1. Имена
# В базе данных одной компании есть баг (или, может быть, фича): если
# ввести туда имя сотрудника меньше чем из трёх букв, то база сломается
# и упадёт. Как компания принимает на работу людей, например, с китайскими
# именами, непонятно.
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
# Напишите программу, которая берёт количество символов в каждой строке
# файла и в качестве ответа выводит общую сумму. Если в какой-либо строке
# меньше трёх символов (не считая литерала \n), то вызывается ошибка, и
# программа завершается.

# def check_length_of_names(file_to_read):
#     symbol_total = 0
#     try:
#         with open(file_to_read, 'r', encoding='utf-8') as read_file:
#             lines = read_file.readlines()
#             for line in lines:
#                 length = len(line)
#                 line = line.rstrip('\n')
#                 if len(line) < 3:
#                     raise ValueError("Длина строки меньше 3 символов")
#                 symbol_total += length
#
#     except FileNotFoundError:
#         print('Файл не найден.')
#     except ValueError as exc:
#         print(f'Ошибка: {exc}')
#     finally:
#         print('Найденная сумма символов:', symbol_total)
#
#
# file = 'people_list.txt'
# check_length_of_names(file)


# Задача 2. Логирование
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
# но и записывают эту ошибку в файл. Таким образом проще сформировать отчёт об ошибках,
# а значит, программисту будет проще их исправить. Это называется логированием ошибок.
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество
# слов, из которых можно получить палиндром (привет предыдущим модулям). Если в строке встречается
# число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log

def check_palindrome():
    palindrome_words = []
    try:
        with open('words.txt', 'r', encoding='utf-8') as read_file, \
            open('errors.txt', 'w', encoding='utf-8') as write_file:
            lines = read_file.readlines()
            for line in lines:
                word = line.rstrip('\n')
                try:
                    if any(symbol.isdigit() for symbol in word):
                        raise ValueError(f'Слово "{word}" содержит число.')

                    if word == word[::-1]:
                        palindrome_words.append(word)

                except ValueError as exp:
                    write_file.write(f'Ошибка: {exp}\n')

    except FileNotFoundError:
        print('Файл не найден.')

    return palindrome_words


result = check_palindrome()
print("Палиндромы:", result)

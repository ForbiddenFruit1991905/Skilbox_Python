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

names_list = []

while True:
    try:
        name = input('Введите имя: ')
        if name.lower() == 'error':
            names_list = []
            raise BaseException('Ты сломал программу!')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('Место закончилось.')
            break
    except TypeError:
        print('Ты чего ввёл?')
    except BaseException:
        names_list = []
        print('Введено стоп слово.')
        raise ValueError('Пожалуйста,не вводите стопслово!')

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена, запись завершена.')
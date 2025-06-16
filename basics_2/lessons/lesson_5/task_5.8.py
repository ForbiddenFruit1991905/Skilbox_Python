# Задача 1. Меню ресторана.
# Ресторан заказал вам приложение, которое в один клик отображает пользователю меню.
# Для работы ресторан предоставил вам свой сайт, где можно найти меню в виде идущих
# подряд названий блюд в нижнем регистре.
# Напишите программу, которая выводит меню на экран. На вход подаётся строка из названий
# блюд, разделённых точкой с запятой, а на выходе названия перечисляются через запятую и
# пробел. Все названия блюд должны начинаться с заглавной буквы.
# Пример:
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
# На данный момент в меню есть: Утиное Филе, Фланк-Стейк, Банановый Пирог, Плов

# def menu_available(menu):
#     nice_view_text = ", ".join(menu.split(';')).title()
#     return nice_view_text
# menu_access = input('Доступное меню: ')
# result = menu_available(menu_access)
# print(f'На данный момент в меню есть: {result}')

# Задача 2. Сжатие.
# Из-за увеличения объёма данных понадобилось сжать их, но так, чтобы не потерять важную информацию.
# Для этого было придумано специальное кодирование: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'. То есть
# группы одинаковых символов исходной строки заменяются на эти символы и количество их повторений в строке.
# Напишите программу, которая считывает строку, кодирует её, используя предложенный алгоритм, и выводит
# закодированную последовательность на экран. Код должен учитывать регистр символов.
# Пример:
# Введите строку: aaAAbbсaaaA
# Закодированная строка: a2A2b2с1a3A1

# def decode_text(text):
#     new_code = ''
#     count = 1
#
#     for i in range(1, len(text)):
#         if text[i] == text[i - 1]:
#             count += 1
#         else:
#             new_code += text[i - 1] + str(count)
#             count = 1
#     new_code += text[-1] + str(count)
#
#     return new_code
#
# text_code = input("Введите строку: ")
# result = decode_text(text_code)
# print(f'Закодированная строка: {result}')
#
# # Вариант от скилбокса:
# def text_coding(text):
#     count, result = 0, ""
#     for index, symbol in enumerate(text):
#         count += 1
#         if index == len(text) - 1 or symbol != text[index + 1]:
#             result += f'{symbol}{count}'
#             count = 0
#     return result
# user_text = input('Введите строку: ')
# print('Закодированная строка:', text_coding(user_text))

# Задача 3. Бегущая строка.
# В одной из практических работ вы писали программу для табло, которая циклически сдвигает элементы списка
# чисел вправо на K позиций. В этот раз вы работаете с двумя строками. Возможно, одна из строк немного сдвинута.
# Нужно проверить, не равна ли первая строка второй.
# Пользователь вводит две строки. Напишите программу, которая определяет, можно ли получить первую строку из второй
# циклическим сдвигом.
# По желанию: если строку получить можно, выведите значение сдвига.
# Пример 1
# Первая строка: abcd
# Вторая строка: cdab
# Первая строка получается из второй со сдвигом 2.
# Пример 2
# Первая строка: hello
# Вторая строка: lohel
# Первая строка получается из второй со сдвигом 3.
# Пример 3
# Первая строка: abcd
# Вторая строка: cdba
# Первую строку нельзя получить из второй с помощью циклического сдвига.

# def shift(sentence_1, sentence_2):
#     count = 0
#     for _ in range(len(sentence_2)):
#         sentence_2 = list(sentence_2[-1]) + sentence_2[:-1]
#         count += 1
#         if sentence_1 == sentence_2:
#             return f'Первая строка получается из второй со сдвигом {count}'
#
#     return 'Первую строку нельзя получить из второй с помощью циклического сдвига'
#
# first_sentence = list(input('Первая строка: '))
# second_sentence = list(input('Вторая строка: '))
# result = shift(first_sentence, second_sentence)
# print(result)

# Вариант от скилбокса:
# def shift_detection(first_text, second_text):
#     first_text *= 2
#     index = first_text.find(second_text)
#
#     if index != -1:
#         result = f"Первая строка получается из второй со сдвигом {index}"
#     else:
#         result = "Первую строку нельзя получить из второй с помощью циклического сдвига."
#     return result
# first_text = input('Первая строка: ')
# second_text = input('Вторая строка: ')
# print(shift_detection(first_text, second_text))

# Задача 4. Баги в программе.
# В IT-компании TechSolutions каждый отдел имеет свой уникальный IP-адрес для хранения файлов.
# Один из разработчиков по имени Константин недавно обновил программу для автоматического сохранения
# файлов на серверах с учётом IP-адресов. Однако из-за недочёта в коде часть IP-адресов и имён файлов
# записалась с ошибками.
# Когда сотрудники компании начали обращать внимание на несоответствие некоторых файлов, то обнаружили,
# что часть файлов с самыми длинными именами имеют ошибки.
# Вся информация по IP-адресам и именам файлов хранится в структуре данных data.
# Помогите Константину найти файлы с самыми длинными именами, которые не имеют ошибок, и составьте
# аналогичную структуру данных, но без недочётов. Используйте следующие критерии:
# IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
# Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
# Файл должен заканчиваться расширением .txt или .docx.
# Вывод в консоли
# Новая структура данных
# [
#     ['128.0.0.255', ['file_1.txt document_2024.docx notes2022.txt']]
#     ['192.168.1.10', ['file_432.txt  important_info.txt notes1900.txt']]
#     ['10.20.30.40', ['file_432.txt  analysis_results.txt notes1998.txt']]
# ]

def check_ip(ip_data):
    ip_parts = [parts[0].replace(',', '.') if ',' in parts[0] else parts[0] for parts in ip_data]
    ip_part = [ip_str.split('.') for ip_str in ip_parts]
    int_ip = [[int(ip_quarter) if ip_quarter.isdigit() else int(ip_quarter[1:]) for ip_quarter in ip] for ip in ip_part]
    check_num = [[-num_ip if num_ip < 0 else 255 if num_ip > 255 else num_ip for num_ip in int_ip_part] for int_ip_part
                 in int_ip]
    ip_finish = ['.'.join(str(num) for num in ip_nums) for ip_nums in check_num]

    return ip_finish


def find_right_data(addresses):
    bad_start = ["@", "№", "$", "%", "^", "&", "*", "()"]
    addresses_sublist = [parts[1][0].split(' ') for parts in addresses]
    file_index = [
        (
            filename_address if (filename_address.endswith('.txt') or filename_address.endswith('.docs'))
            else filename_address[:-5] + (
                '.docs' if ('d' in filename_address[-5:] or 'o' in filename_address[-5:])
                else '.txt' if ('t' in filename_address[-4:] or 'x' in filename_address[-4:])
                else '.txt'
            )
        ) if not any(filename_address.startswith(bad) for bad in bad_start)
        else filename_address[1:]
        for addresses in addresses_sublist
        for filename_address in addresses
    ]
    address_finish = [file_index[i:i + 3] for i in range(0, len(file_index), 3)]
    return address_finish


def changed_ip_files(addresses):
    fixed_ips = check_ip(data)
    fixed_files = find_right_data(data)
    combined = []
    for i in range(len(fixed_ips)):
        ip = fixed_ips[i]
        files = fixed_files[i]
        combined.append([ip, files])

    return combined


data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]

print(changed_ip_files(data))


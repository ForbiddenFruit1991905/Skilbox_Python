# Задача 1. Саботаж!
# Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и
# добавил в код сайта символ ~ (тильда). Но программисты быстро решили эту
# проблему, пройдясь по всему коду маленькой программой.
# Пользователь вводит строку. Напишите программу, которая проходит по строке
# и выводит в консоль индексы символа ~. Для решения этой задачи (и остальных тоже)
# используйте функцию enumerate.
# Пример:
# Строка: so~mec~od~e

# def find_index_tilda(text):
#     list_of_indexes = []
#     for index, symbol in enumerate(text):
#         if symbol == "~":
#             list_of_indexes.append(index)
#     return list_of_indexes
#
#
# def remove_tilda(text):
#     text_list = list(text)
#     for index in find_index_tilda(text):
#         for index_text, symbol_text in enumerate(text):
#             if index == index_text:
#                 text_list.remove(symbol_text)
#     return text_list
#
#
# some_text = input("Введите текст: ")
# result = find_index_tilda(some_text)
# remove_result = remove_tilda(some_text)
# print(result)
# print(remove_result)

# Вариант от скилбокса
# import random
#
#
# def get_indexes(where_to_search, what_to_search):
#     return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]
#
#
# text = input("Введите текст: ")
# print("Ответ:", " ".join(get_indexes(text, "~")))

# Задача 2. Словари из списков.
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
# Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
# Подсказка: random
# Пример:
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

# import random
#
#
# def random_dict(random_symbols):
#     dictionary = {}
#     for index, letter in enumerate(random_symbols, start=1):
#         dictionary[index] = letter
#     return dictionary
#
#
# russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# random_letters_1 = [random.choice(russian_letters) for _ in range(10)]
# random_letters_2 = [random.choice(russian_letters) for _ in range(10)]
# result_1 = random_dict(random_letters_1)
# result_2 = random_dict(random_letters_2)
# print(f'{result_1}\n{result_2}')

# Вариант от скилбокса
# def get_random_letter(n):
#     return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)
#
#
# first_letters = get_random_letter(10)
# second_letters = get_random_letter(10)
# print(first_letters)
# print(second_letters)
#
# first_dictionary = dict(enumerate(first_letters))
# second_dictionary = dict(enumerate(second_letters))
# print(first_dictionary)
# print(second_dictionary)


# Задача 3. Универсальная программа.
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
# При этом он предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки,
# списка, словаря), у которых индекс чётный.
# Пример 1:
# Допустим, есть такая строка: 'О Дивный Новый мир!'
# Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
# Пример 2:
# Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
# Результат: [100, 300, 0, 'а']
# Примечание: для проверки типа можно использовать функцию isinstance(<элемент>, <тип данных>),
# которая возвращает True, если элемент принадлежит к этому типу данных, и возвращает False в
# противном случае.

def even_symbols(text):
    new_list = []
    if isinstance(text, dict):
        text = text.values()
    for index, symbol in enumerate(text):
        if index % 2 == 0:
            new_list.append(symbol)

    return new_list


some_text_str = 'О Дивный Новый мир!' # input('Есть такая строка: ')
some_text_list = [100, 200, 300, 'буква', 0, 2, 'а'] # input('Есть такой список: ').split(', ')
data = {0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}
result_str = even_symbols(some_text_str)
print(result_str)
result_list = even_symbols(some_text_list)
print(result_list)
result_dict = even_symbols(data)
print(result_dict)

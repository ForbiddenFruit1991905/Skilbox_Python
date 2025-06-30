# Задача 1. Ошибка
# В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что старший
# разработчик быстро её нашёл и исправил. Он решил проверить, смогли бы вы её исправить,
# если бы его не было на месте. Поэтому он написал для вас код с аналогичной ошибкой:
# Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых
# равны ранее объявленным переменным. Затем вызывается функция, которая должна изменять
# значения словаря, добавляя к значениям случайное число, в зависимости от типа данных.
# Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку и убедитесь,
# что nums_list, some_dict и uniq_nums не меняются.

# import random
# import copy
#
# def change_dict(dct):
#     just_copy = copy.deepcopy(dct)
#     num = random.randint(1, 100)
#     for i_key, i_value in just_copy.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
# print(nums_list, some_dict, uniq_nums)

# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами
# и их id. Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых
# данных, информацию о его изменяемости, а также id этого объекта.
# Помните, что через input можно получить только строку, что бы вы ни вводили. В данном случае ввод
# можно выполнить вручную, просто вписав нужный объект в переменную, без использования функции input.
# Пример 1:
# data_input = "привет"
# Тип данных: <class 'str'> (строка)
# Неизменяемый (immutable)
# id объекта: 140013695242560
# Пример 2:
# data_input  = {"a": 10, "b": 20}
# Тип данных: <class 'dict'> (словарь)
# Изменяемый (mutable)
# id объекта: 140005763835136

data_names_dict = {
    "<class 'str'>": "строка",
    "<class 'dict'>": "словарь",
    "<class 'list'>": "список",
    "<class 'set'>": "множество"
}

mutable_check_helper = {
    "mutable": ("словарь", "список", "множество")
}


def check_info(data):
    type_of_data = type(data)
    name_of_data = ""
    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"
    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {type_of_data} ({name_of_data})")
    print(property_of_data)
    print("Id объекта:", id(data))


data_input_1 = "привет"
data_input_2  = {"a": 10, "b": 20}
check_info(data_input_1)
check_info(data_input_2)
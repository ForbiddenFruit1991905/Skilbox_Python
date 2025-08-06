# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
# Вариант 1

# import random
#
#
# class MyIterator:
#     def __init__(self, quantity):
#         self.quantity = quantity
#
#     def __iter__(self):
#         counter = 0
#         cur_val = random.uniform(0.0, 1.0)
#         while counter < self.quantity:
#             if counter == 0:
#                 yield round(cur_val, 2)
#             else:
#                 cur_val += random.uniform(0.0, 1.0)
#                 yield round(cur_val, 2)
#             counter += 1
#
#
# check_iter = MyIterator(6)
# print("Элементы итератора:")
# for i_index in check_iter:
#     print(i_index)

# Вариант 2

# def counter():
#     n = 0
#     while True:
#         n += 1
#         yield n
#
# def prime_numbers(nums):
#     prime_nums = []
#     for number in range(2, nums + 1):
#         for prime in prime_nums:
#             # if prime * prime > number:
#             #     break
#             if number % prime == 0:
#                 break
#         else:
#             prime_nums.append(number)
#             yield number
#
# gen = counter()
# for _ in range(50):
#     print(next(gen), end=' ')
# print()
#
# for index in prime_numbers(50):
#     print(index, end=' ')


# Задача 2. Очень большой файл
#
# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии
# компьютер просто зависает, так как данные не помещаются в оперативной памяти вашего суперкомпьютера
# (не очень-то и «супер»).
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
# которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.
import random


def generate_file():
    with open('numbers.txt', 'w', encoding='utf-8') as file_to_write:

        for _ in range(5):
            generate_nums = [str(random.randint(0, 10)) for _ in range(10)]
            line = ' '.join(generate_nums)
            file_to_write.write(line + '\n')


def read_file_to_find_total():
    with open('numbers.txt', 'r', encoding='utf-8') as file_to_read:
        total = 0
        for i_line in file_to_read:
            numbers_str = i_line.rstrip().split()
            numbers = [int(num) for num in numbers_str]
            total += sum(numbers)
        yield f"Общая сумма всех чисел в файле: {total}"


generate_file()
for line in read_file_to_find_total():
    print(line)
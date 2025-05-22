# Задача 1. Пирамидка.
# Напишите программу, которая получает на вход количество уровней пирамиды
# и выводит их на экран, заполняя нечётными числами:
#                 1
#             3       5
#         7       9       11
#     13      15      17      19
# 21      23      25      27      29

# height = int(input("Введите высоту пирамиды: "))
# curr_num = 1
#
# for row in range(height):
#     spaces = "\t" * (height - row)
#     line_row = ""
#     for _ in range(row + 1):
#         line_row += str(curr_num) + 2 * "\t"
#         curr_num += 2
#     print(spaces + line_row)

# Задача 2. Яма.
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта.
# Что нужно сделать.
# Напишите программу, которая получает на вход число N и выводит на экран числа
# в виде ямы:
# Введите число: 5
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

height = int(input("Введите высоту ямы: "))

for row in range(1, height + 1):
    spaces = "." * (height - row) * 2
    reverse_line = ""
    for i in range(height, height - row, -1):
        reverse_line = str(i) + reverse_line
        print(i, end="")
    print(spaces, end="")
    print(reverse_line, end="")
    print()

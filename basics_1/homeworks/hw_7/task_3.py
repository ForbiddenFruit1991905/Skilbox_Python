# Задача 3. Число наоборот.
# Что нужно сделать.
# Пользователь вводит два числа: N и K.
# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.
# Пример.
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321

def reversed_num(number):
    reversed_digits = ""
    for symbols in str(number):
        reversed_digits = symbols + reversed_digits
    return int(reversed_digits)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
res_1 = reversed_num(first_number)
res_2 = reversed_num(second_number)
print(f'Первое число наоборот: {res_1}')
print(f'Второе число наоборот: {res_2}')
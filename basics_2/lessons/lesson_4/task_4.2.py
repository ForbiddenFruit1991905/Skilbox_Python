# Задача 1. Кубы и квадраты.
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом
# же диапазоне. Выведите списки на экран. Для генерации используйте list comprehensions
# (как и в следующих задачах).
# Пример:
# Левая граница: 5
# Правая граница: 10
# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

def get_list_of_cubes(mult, i_cube):
    return i_cube ** mult

def get_list_of_squares(mult, i_square):
    return i_square ** mult

left_border = int(input("Левая граница: "))
right_border = int(input("Правая граница: "))

cubes_nums = [get_list_of_cubes(3, num) for num in range(left_border, right_border + 1)]
print(f'Список кубов чисел в диапазоне от {left_border} до {right_border}: {cubes_nums}')
squares_nums = [get_list_of_squares(2, num) for num in range(left_border, right_border + 1)]
print(f'Список квадратов чисел в диапазоне от {left_border} до {right_border}: {squares_nums}')
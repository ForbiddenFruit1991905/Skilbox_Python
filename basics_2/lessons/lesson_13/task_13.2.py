# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая
# эмулирует работу цикла for с помощью цикла while и проходит по всем элементам итерируемого
# объекта. Не забудьте про исключение «конца итерации».
import random


def my_iterator(some_sequence):
    my_iter = iter(some_sequence)
    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            break


numbers = [random.randint(0, 10) for _ in range(int(input("Введите количество чисел: ")))]
my_iterator(numbers)
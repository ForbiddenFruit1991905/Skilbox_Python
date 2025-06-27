# Задача 1. Challenge
# Обычно программисты любят, когда всё просто и понятно. Но Антон не из таких.
# Он любит устраивать себе челлендж, развиваться и сразу применять на практике то,
# что только что узнал. И в этот раз он подумал реализовать подсчёт факториала без
# использования циклов.
# Напишите функцию, которая считает факториал числа с помощью рекурсии.
# Кстати, в Python есть ограничение на количество рекурсивных вызовов. Попробуйте передать
# своей функции, например, число 1000 и посмотрите, что будет.
import sys


def get_factorial(some_number):
    max_recursion = sys.getrecursionlimit()
    if some_number >= max_recursion:
        print(f"Внимание: число слишком большое для рекурсивного вычисления (лимит глубины рекурсии {max_recursion}).")
        some_number = max_recursion - 1
        print(f"Вычислим факториал для {some_number} вместо введённого.")

    if some_number == 1 or some_number == 0:
        return 1
    minimum_number_factorial = get_factorial(some_number - 1)
    return some_number * minimum_number_factorial

number = int(input("Введите число: "))
result = get_factorial(number)
print(result)
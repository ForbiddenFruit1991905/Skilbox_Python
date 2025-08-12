# Задача 1. Как дела?
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор,
# который при вызове декорируемой функции спрашивает у пользователя: «Как дела?», вне зависимости от ответа
# пишет что-то вроде: «А у меня не очень!» — и только потом запускает саму функцию. Правда, после такой выходки
# Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
# Пример кода:
# from functools import wraps
# from typing import Callable, Any


# def how_are_you(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         answer = input('Как дела? ')
#         print(f'Ты ответил: {answer}')
#         print('А у меня не очень! Ладно, держи свою функцию.')
#         return func(*args, **kwargs)
#     return  wrapper
#
#
# @how_are_you
# def test():
#     print('<Тут что-то происходит...>')
#
# test()

# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>


# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный
# пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
# Чтобы посмотреть решение от нашего эксперта, нажмите на кнопку ниже.

# import time
# from functools import wraps
# from typing import Callable, Any
#
#
# def wait_before(seconds: float) -> Callable:
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args, **kwargs) -> Any:
#             print(f'Ждём {seconds} секунд(ы) перед вызовом функции {func.__name__}...')
#             time.sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @wait_before(3)
# def some_function():
#     print("Функция выполнена!")
#
# some_function()

# Вариант от скилбокса:
# from functools import wraps
# from time import sleep
# from typing import Callable, Any
#
# def slowdown_2s(func: Callable) -> Callable:
#     """
#     Декоратор, который замедляет выполнение декорируемой функции на 2 секунды.
#     Args:
#         func: Функция, которую нужно декорировать.
#
#     Returns: Ссылка на функцию-обёртку.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         """
#         Обёртка для декорируемой функции, осуществляющая задержку перед вызовом.
#         Задерживает выполнение на 2 секунды, а затем вызывает оригинальную функцию
#         с переданными ей аргументами.
#         Args:
#             *args: Позиционные аргументы, передаваемые в декорируемую функцию.
#             **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
#         Returns: Результат, возвращаемый декорируемой функцией.
#         """
#         sleep(2)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# Задача 3. Логирование
# Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран
# выводится название функции и её документация. Если во время выполнения декорируемой
# функции возникла ошибка, то в файл function_errors.log записывается название функции
# и ошибки.
# Постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же
# ошибки, а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
# import os
# import datetime
# from functools import wraps
# from typing import Callable, Any
#
# def logging(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         print(f'Название функции {func.__name__} и ее документация:\n{func.__doc__}')
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             log_path = os.path.join(os.getcwd(), 'error_log.txt')
#             with open(log_path, 'a', encoding='utf-8') as f:
#                 f.write(f'Ошибка в функции {func.__name__}: {e}\nДата и время: {datetime.datetime.now()}.\n')
#             print(f'Произошла ошибка: {e}, но программа продолжит работу.')
#             return None
#     return wrapper
#
#
# @logging
# def is_even(number: int) -> bool:
#     """
#     Проверяет, является ли число чётным.
#     :param number: Целое число для проверки.
#     :return: True, если число чётное, иначе False.
#     """
#     return number % 2 == 0
#
# @logging
# def division(number_1: int, number_2: int) -> float | None:
#     """
#     Проверяет делимость целочисленных чисел.
#     :param number_1: Целое число для проверки.
#     :param number_2: Целое число для проверки.
#     :return: Int, если первое число больше второго.
#     """
#     if number_1 > number_2:
#         # try:
#             return number_1 / number_2
#         # except ZeroDivisionError:
#         #     print("Ошибка: Деление на ноль!")
#         #     return None
#
#
# print(is_even(0))
# print(division(4, 3))
# print(division(1, 0))
# print(division(4, 2))


# Задача 4. Кеширование для ускорения вычислений
# Вы разрабатываете программу для оптимизации вычислений чисел Фибоначчи. Числа Фибоначчи
# вычисляются рекурсивной функцией, каждое число равно сумме двух предыдущих чисел. Однако
# вы заметили, что при больших значениях чисел Фибоначчи вычисления занимают значительное время,
# так как многие значения вычисляются повторно. Вам поручили создать декоратор, который кеширует
# результаты вызова функции и позволяет избежать повторных вычислений для одних и тех же аргументов.
# Для начала работы у вас есть такой код:
from typing import Callable, Any, Dict


def register_plugins(func: Callable) -> Callable:
    # cache_dict: Dict[Any, Any] = dict()
    cache = {}
    # def wrapper(*args, **kwargs) -> Any:
    def wrapper(number: int) -> int:
        # key = args + (frozenset(kwargs.items()),)
        # if key in cache_dict:
        #     return cache_dict[key]
        #
        # result = func(*args, **kwargs)
        # cache_dict[key] = result
        # return result
        if number not in cache:
            cache[number] = func(number)
        return cache[number]

    return wrapper


@register_plugins
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован

# Создайте декоратор, который кеширует (сохраняет для дальнейшего использования) результаты вызова
# функции и, при повторном вызове с теми же аргументами, возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, если такие аргументы
# уже использовались, возвращать сохранённый результат вместо запуска расчёта.
# Советы:
# Для хранения результатов удобно использовать словарь, так как поиск элементов внутри словаря будет
# иметь сложность, равную в среднем O(1).
# При этом не стоит хранить все вычисления в одном словаре, созданном снаружи функций (в глобальной области
# видимости). Лучше создавать отдельные словари для каждой декорируемой функции.

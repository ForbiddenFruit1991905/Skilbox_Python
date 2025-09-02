# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.
import functools
from typing import Callable


def number_of_repeat(number: int):
    def repeat_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)

        return wrapped
    return repeat_decorator

@number_of_repeat(4)
def some_message(name: str) -> None:
    print(f'Привет, {name}! Как твои дела?')

some_message('Вика')


# Задача 2. Замедление кода 2
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор, который перед
# выполнением декорируемой функции ждёт несколько секунд.
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве
# аргумента. По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор
# можно было использовать как с аргументами, так и без них.

import time
from functools import wraps
from typing import Callable, Any


def wait_before(seconds: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            print(f'Ждём {seconds} секунд(ы) перед вызовом функции {func.__name__}...')
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@wait_before(3)
def some_function():
    print("Функция выполнена!")

some_function()
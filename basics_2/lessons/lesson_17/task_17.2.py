# Задача 1. Счётчик 2
# Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов
# декорируемой функции. Для этого мы использовали интересную особенность классов. В этот
# раз реализуйте тот же декоратор, но уже с использованием знаний о локальных и глобальных
# переменных.
# Реализуйте декоратор двумя способами:
# используя глобальную переменную count;
# используя локальную переменную count внутри декоратора.
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции
# и методы, находящиеся во встроенном пространстве имён в Python.
# Результат выполнения команды:
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__' и т.д.
import functools
from typing import Callable, Any


count = 0

def counter(number: int):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            global count
            count_local = 0
            print('Вызов функции.')
            print(dir(__builtins__))
            result = None
            for _ in range(number):
                result = func(*args, **kwargs)
                count += 1
                count_local += 1
            print(f'Кол-во (глобальный счетчик) вызовов {count}')
            print(f'Кол-во (локальный счетчик) вызовов {count_local}')
            return result
        return wrapper
    return decorator


@counter(3)
def some_func(name: str) -> None:
    print('Hi, {}'.format(name))


some_func('Vika')

print('*' * 100)

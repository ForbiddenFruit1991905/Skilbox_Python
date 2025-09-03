# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов
# объекта класса каждый раз, когда объект класса создаётся в основном коде.
import functools
from datetime import datetime
from typing import Callable


def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        current_daytime = cls(*args, **kwargs)
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f'Время создания объекта класса: {formatted_time}')
        return current_daytime
    return wrapper

def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith("__"):
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate

def method_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызов метода {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@create_time
@for_all_methods(method_decorator)
class Functions:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def some_func(self) -> None:
        print(f"Привет, {self.name}")

    def another_func(self):
        print(f'Сколько тебе лет? Мне {self.age} годика.')


my_funcs_1 = Functions('Соня', 3)
my_funcs_1.some_func()
my_funcs_1.another_func()

# Пример от скиллбокса
import datetime


def decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)

        print("Время создания -", datetime.datetime.now())
        print("Методы:", end=" ")
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            print(i_method, end=' ')
        print()
        return instance

    return wrapper


@decorator
class Example:

    def hello(self):
        print("hello")

    def hello_2(self):
        print("hello")


Example()
Example()
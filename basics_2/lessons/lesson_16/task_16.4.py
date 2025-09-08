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


# Задача 2. Декорацию знаешь?
# На новой работе вы познакомились с middle-разработчиком на Python, который согласился научить вас всему,
# что умеет сам. Но перед этим он решил точечно проверить ваши знания. Он показал код, где один и тот же
# декоратор логирования использовался для каждого метода класса отдельно.
# Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
# это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.

def logging(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        result = cls(*args, **kwargs)
        print("Время создания -", datetime.datetime.now())
        print("Методы:", end=" ")
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            print(i_method, end=' ')
        print()
        return result
    return wrapper

@logging
class MyClass:
    def method_1(self) -> None:
        print('Version 1')

    def method_2(self) -> None:
        print('Version 2')

    def method_3(self) -> None:
        print('Version 3')


my_funcs = MyClass()
my_funcs.method_1()
my_funcs.method_2()
my_funcs.method_3()

# Пример от скиллбокса
def logged(func):
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)

    return wrapped


def decorator(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue
        a = getattr(cls, i_method)
        if hasattr(a, '__call__'):
            decorated_a = logged(a)
            setattr(cls, i_method, decorated_a)
    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()
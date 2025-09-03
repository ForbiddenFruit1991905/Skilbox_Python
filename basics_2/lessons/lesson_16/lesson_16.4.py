# Изучая декораторы мы говорили о том,
# что они позволяют красиво модифицировать поведение функций и без лишнего повторения кода.
# Однако, логично предположить, что всё то же самое может относиться не только к функциям.

# Рассмотрим такую задачу.
# Скажем, мы работаем с большим проектом и с огромным количеством всяких классов.
# И для создания отчета, нам нужно знать когда создавались объекты того или иного класса.
# Нам нужно написать код, который как раз будет выводить на экран время создания объекта,
# причем сразу же когда он инициализируется в программе.


# За пример возьмем класс
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


# Опишем декоратор
import functools
from datetime import datetime


def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время создания инстанса класса:", datetime.utcnow())
        return instance

    return wrapper


# Добавим декоратор к классу
@createtime
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
my_funcs_2 = Functions(max_num=2000)
my_funcs_3 = Functions(max_num=3000)

#  Дополним нашу задачу.
#  Скажем, нам нужно сделать так, чтобы при вызове любого метода класса на экран выводилось время его работы.
#  Для этого нам понадобится наш старый декоратор таймер.


#  Давайте просто его сюда вставим
import time
from typing import Callable


def timer(func: Callable) -> Callable:
    """Декоратор. Выводит время работы функции или метода"""

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Время работы функции:", end - start)
        return result

    return wrapped


# Попробуем применить его в качестве ещё одного декоратора класса
@timer
@createtime
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
my_funcs_2 = Functions(max_num=2000)
my_funcs_3 = Functions(max_num=3000)


# При запуске увидим неправильный результат
# Получается, что питон выдал время, затраченное на инициализацию объекта, а методы здесь остались нетронутыми.
# Ну, этого следовало ожидать. В таком случае, мы можем просто задекорировать все методы
@createtime
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    @timer
    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    @timer
    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
my_funcs_2 = Functions(max_num=2000)
my_funcs_3 = Functions(max_num=3000)


# И вот теперь всё работает.
# Однако, есть одна проблема: если этих методов (выделить) будет не два,
# а хотя бы штук 10, то декорировать каждый из них это крайне неэффективное занятие.
# Значит, нам опять же нужен декоратор для класса,
# который сам задекорирует все методы с помощью другого декоратора, в нашем случае с помощью таймера.
# Тогда нам понадобится декоратор с аргументом
def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и
    применяет его ко всем методам класса
    """

    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith("__") is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return decorate


@createtime
@for_all_methods(timer)  # Добавим наш декоратор
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
my_funcs_2 = Functions(max_num=2000)
my_funcs_3 = Functions(max_num=3000)
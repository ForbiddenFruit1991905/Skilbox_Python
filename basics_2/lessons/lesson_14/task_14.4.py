# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут
# различные ингредиенты вроде салата, помидоров и других. Всё это в свою очередь
# содержится между двух половинок булочки. Реализуйте такую функцию и два соответствующих
# декоратора — ингредиенты и хлеб.
# Пример результата работы программы при вызове функции sandwich:
# </----------\>
#помидоры#
# --ветчина--
# ~салат~
# <\______/>


from typing import Callable


def sandwich(func: Callable) -> Callable:
    def wrapper():
        print('</----------\>')
        result = func()
        print(result)
        print('<\______/>')
    return wrapper


def tomatoes():
    return '#помидоры#'


def harm():
    return '--ветчина--'


def salat():
    return '~салат~'


@sandwich
def make_sandwich():
    return '\n'.join([tomatoes(), harm(), salat()])

make_sandwich()

# Вариант от скилбокса

def get_some_salad(func):
    def wrap_that_salad(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrap_that_salad


def get_some_buns(func):
    def wrap_that_buns(*args, **kwargs):
        print("</----------\>")
        func(*args, **kwargs)
        print("<\______/>")

    return wrap_that_buns


@get_some_buns
@get_some_salad
def filling_burger(filler):
    print(filler)


filling_burger("ветчина")

# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, часть из которых
# используется в других проектах в качестве плагинов, то есть они как бы «подключаются»
# и создают дополнительный функционал.
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как
# плагины и заносить их в соответствующий словарь.

from typing import Callable, Dict


PLUGINS: Dict[str, Callable] = dict()

def register_plugins(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@register_plugins
def say_hello(name: str) -> str:
    return f"Hello, {name}"


@register_plugins
def question() -> str:
    some_user_question = input('Введите любой вопрос:\n')
    return some_user_question


print(PLUGINS)
print(say_hello('Vika'))
print(question())

print(PLUGINS['say_hello']('Vika'))
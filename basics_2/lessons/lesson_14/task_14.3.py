# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
# Не забывайте про документацию и аннотации типов.
# Пример декорируемой функции:
def do_twice(func):
    def wrapped_func(*args):
        result = func(*args)
        func(*args)
        return result
    return wrapped_func

@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')

# или так:
def do_n_times(number):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapped_func
    return decorator


@do_n_times(2)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')


# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
# которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками
# в интернете. Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать
# намного красивее и удобнее.
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

import time


def get_timer(func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 5)
        print(f'Функция работала {run_time} секунд(ы).')

        return result
    return wrapped_func

@get_timer
def some_function():
    palindrome_words = []
    try:
        with open('words.txt', 'r', encoding='utf-8') as read_file, \
            open('errors.txt', 'w', encoding='utf-8') as write_file:
            lines = read_file.readlines()
            for line in lines:
                word = line.rstrip('\n')
                try:
                    if any(symbol.isdigit() for symbol in word):
                        raise ValueError(f'Слово "{word}" содержит число.')

                    if word == word[::-1]:
                        palindrome_words.append(word)

                except ValueError as exp:
                    write_file.write(f'Ошибка: {exp}\n')

    except FileNotFoundError:
        print('Файл не найден.')

    return palindrome_words


my_result = some_function()
print(my_result)
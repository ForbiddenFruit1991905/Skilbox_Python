# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
def func_1(x):
    return x + 10

def func_2(func, *args, **kwargs):
    result_1 = func(*args, **kwargs)
    result_2 = func(*args, **kwargs)
    return result_1 * result_2
    # или так: return func(number) * func(number)

# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов
# переданной функции.
# Пример основного кода:
print(f'Результат: {func_2(func_1, 9)}.')


# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость
# передачи данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время
# вам было лень, поэтому возникла идея написать «автотест», который всё сделает сам.
# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы
# переданной функции func и выдаёт ответ на экран.
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.
import time


def get_timer(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    run_time = round(end - start, 5)
    print(f'Функция работала {run_time} секунд(ы).')

    return result


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


my_result = get_timer(some_function)
print(my_result)

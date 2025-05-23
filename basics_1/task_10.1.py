# Задача 1. Таблица умножения.
# Математик Паша недавно заметил, что у него уже есть куча разных таблиц
# степеней, но нет самого основного — таблицы умножения. Пора бы это исправить.
# Напишите программу, которая выводит таблицу умножения для чисел от 1 до 9.
# Для этого используйте конструкцию вложенного цикла: внешний отвечает за первый
# множитель, а внутренний — за второй.
# Дополнение: выведите настоящую таблицу умножения, без всяких знаков, только числа.
# Чтобы она получилась красивой и ровной, используйте литерал \t внутри оператора end.
# \t — это литерал табуляции, благодаря ему все числа выстраиваются в виде таблицы.
# Результат должен получиться таким:
# 1   2   3   4   5   6   7   8   9
# 2   4   6   8   10  12  14  16  18
# ....

# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end="\t")
#     print()

# Задача 2. Таблица суммы.
# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 0 до N.

# N = int(input("Enter number: "))
#
# for row in range(0, N + 1):
#     for col in range(0, N + 1):
#         print(row + col, end="\t")
#     print()

# Задача 3. Анализ данных.
# Отдел анализа данных сегодня получил вот такую интересную штуку:
#
#
# Вам, как работнику этого отдела, дали задание понять, как и почему такое произошло. Напишите программу, которая выводит на экран такую таблицу.
# 💡 Замечание: не забудьте про литерал табуляции \t.

N = int(input("Enter number: "))

for row in range(0, N + 1):
    for col in range(0, -N - 1, -1):
        print(row + col, end="\t")
    print()
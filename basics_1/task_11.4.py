# Задача 1. Герон.
# Существует, так называемая, формула Герона, позволяющая вычислить площадь треугольника,
# зная длины его сторон.
# S= √ (p * (p - a)*(p - b)*(p - c)), где
# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a, b, c - длины сторон треугольника.
# Напишите программу, которая принимает на вход длины сторон треугольника и выводит его площадь
import math
#
# a = int(input("Введите длину a треугольника: "))
# b = int(input("Введите длину b треугольника: "))
# c = int(input("Введите длину c треугольника: "))
#
# p = (a + b + c) / 2
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(S)

# Задача 2. Игра.
# Вам предстоит создать 2D-игру (вид сверху, игрок двигается в двух плоскостях).
# Начнём с управления персонажем: получаем от игрока пройденное расстояние и угол, по которому
# двигался персонаж. Зная эту информацию, нужно изменить текущие координаты (0, 0) на новые (х, у).
# Чтобы это сделать, требуется узнать, какое расстояние персонаж преодолеет по горизонтали (по оси Х,
# x = расстояние × косинус угла) и по вертикали (по оси У, y = расстояние × синус угла).
# Напишите программу, которая получает на вход расстояние и угол поворота. Выведите координаты нового
# местоположения персонажа.

# distance = int(input("Введите расстояние: "))
# angle = int(input("Введите угол поворота: "))
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance
# print(f"Координаты нового местоположения персонажа: {x, y}")

# Задача 3. Мега-калькулятор.
# Кеша учится в третьем классе, и уже умеет программировать на питоне. Как и многие его одноклассники,
# он очень любит сразу применять все полученные знания на практике. Вчера Кеша узнал про модуль math и
# его основные возможности, поэтому решил написать мега-калькулятор, который бы применял сразу все функции
# к введенному пользователем числу. Чтобы ничего не забыть, он пользуется шпаргалкой, которую прикрепили
# к уроку.
# Напишите программу, которая получает от пользователя вещественное число, по очереди применяет к нему
# функции модуля Math и выводит результат:
# округляет вниз,
# округляет вверх,
# берет модуль числа,
# извлекает квадратный корень,
# возводит экспоненту в степень, равную числу,
# считает натуральный логарифм числа,
# считает логарифм числа по основанию 2,
# считает логарифм числа по основанию 10,
# считает синус и косинус числа.
# И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа. Для этого ему пришлось
# придумать и реализовать контроль ввода: факториал вычисляется, только если введенное число было натуральным.

number = float(input("Введите число: "))

floor = math.floor(number)
ceil = math.ceil(number)
module = abs(number)
square = math.sqrt(number)
exponent = math.exp(number)
log_2 = math.log2(number)
log_10 = math.log10(number)
sin = math.sin(number)
cos = math.cos(number)
print(floor, "\t" * 5, ceil, "\t" * 5, module, "\n", square, "\t", exponent, "\t", log_2, "\n", log_10, "\t", sin, "\t", cos)
if number < 0 or number != int(number):
    print("Ненатуральное")
else:
    print(math.factorial(int(number)))

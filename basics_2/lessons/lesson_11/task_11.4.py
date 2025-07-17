# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока.
# На всякий случай вот описание класса.
# Четыре атрибута:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра
# класса (то есть передаваться в init). Реализуйте такое изменение класса.

# import random
#
#
# class Toyota:
#
#     cars = []
#
#     def __init__(self, color, price, current_speed, max_speed=200):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#         Toyota.cars.append(self)
#
#
#     def car_info(self):
#         print('Color: {}\nPrice: {}\nMax speed: {}'
#               '\nCurrent speed: {}'.format(self.color, self.price,
#                 self.max_speed, self.current_speed))
#
#
#     def change_speed(self, new_speed):
#         self.current_speed = new_speed
#
#
# car_1 = Toyota('blue', 1500000, 0)
# car_2 = Toyota('green', 2500000, 0)
# car_3 = Toyota('pink', 3500000, 0)
#
# for car in Toyota.cars:
#     car.change_speed(random.randint(0, car.max_speed))
#     car.car_info()
#     print('-' * 20)


# Задача 2. Координаты точки
# Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут
# передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
# Реализуйте класс, который будет представлять эту точку, и напишите метод, который
# предоставляет информацию о ней. Также внутри класса пропишите счётчик, который будет
# отвечать за количество созданных точек.
# Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.

# class Dots:
#
#     dots_sequence = []
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Dots.dots_sequence.append(self)
#         Dots.count += 1
#
#
#     def dot_info(self):
#         print('X: {}, Y: {}'.format(self.x, self.y))
#
# dot_1 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
# dot_2 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
# dot_3 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
#
# for dot in Dots.dots_sequence:
#     dot.dot_info()
#     print('*' * 15)
#
# print("Всего точек создано:", Dots.count)
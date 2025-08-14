# Задача 1. Транспорт
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость,
# и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс
# «Транспорт» должен быть абстрактным и содержать абстрактные методы.
# Также добавьте класс-примесь, в котором реализован функционал проигрывания
# музыки. «Замешайте» этот класс в «Амфибию».
# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def signal(self):
#         print('Подаю сигнал!')
#
# class PlayMusic:
#     def __init__(self, type_of_music="default", load=0):
#         self.type_of_music = type_of_music
#         self.load = load
#
#     def play_music(self):
#         print('Могу проигрывать музыку!')
#         print(f'Проигрываю музыку: {self.type_of_music}')
#
# class Autos(Transport):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#          print(f'{self.color} автомобиль движется со скоростью {self.speed} по земле.')
#
#     def signal(self):
#         print('Автомобиль подаёт сигнал: Бип-бип!')
#
# class Boats(Transport):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         print(f'{self.color} лодка движется со скоростью {self.speed} по воде.')
#
#     def signal(self):
#         print('Лодка подаёт сигнал: Ту-ту!')
#
# class Amphibian(Autos, Boats, PlayMusic):
#     def __init__(self, color, speed, type_of_music="default", load=0):
#         Autos.__init__(self, color, speed)
#         Boats.__init__(self, color, speed)
#         PlayMusic.__init__(self, type_of_music, load)
#
#     def move(self):
#         print(f'{self.color} амфибия движется со скоростью {self.speed} по земле и воде.')
#
#
# a = Amphibian('Красная', 45)
# a.play_music()
# a.move()

# Задача 2. Фигуры
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты. Каждая из
# них имеет координаты XY, длину и ширину. Также каждая фигура может менять координаты (двигаться) и менять
# размер. Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные
# фигуры и работают они по-разному. В частности, по-разному работает метод изменения размера фигуры, так как
# у квадрата все стороны равны.
# Подсказка: чтобы избежать ошибки TypeError при наследовании класса с абстрактным методом, наследующий класс
# обязательно должен переопределить этот метод.
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    @abstractmethod
    def change_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class ResizableFigure:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width
        print(f'Фигура изменена: длина = {self.length}, ширина = {self.width}')

class Rectangle(Figure, ResizableFigure):
    def __init__(self, x, y, length, width):
        Figure.__init__(self, x, y, length, width)
        ResizableFigure.__init__(self, length, width)

    def change_position(self, new_x, new_y):
        super().change_position(new_x, new_y)

class Square(Figure, ResizableFigure):
    def __init__(self, x, y, size):
        Figure.__init__(self, x, y, size, size)
        ResizableFigure.__init__(self, size, size)

    def change_position(self, new_x, new_y):
        super().change_position(new_x, new_y)


rectangle = Rectangle(100, 200, 30,70)
square = Square(300, 500, 50)

for figure in [rectangle, square]:
    new_size_y = figure.width * 2
    new_size_x = figure.length * 2
    figure.resize(new_size_x, new_size_y)
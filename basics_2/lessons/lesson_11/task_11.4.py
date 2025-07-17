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


# Задача 3. Весёлая ферма
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей
# зрелости и расти. Всего у картошки может быть четыре стадии зрелости.
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю
# эту картошку, а также предоставлять информацию о зрелости всей картошки на своей территории.
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите
# грядку. Пример результата (проверка на зрелость и три взращивания):
# Картошка ещё не созрела!
# Картошка прорастает!
# Картошка 1 сейчас Росток
# ...
# Картошка 5 сейчас Росток
# Картошка ещё не созрела!
# Картошка прорастает!
# Картошка 1 сейчас Зелёная
# ...
# Картошка 5 сейчас Зелёная
# Картошка ещё не созрела!
# Картошка прорастает!
# Картошка 1 сейчас Зелёная
# ...
# Картошка 5 сейчас Зелёная
# Картошка ещё не созрела!

class Potato:

    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0


    def growth_of_potato(self):
        if self.state < 3:
            self.state += 1

        self.info_potato()


    def is_ripe(self):
        if self.state == 3:
            print(f'Картошка {self.index} созрела!')
            return True
        else:
            print(f'Картошка {self.index} ещё не созрела!')
            return False


    def info_potato(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))

class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count +1)]


    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.growth_of_potato()


    def are_all_ripe(self):
        for index_potato in self.potatoes:
            if not index_potato.is_ripe():
                break
        else:
            print('Вся картошка созрела! Можно собирать!')


my_garden = Garden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()

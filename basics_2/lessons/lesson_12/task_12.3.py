# Задача 1. Автомобили
# Даны два класса автомобилей: грузовой и легковой. У каждого из этих автомобилей
# есть своя модель, и каждый может сделать два действия: сообщить свою модель и поехать.
# Грузовой автомобиль имеет такой атрибут, как заполненность багажника, изначально он
# равен нулю. У него есть ещё два действия: загрузить и разгрузить багажник.
# У легкового автомобиля нет багажника, но есть навигационная система, которая передаётся
# вместе с моделью. Также вместо загрузки и разгрузки у него есть другое действие — включить
# навигацию.
# Реализуйте классы грузового и легкового автомобилей. Для этого выделите общие атрибуты и
# методы в отдельный класс «Автомобиль» и используйте наследование. Не забудьте о функции super
# в дочерних классах.

# class Auto:
#
#     def __init__(self, model):
#         self.model = model
#
#
#     def __str__(self):
#         return f'Модель автомобиля {self.model}.'
#
#
#     def run(self):
#         print('Машина поехала.')
#
#
# class CargoAuto(Auto):
#
#     def __init__(self, model, total_load=0):
#         super().__init__(model)
#         self.total_load = total_load
#
#
#     def load_auto(self):
#         self.total_load += 1
#         print("Машина загружена в кол-ве {} тонн.".format(self.total_load))
#
#
#     def reload_auto(self):
#         self.total_load -= 1
#         print("Машина разгружена и товара осталось в кол-ве {} тонн.".format(self.total_load))
#
#
# class PassengerAuto(Auto):
#
#     def __init__(self, model, nav_system):
#         super().__init__(model)
#         self.nav_system = nav_system
#
#
#     def turn_navigation_system(self):
#         print('Навигационная система {} подключена.'.format(self.nav_system))
#
#
# cargo_auto = CargoAuto('sjhg')
# passenger_auto = PassengerAuto('jdbhkh', '132jh')
# print(cargo_auto)
# print(passenger_auto)
# cargo_auto.load_auto()
# cargo_auto.load_auto()
# cargo_auto.reload_auto()
# passenger_auto.turn_navigation_system()

# Задача 2. Домашние роботы
# На выставку робототехники привезли несколько интересных моделей роботов, которые похожи
# между собой, но немного различаются функциональностью. У каждого робота есть номер модели
# и действие operate, которое описывает выполняемые им функции.
# Особенности роботов:
# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот
# сообщает, что он пылесосит пол, и выводит текущую заполняемость мешка.
# У робота-охранника есть сигнализация, и при команде operate он выводит сообщение о патрулировании
# дома с её помощью.
# Ещё есть робот для бассейнов, который также является охранником. У этого робота есть значение глубины,
# и при команде operate он делает то же, что и робот-охранник, плюс сообщает, что охрана ведётся под водой.
# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Модель робота {}.'.format(self.model)

    def operate(self):
        print('Робот включен!')


class RobotVacuumCleaner(Robot):
    def __init__(self, model, garbage_bag=0):
        super().__init__(model)
        self.garbage_bag = garbage_bag

    def operate(self):
        Robot.operate(self)
        self.garbage_bag += 1
        print("Пылесос работает. Заполняемость равна {}".format(self.garbage_bag))


class RobotSecure(Robot):
    def __init__(self, model, signalization):
        super().__init__(model)
        self.signalization = signalization

    def operate(self):
        Robot.operate(self)
        print('Сигнализация подключена: {}.'.format(self.signalization))


class PoolCleaningRobot(RobotSecure):
    def __init__(self, model, signalization, depth):
        super().__init__(model, signalization)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана ведётся под водой на глубине {self.depth} метров.')


rvc = RobotVacuumCleaner('hgjd', 5)
rs = RobotSecure('djkh', '1234khg')
pcr = PoolCleaningRobot('2huhh', '12h3lhg', 10)

rvc.operate()
print(rvc)
rs.operate()
print(rs)
pcr.operate()
print(pcr)

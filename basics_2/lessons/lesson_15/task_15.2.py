# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких,
# а летающих: разведывательного дрона и военного робота.
# Разведывательный дрон просто летает в поиске противника. При команде operate
# он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение
# о защите военного объекта с воздуха с помощью этого оружия.
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот»
# и «Может летать» должны быть вынесены в отдельные классы. Обычный робот имеет модель и
# может вывести сообщение «Я — Робот». Объект, который умеет летать, дополнительно имеет
# атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.

class Robot:
    def __init__(self, model: str):
        self.model = model

    def say(self):
        print('Я — Робот')

    def operate(self):
        pass


class Flyable:
    def __init__(self, height: int, speed: int):
        self.height = height
        self.speed = speed
        self.position = 0

    def can_fly(self):
        print('Могу летать!')

    def take_off(self):
        print('Могу взлетать!')

    def can_land(self):
        print('Могу приземляться!')


class ReconnaissanceDrone(Robot, Flyable):
    def __init__(self, model: str, height: int, speed: int):
        Robot.__init__(self, model)
        Flyable.__init__(self, height, speed)

    def operate(self):
        print("Веду разведку с воздуха.")
        self.position += self.speed
        print(f"Переместился вперёд, текущая позиция {self.position}")


class MilitaryRobot(ReconnaissanceDrone):
    def __init__(self, model: str, height: int, speed: int, weapon: str):
        super().__init__(model, height, speed)
        self.weapon = weapon

    def operate(self):
        print(f'Защита военного объекта с воздуха с помощью {self.weapon}.')

    def __str__(self):
        return  f'Модель: {self.model}\nВысота: {self.height}\nСкорость: {self.speed}\nОружие: {self.weapon}'



m_r = MilitaryRobot('jshgljh', 500, 20, 'machine gun')
print(m_r)
m_r.operate()
m_r.say()
print('**************************************************')
d = ReconnaissanceDrone('drone1', 300, 15)
d.operate()
d.can_fly()
d.take_off()
d.can_land()
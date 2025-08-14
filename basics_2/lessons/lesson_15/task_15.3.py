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
from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def signal(self):
        print('Подаю сигнал!')

class PlayMusic:
    def __init__(self, type_of_music="default", load=0):
        self.type_of_music = type_of_music
        self.load = load

    def play_music(self):
        print('Могу проигрывать музыку!')
        print(f'Проигрываю музыку: {self.type_of_music}')

class Autos(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def move(self):
         print(f'{self.color} автомобиль движется со скоростью {self.speed} по земле.')

    def signal(self):
        print('Автомобиль подаёт сигнал: Бип-бип!')

class Boats(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def move(self):
        print(f'{self.color} лодка движется со скоростью {self.speed} по воде.')

    def signal(self):
        print('Лодка подаёт сигнал: Ту-ту!')

class Amphibian(Autos, Boats, PlayMusic):
    def __init__(self, color, speed, type_of_music="default", load=0):
        Autos.__init__(self, color, speed)
        Boats.__init__(self, color, speed)
        PlayMusic.__init__(self, type_of_music, load)

    def move(self):
        print(f'{self.color} амфибия движется со скоростью {self.speed} по земле и воде.')


a = Amphibian('Красная', 45)
a.play_music()
a.move()

# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс
# геттерами и сеттерами для соответствующих атрибутов. Используйте встроенные декораторы.
# Вот входные данные той задачи:
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет
# двигаться и подавать сигнал. В парке транспорта стоят:
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.

from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

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
a.speed = 55
print(a.speed)
a.color = 'Violet'
print(a.color)
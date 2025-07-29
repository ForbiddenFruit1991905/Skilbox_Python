# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
# Также есть два дочерних класса:
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

class Unit:
    def __init__(self, health_points):
        self.__health_points = health_points

    def set_hp(self, new_hp):
        if new_hp < 0:
            self.__health_points = 0
        else:
            self.__health_points = new_hp

    def get_hp(self):
        return self.__health_points

    def get_damage(self, loss=0):
        new_hp = self.get_hp() - loss
        self.set_hp(new_hp)
        print(f'Остаток HP: {self.get_hp()}')


class Soldier(Unit):
    # получает урон, равный переданному значению.
    def __init__(self, health_points):
        super().__init__(health_points)

    def get_damage(self, loss):
        rest_xp = self.get_hp() - loss
        self.set_hp(rest_xp)
        print(f'Остаток HP: {self.get_hp()}')


class NPS(Soldier):
# Обычный гражданин: получает урон, равный двукратному переданному значению.
    def __init__(self, health_points):
        super().__init__(health_points)

    def get_damage(self, loss):
        rest_xp = self.get_hp() - loss * 2
        self.set_hp(rest_xp)
        print(f'Остаток HP: {self.get_hp()}')


soldier_unit = Soldier(10)
soldier_unit.get_damage(3)
nps_unit = NPS(10)
nps_unit.get_damage(3)
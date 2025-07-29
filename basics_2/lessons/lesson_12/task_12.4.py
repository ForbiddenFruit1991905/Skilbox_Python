# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
# Также есть два дочерних класса:
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

# class Unit:
#     def __init__(self, health_points):
#         self.__health_points = health_points
#
#     def set_hp(self, new_hp):
#         if new_hp < 0:
#             self.__health_points = 0
#         else:
#             self.__health_points = new_hp
#
#     def get_hp(self):
#         return self.__health_points
#
#     def get_damage(self, loss=0):
#         new_hp = self.get_hp() - loss
#         self.set_hp(new_hp)
#         print(f'Остаток HP: {self.get_hp()}')
#
#
# class Soldier(Unit):
#     # получает урон, равный переданному значению.
#     def __init__(self, health_points):
#         super().__init__(health_points)
#
#     def get_damage(self, loss):
#         rest_xp = self.get_hp() - loss
#         self.set_hp(rest_xp)
#         print(f'Остаток HP: {self.get_hp()}')
#
#
# class NPS(Soldier):
# # Обычный гражданин: получает урон, равный двукратному переданному значению.
#     def __init__(self, health_points):
#         super().__init__(health_points)
#
#     def get_damage(self, loss):
#         rest_xp = self.get_hp() - loss * 2
#         self.set_hp(rest_xp)
#         print(f'Остаток HP: {self.get_hp()}')
#
#
# soldier_unit = Soldier(10)
# soldier_unit.get_damage(3)
# nps_unit = NPS(10)
# nps_unit.get_damage(3)

# Задача 2. Полёт
# Иногда для реализации дочерних классов используется так называемый класс-роль, где
# также описываются общие атрибуты и методы, но в программе инициализируются объекты
# только дочерних классов, а базовый класс-роль не трогается. К примеру, что общего у
# бабочки и ракеты? Они обе могут летать и приземляться.
# Реализуйте класс «Может летать».
# Атрибуты:
# Высота = 0.
# Скорость = 0.
# Методы:
# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.
# Затем реализуйте два дочерних класса:
# «Бабочка», который может:
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).
# «Ракета», которая может:
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).

class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )

class Butterfly(CanFly):
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.height = 1
        print(f'Бабочка взлетела на высоту {self.height}.')

    def fly(self):
        self.speed = 0.5
        print(f'Бабочка полетела со скоростью {self.speed}.')

class Aircraft(CanFly):
# «Ракета», которая может:
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).
    def __init__(self):
        super().__init__()

    def take_off(self):
        self.height = 500
        self.speed = 1000

    def land(self, explosure=False):
        self.height = 0
        if explosure:
            print("Взрыв!")
        else:
            print("Приземление прошло успешно.")

butterfly = Butterfly()
butterfly.take_off()
butterfly.fly()
rocket = Aircraft()
rocket.take_off()
rocket.land(explosure=True)
rocket.land()


# Вариант от скилбокса:
# class CanFly:
#
#     def __init__(self):
#         self.altitude = 0  # метров
#         self.velocity = 0  # км/ч
#
#     def take_off(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def land_on(self):
#         self.altitude = 0
#         self.velocity = 0
#
#     def __str__(self):
#         return '{} высота {} скорость {}'.format(
#             self.__class__.__name__, self.altitude, self.velocity,
#         )
#
#
# class Butterfly(CanFly):
#
#     def take_off(self):
#         self.altitude = 1
#
#     def fly(self):
#         self.velocity = 0.1
#
#
# class Aircraft(CanFly):
#
#     def take_off(self):
#         self.velocity = 300
#         self.altitude = 1000
#
#     def fly(self):
#         self.velocity = 800
#
#
# class Missile(CanFly):
#
#     def take_off(self):
#         self.velocity = 1000
#         self.altitude = 10000
#
#     def land_on(self):
#         self.altitude = 0
#         self.destroy_enemy_base()
#
#     def destroy_enemy_base(self):
#         print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')

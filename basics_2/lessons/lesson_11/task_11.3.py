# Задача 1. Машина 2.
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
import random


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0


    def car_info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}'
              '\nCurrent speed: {}'.format(self.color, self.price,
                self.max_speed, self.current_speed))


    def change_speed(self, new_speed):
        self.current_speed = new_speed


car_name = [Toyota() for _ in range(3)]

for index, car in enumerate(car_name, start=1):
    print(f"Car №{index}:")
    car.change_speed(random.randint(0, car.max_speed))
    car.car_info()
    print('-' * 20)

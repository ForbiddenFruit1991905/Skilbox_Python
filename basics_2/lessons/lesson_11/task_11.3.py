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


# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома»
# и объекты которого могут выполнять следующие действия:
    # 1. Отобразить информацию о себе.
    # 2. Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
    # 3. Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести
    # соответствующее сообщение об успешной/неуспешной покупке дома.

# Создайте как минимум один экземпляр класса и проверьте работу методов.

# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):

# Family name: Common family
# Family funds: 100000
# Having a house: False

# Try to buy a house
# Not enough money!

# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0

# Family name: Common family
# Family funds: 0.0
# Having a house: True

class Family:

    surname = 'Some family'
    money = 100000
    get_house = False


    def family_info(self):
        print('Family surname: {}\nFamily current budget: {}\nHaving a house: {}\n'.format(self.surname,
                                                                                           self.money, self.get_house))

    def earn_money(self, salary):
        self.money += salary
        print('Earned {} money! Current value: {}'.format(salary, self.money))


    def buy_house(self, house_price, discount=10):
        print('Try to buy a house')
        house_price -= house_price * discount / 100

        if self.money >= house_price:
            self.money -= house_price
            self.get_house = True
            print('House purchased! Current money: {}'.format(self.money))
        else:
            print('Not enough money! You need to earn: {}.'.format(house_price - self.money))


my_family = Family()
my_family.family_info()
my_family.buy_house(10 ** 6)

if not my_family.get_house:
    my_family.earn_money(850000)
    print('Try to buy a house again')
    my_family.buy_house(10 ** 6, 10)

my_family.family_info()

# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение
# текущей скорости на случайное число от нуля до 200.
# import random
#
#
# class Toyota:
#     color = 'red'
#     price = 1000000
#     max_speed = 200
#     current_speed = 0
#
#
# car_1 = Toyota()
# car_2 = Toyota()
# car_3 = Toyota()
# car_sequence = [car_1, car_2, car_3]
# for item in car_sequence:
#     item.current_speed = item.current_speed = random.randint(0, item.max_speed)
#     print(item.current_speed)


# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора
# есть четыре характеристики: название производителя, матрица, разрешение и частота
# обновления экрана. Все четыре монитора отличаются только частотой.
# У наушников три характеристики: название производителя, чувствительность и наличие
# микрофона. Отличие только в наличии микрофона.
# Для внесения в базу программист начал писать код. Поправьте программиста: перепишите
# код, используя классы и экземпляры классов.
class MonitorCharacters:

    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60

monitor_1 = MonitorCharacters()
monitor_2 = MonitorCharacters()
monitor_3 = MonitorCharacters()
monitor_4 = MonitorCharacters()

monitor_1.monitor_freq = 60
monitor_2.monitor_freq = 144
monitor_3.monitor_freq = 70
monitor_4.monitor_freq = 60


class HeadphonesCharacters:

    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = False


headphones_1 = HeadphonesCharacters()
headphones_2 = HeadphonesCharacters()
headphones_3 = HeadphonesCharacters()

headphones_1.headphones_micro = False
headphones_2.headphones_micro = True
headphones_3.headphones_micro = True

# Вариант от скилбокса:
# monitors = [Monitor() for _ in range(4)]
# headphones = [Headphones() for _ in range(3)]
#
# for index, number in enumerate([60, 144, 70, 60]):
#     monitors[index].frequency = number
#
# headphones[0].micro = False
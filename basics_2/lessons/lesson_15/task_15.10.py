# Математический модуль.
# Вася использует в своей программе очень много различных математических вычислений, связанных с фигурами.
# Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством
# функций, он решил выделить для них отдельный класс, подключить как модуль и использовать по аналогии с
# модулем math.
# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.
# Пример основного кода:
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)
# Результат:
# 31.41592653589793
# 113.09733552923255
import math
from abc import ABC


class MyMath(ABC):
    @classmethod
    def circle_length(cls, radius: float) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_square(cls, radius: float) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, edge: float) -> float:
        return edge ** 3

    @classmethod
    def sphere_square_of_surface(cls, radius: float) -> float:
        return 4 * math.pi * radius ** 2


result_1 = MyMath.circle_length(radius=5)
result_2 = MyMath.circle_square(radius=6)
result_3 = MyMath.cube_volume(edge=5)
result_4 = MyMath.sphere_square_of_surface(radius=7)
print(round(result_1, 2))
print(round(result_2, 2))
print(round(result_3, 2))
print(round(result_4, 2))
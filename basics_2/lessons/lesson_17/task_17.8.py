# Даны три списка:
from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# Из списка names берутся только имена минимум из пяти букв.
# Из списка numbers берётся произведение всех чисел.

result_floats = list(map(lambda x: round(x ** 3, 3), floats))
print(result_floats)

result_names = list(filter(lambda name: len(name) >= 5, names))
print(result_names)

result_numbers = reduce(lambda x, y: x * y, numbers)
print(result_numbers)
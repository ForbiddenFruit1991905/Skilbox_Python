# Есть множество встроенных и внешних библиотек для работы с данными в Python.
# С некоторыми из них вы уже работали. Например, с модулем collections, когда
# использовали специальный класс OrderedDict, с помощью которого делали упорядоченный
# словарь. В этой библиотеке есть и другие возможности, но их немного. Официальная
# документация: collections — Container datatypes.
# Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на
# вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
from collections import Counter


def can_be_poly(string_txt: str) -> bool:
    symbols = Counter(string_txt)
    result = filter(lambda letter: letter % 2, symbols.values())
    return len(list(result)) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
# Результат:
# True
# False
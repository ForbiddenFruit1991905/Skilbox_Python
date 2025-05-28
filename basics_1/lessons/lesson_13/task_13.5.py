import math

precision = float(input("Точность: "))
result = 0
i = 0
add_member = 1

while add_member > precision:
    add_member = 1 / math.factorial(i)
    result += add_member
    i += 1

print("Результат:", result)
print("Константа:", math.e)
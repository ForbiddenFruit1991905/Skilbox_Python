# Задание 6. Треугольник из хештегов.
# Что нужно сделать.
# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамиду),
# заполненный символами хештега (#). Пусть высоту пирамиды определяет пользователь.
# Пример.
# Введите высоту пирамиды: 5
    #
   ###
  #####
 #######
#########

height = int(input("Введите высоту пирамиды: "))

for row in range(1, height + 1):
    spaces = " " * (height - row)
    symbols = "#" * (2 * row - 1)
    print(spaces + symbols)

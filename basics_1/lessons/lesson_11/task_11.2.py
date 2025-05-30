# Задача 1. Ставки на спорт.
# Нас наняла букмекерская контора, где проводятся ставки на конный спорт. Напишите
# программу расчёта потенциального выигрыша игрока. Для этого вводится его ставка в
# рублях и коэффициент (вещественное число), а выводится их произведение в качестве
# потенциального выигрыша.
# Пример:
# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544
# Усложнение задачи: сделайте так, чтобы после точки выводилось не больше двух цифр.

# bet = int(input("Сколько ставим? "))
# coefficient = float(input("Какой коэффициент? "))
# win = round(bet * coefficient, 2)
# print(f"Потенциальный выигрыш: {win}")

# Задача 2. День рождения.
# В честь дня рождения сына отец не придумал ничего лучше, кроме как подарить денег. Зато
# он придумал хоть и странную, но интересную формулу, по которой высчитывается сколько он
# подарит: возраст сына умножается на 1.5 и на его температуру тела. Остаётся только позавидовать
# такой фантазии.
# Напишите программу, которая запрашивает у пользователя возраст (целое число) и температуру тела
# (вещественное число) и в результате выводит сколько отец подарит сыну денег на день рождения.

# age = int(input("Укажите возраст: "))
# temp = float(input("Укажите температуру тела: "))
# present = round(age * 1.5 * temp, 2)
# print(present)

# Задача 3. Индекс массы тела.
# Алексей работает диетологом в частной клинике, каждый день он принимает пациентов разных возрастов
# и с разными показателями роста (в метрах) и веса (в кг). Для каждого человека ему нужно считать индекс
# массы тела - это вес поделить на рост в квадрате. По государственным стандартам индекс округляется до
# двух знаков после точки. Затем по этому индексу определяется, всё ли в порядке у человека с массой тела:
# если до 18.5, то недобор; до 25 - всё нормально, до 30 уже идёт избыток, а после 30 - ожирение. Напишите
# такую программу для Алексея.

height = float(input("Рост: "))
weight = float(input("Вес: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("недобор")
elif bmi < 25:
    print("ok")
elif bmi < 30:
    print("избыток")
else:
    print("Ожирение")
print(round(bmi, 2))

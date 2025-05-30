# Задача «Яйца».
# В рамках программы колонизации Марса компания «Спейс Инжиниринг» вывела особую породу
# черепах, которые по задумке должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации, а слишком глубоко —
# из-за давления грунта и недостатка кислорода. Вообще, факторов очень много, но специалисты
# проделали большую работу и предположили, что уровень опасности для черепашьих яиц рассчитывается
# по формуле:
# D = x ** 3 - 3 * x ** 2 - 12 * x + 10;
# где x — глубина кладки в метрах, а D — уровень опасности в условных единицах.
# Для тестирования гипотезы нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# Что нужно сделать.
# Напишите программу, находящую такое значение глубины х, при котором уровень опасности как можно более
# близок к нулю. На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение х, удовлетворяющее этому отклонению. Известно,
# что глубина точно > 0 и < 4 метров.
# Пример работы программы.
# Введите максимально допустимый уровень опасности: 0.01
# Приблизительная глубина безопасной кладки: 0.732421875

# Функция для вычисления среднего значения глубины и уровня опасности на этой глубине
def danger(d_min, d_max):
    d_middle = (d_min + d_max) / 2
    middle_danger = d_middle ** 3 - 3 * d_middle ** 2 - 12 * d_middle + 10
    # Возвращаем среднее значение глубины и рассчитанный уровень опасности
    return d_middle, middle_danger


def depth_calculation(user_danger_level):
    lower_bound = 0
    upper_bound = 4

    while True:
        mid, danger_level = danger(lower_bound, upper_bound)

        if danger_level > 0:
            lower_bound = mid
        else:
            upper_bound = mid

        if abs(danger_level) < user_danger_level:
            return mid

max_danger = float(input("Введите максимально допустимый уровень опасности: "))
result = depth_calculation(max_danger)
print("Приблизительная глубина безопасной кладки: ", result)
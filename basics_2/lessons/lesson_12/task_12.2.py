# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет
# координаты x и y; при создании новой точки могут передаваться пользовательские
# значения координат, по умолчанию x = 0, y = 0.
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
# Предоставление информации о точке (используйте магический метод str).
# Геттер и сеттер для x.
# Геттер и сеттер для y.
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.

# class Dots:
#
#     dots_sequence = []
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Dots.dots_sequence.append(self)
#         Dots.count += 1
#
#
#     def __str__(self):
#         return 'X: {}, Y: {}'.format(self.x, self.y)
#
#
#     def get_y(self):
#         return self.y
#
#
#     def get_x(self):
#         return  self.x
#
#
#     def set_y(self, y):
#         if isinstance(y, int):
#             self.y = y
#         else:
#             raise ValueError('Недопустимая координата Y')
#
#
#     def set_x(self, x):
#         if isinstance(x, int):
#             self.x = x
#         else:
#             raise ValueError('Недопустимая координата X')
#
#
#     def get_dot_sequence(self):
#         return Dots.dots_sequence
#
#
#     def get_count(self):
#         return Dots.count
#
#
# dot_1 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
# dot_2 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
# dot_3 = Dots(int(input("Введите x: ")), int(input("Введите y: ")))
#
# for dot in Dots.dots_sequence:
#     print(dot)
#     print('*' * 15)
#
# print("Всего точек создано:", dot_1.get_count())


# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв)
# и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество
# инициализированных объектов. Реализуйте сокрытие данных для всех атрибутов (как статических, так
# и динамических), а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и
# «крайне нерекомендуемым», который был показан в уроке.

class Person:

    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1


    def __str__(self):
        return 'Имя: {}\nВозраст: {}\n'.format(self.__name, self.__age)


    def get_count(self):
        return self.__count


    def get_name(self):
        return self.__name


    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Неправильные символы имени")


    def get_age(self):
        return self.__age


    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age


vika = Person("Vika", 34)
dima = Person("Dima", 34)
print(vika)
print(dima)
new_age = 35
dima.set_age(new_age)
print(vika.get_count())
print(dima.get_age())
dima._Person__age = 99
print(dima.get_age())

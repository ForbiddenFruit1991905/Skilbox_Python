# class Fibonacci:
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = 0
#         self. next_val = 1
#         self.number = number
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number:
#                 raise StopIteration()
#             self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
#
#         return self.cur_val
#
#
# fib_iterator = Fibonacci(10)
# for i_value in fib_iterator:
#     print(i_value)
# print(8 in fib_iterator)


# Задача 1. Бесконечный итератор
# Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только один
# статический атрибут — счётчик. Итератор увеличивает счётчик и возвращает предыдущее значение.
# У вас должен получиться бесконечный итератор.
# То есть при вызове такого кода в основной программе значения будут выдаваться бесконечно.

# class CountIterator:
#
#     counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # current = CountIterator.counter
#         # CountIterator.counter += 1
#         # return current
#         CountIterator.counter += 1
#         return CountIterator.counter - 1
#
#
# my_iter = CountIterator()
# for i_elem in my_iter:
#     print(i_elem)


# Задача 2. Случайная сумма
# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего
# элемента (первый элемент — просто случайное вещественное число от 0 до 1). Алексею нельзя
# хранить в памяти весь этот список, а со значениями работать как-то надо.
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
# Пример работы программы:
# Кол-во элементов: 5
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
# Новое кол-во элементов: 6
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34

# class MyIterator:
#     def __init__(self, quantity):
#         self.counter = 0
#         self.cur_val = 0
#         self.quantity = quantity
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_val = random.uniform(0.0, 1.0)
#         return self
#
#     def __next__(self):
#         if self.counter >= self.quantity:
#             raise StopIteration
#         if self.counter == 0:
#             result = self.cur_val
#         else:
#             self.cur_val += random.uniform(0.0, 1.0)
#             result = self.cur_val
#         self.counter += 1
#         return round(result, 2)
#
# check_iter = MyIterator(6)
# print("Элементы итератора:")
# for i_index in check_iter:
#     print(i_index)


# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
class Primes:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current_number = 1

    def __iter__(self):
        self.current_number = 1
        return self

    def is_prime(self, number):
        if number <= 1:
            return False
        for index in range(2, int(number ** 0.5) + 1):
            if number % index == 0:
                return False
        return True

    def __next__(self):
        while True:
            self.current_number += 1
            if self.current_number >= self.max_number:
                raise StopIteration
            if self.is_prime(self.current_number):
                return self.current_number


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
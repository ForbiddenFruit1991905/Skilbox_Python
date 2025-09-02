# Дата
# Реализуйте класс Date, который должен:
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых
# значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
# При тестировании программы объект класса Date должен инициализироваться исключительно через
# метод конвертации, например:
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
# Пример основного кода:
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12   Год: 2077
# True
# False

class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        # return f'День: {self.day}    Месяц: {self.month}    Год: {self.year}'

        return "День: {}\tМесяц: {}\tГод: {}".format(
        self.day, self.month, self.year
    )

    @classmethod
    def _parse_date(cls, some_date: str) -> tuple[int, int, int]:
        parts = some_date.split('-')
        return int(parts[0]), int(parts[1]), int(parts[2])

    @classmethod
    def from_string(cls, some_date: str):
        day, month, year = cls._parse_date(some_date)
        return cls(day, month, year)

    @classmethod
    def is_date_valid(cls, some_date: str) -> bool:
        day, month, year = cls._parse_date(some_date)
        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (0 <= year <= 3999):
            return False
        return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
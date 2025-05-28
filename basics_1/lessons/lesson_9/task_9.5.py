# Пример 1. Фильтрация текста.
# txt = input("Enter txt: ")
# summ = 0
# print("Отфильтрованный текст: ", end="")
# for letter in txt:
#     if letter.isdigit():
#         summ += int(letter)
#     else:
#         print(letter, end="")
# print("\nСумма цифр:", summ)

# Пример 2. Нахождение двух одинаковых букв, стоящих рядом.
string = input("Введите строку: ")
prev_symbol = ""
equal_symbol = False
for letter in string:
    if prev_symbol == letter:
        equal_symbol = True
        break
    else:
        prev_symbol = letter

if equal_symbol:
    print("Есть две одинаковые буквы подряд")
else:
    print("Нет двух одинаковых букв подряд")
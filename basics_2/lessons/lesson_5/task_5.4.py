# Пример 1:
# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if not path.endswith('.txt'):
#     print('Ошибка: неверное расширение файла.')
# elif not path.startswith('C:/'):
#     print('Ошибка: неверно указан диск.')
# else:
#     print('Путь к файлу:', path)

# Пример 2:
# word_list = []
#
# for i_num in range(3):
#     print('Введите', i_num + 1, 'слово:', end=' ')
#     word = input().lower()
#     word_list.append(word)
#
# text = input('Введите текст: ').lower().split()
#
# print('\nПодсчёт слов в тексте')
# for index in range(3):
#     print(word_list[index], ':', text.count(word_list[index]))

# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком
# способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте
# конкатенацию и сделайте так, чтобы текст был в одном регистре.

# def get_caesar_cipher(alphabet, text, offset):
#     result_cipher = [alphabet[(alphabet.index(letter) + offset) % len(alphabet)] if letter in alphabet
#                      else letter
#                      for letter in text]
#     return result_cipher
#
# russian_alphabet = [
#     'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
#     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#     'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
# ]
# message = input('Введите сообщение: ').lower()
# shift = int(input('Введите сдвиг: '))
# encrypted_message = get_caesar_cipher(russian_alphabet, message, shift)
# print(f'Зашифрованное сообщение: {"".join(encrypted_message)}')

# Задача 2. Путь к файлу
# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто используются
# абсолютные пути файлов, которые необходимо проверять.
# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение
# файла. Напишите программу, которая проверяет корректность этого пути.
# Пример:
# Путь к файлу: C:/user/docs/folder/new_file.txt
# На каком диске должен лежать файл: C
# Требуемое расширение файла: .txt
# Путь корректен!

# path = input("Путь к файлу: ")
# disk = input("На каком диске должен лежать файл: ")
# extension = input("Требуемое расширение файла: ")
#
# if path.startswith(disk) and path.endswith(extension):
#     print("Путь корректен!")
# else:
#     print("Путь некорректен!")

# Задача 3. Удаление части.
# На вход в программу подаётся строка, состоящая из заглавных и строчных букв кириллицы. Напишите код,
# который проверяет, каких букв в строке больше: строчных или заглавных. Если заглавных букв больше, то
# сделайте все буквы строки заглавными, иначе сделайте всё строчными.
# Подсказка: используйте методы islower() и/или isupper().
# Пример:
# Введите строку: ПитоН - этО хорошО
# Результат: питон - это хорошо
# Пример 2:
# Введите строку: ПиТоН - ЭтО УДоБнО
# Результат: ПИТОН - ЭТО УДОБНО

text = input("Введите строку: ")

if text.isupper() or text.islower():
    print("Текст полностью заглавный или строчный")
else:
    count_lower = 0
    count_upper = 0

    for letter in text:
        if letter.islower():
            count_lower += 1
        else:
            count_upper += 1

    if count_upper > count_lower:
        print(text.upper())
    else:
        print(text.lower())

# Вариант от скилбокс:

# text = input("Введите текст: ")
# lowers = len([letter for letter in text if letter.islower()])
# uppers = len([letter for letter in text if letter.isupper()])
#
# if lowers > uppers:
#     print("Результат:", text.lower())
# else:
#     print("Результат:", text.upper())
# Задача 3. Аналог Steam.
# Вы пишете программу-инсталлятор для компьютерной игры. Пока инсталлятор скачивает
# обновление, для пользователя необходимо отображать количество скачанных процентов,
# чтобы он понимал, успеет ли заварить чай, прежде чем завершится процесс. Каждое
# обновление игры требует разного количества мегабайтов, при этом у разных игроков
# разная скорость интернет-соединения.
# Что нужно сделать.
# Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость
# интернет-соединения в мегабайтах в секунду. Для каждой секунды программа должна рассчитывать
# и выводить на экран процент скачанного объёма до тех пор, пока скачивание не завершится. В
# конце программа должна показать, сколько секунд заняло скачивание обновления. Обеспечьте
# контроль ввода.
# Пример.
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения: 27
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

import math

download_size = int(input("Укажите размер файла для скачивания: "))
download_speed = int(input("Какова скорость вашего соединения: "))
size_range = math.ceil(download_size / download_speed)
percent = 0
downloaded = 0

if download_size < 0 or download_speed < 0:
    print("Размер обновления и скорость соединения не могут быть меньше нуля.")
elif download_size < download_speed:
    print(f"Прошло 1 сек. Скачано {download_size} из {download_size} Мб (100%)")
else:
    while downloaded < download_size:
        for sec in range(1, size_range + 1):
            downloaded += download_speed
            percent = math.ceil(100 * (downloaded / download_size))
            if downloaded > download_size:
                downloaded = download_size
                percent = 100
            print(f"Прошло {sec} сек. Скачано {downloaded} из {download_size} - {percent} %")

# download_size = int(input("Укажите размер файла для скачивания: "))
# download_speed = int(input("Какова скорость вашего соединения: "))
# size_range = math.ceil(download_size / download_speed)
# procent = 0
# if download_size < 0 or download_speed < 0:
#     print("Размер обновления и скорость соединения не могут быть меньше нуля.")
# elif download_size < download_speed:
#     print(f"Прошло 1 сек. Скачано {download_size} из {download_size} Мб (100%)")
# else:
#     for sec in range(1, size_range + 1):
#         procent = math.ceil(100 * (download_speed / download_size))
#         print(f"Прошло {sec} сек. Скачано {download_speed} из {download_size} - {procent} %")
#         download_speed += 27
#         if download_speed > download_size:
#             download_speed = download_size
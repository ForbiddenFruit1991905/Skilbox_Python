# list_values = (1, 2, 3) # Есть неизменяемый объект (кстати, попробуйте потом повторить этот код с изменяемым объектом)
# hash_value = hash(list_values) # Применим к этому объекту функцию hash
# print(hash_value) # Проверим, что получилось (бессмысленный набор чисел)
# hash_value_2 = hash(list_values) # Попробуем ещё раз
# print(hash_value_2) # Опять набор чисел
# print(hash_value == hash_value_2) # И он в точности равен первому
# str_value = 'jgjdd'
# hash_value = hash(str_value)

# unhashable types:
# list_values = [1, 2, 3]
# hash_value = hash(list_values)
# set_values = {1, 2, 3}
# hash_value = hash(set_values)



# def simple_hash(input_string): # На вход получаем строку
#     hash_value = 0
#     for char in input_string: # Запускаем цикл по символам строки
#         hash_value += ord(char) # Суммируем код каждого символа
#     return hash_value # На выходе получаем сумму — некое числовое значение
#
# some_string = input("Введите строку: ")
# result = simple_hash(some_string)
# print(result)



# tuple_example = (1, 2, 3) # Возьмём тот же кортеж
# print(hash(tuple_example)) # Его хеш при каждом запуске может отличаться
# # При моём запуске хеш был равен числу 529344067295497451
# hash_dict = {(1, 2, 3): 'hello'} # Если я захочу создать словарь с этим кортежем,
# # то «под капотом» будет создан массив, в котором по индексу 529344067295497451
# # будет храниться пара (1, 2, 3) и 'hello'
#
#
# data = {
#     (1, 2, 3): 'hello',
#     (4, 5, 6): 'world',
#     (7, 8, 9): 'python'
# }
#
# # Создаем обратный словарь: хеш ключа → ключ
# hash_to_key = {hash(key): key for key in data.keys()}
#
# # Допустим, у нас есть хеш
# some_hash = hash((1, 2, 3))
#
# # Получаем ключ по хешу
# key = hash_to_key.get(some_hash)
#
# if key is not None:
#     print(f"Ключ по хешу: {key}")
#     print(f"Значение из словаря: {data[key]}")
# else:
#     print("Ключ по такому хешу не найден")
# # или так:
# if some_hash in hash_to_key:
#     key = hash_to_key[some_hash]
#     print(f"Ключ по хешу: {key}")
#     print(f"Значение из словаря: {data[key]}")
# else:
#     print("Ключ по такому хешу не найден")



def rabin_karp_search(text, pattern):
    # Проверяем случаи, когда текст или подстрока пустые
    if not text or not pattern:
        return []

    # Вычисляем хеш-значение для подстроки и первого окна текста
    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])

    matches = [] # Список индексов совпадений

    # Проходим по тексту с помощью скользящего окна
    for i in range(len(text) - len(pattern) + 1):
        # Если хеш-значения совпадают, сравниваем каждый символ окна с подстрокой
        if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
            # Стоит уточнить, что благодаря ленивому выполнению Python, если первое
            # условие в связке AND вернёт False, то второе не будет запускаться вообще
            matches.append(i)

        # Обновляем хеш-значение для следующего окна
        window_hash = hash(text[i + 1:i + len(pattern) + 1])

    return matches

# Пример использования
text = "abracadabra"
pattern = "cad"
matches = rabin_karp_search(text, pattern)
print(f"Совпадения найдены на позициях: {matches}")
# Задача 1. Заказ фруктов
# В торговую компанию пришёл заказ:
# order = {'apple': 2,
#          'banana': 3,
#          'pear': 1,
#          'watermelon': 10,
#          'chocolate': 5}
# Ключи — названия товаров, значения — необходимое количество килограммов.
# При помощи метода get и установки значения по умолчанию проверьте, есть ли
# товар на складе, и получите его цену. Если товара нет, то по умолчанию получите 0.
# Подсчитайте итоговую выручку компании по имеющимся товарам.
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# Ключи — названия товаров, значения — цена за один килограмм.
# Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных товаров,
# и выведите итоговую сумму в консоль.
# Если искомого товара нет на складе, то по умолчанию получите 0. В этом поможет метод get и
# установка значения по умолчанию.

# order = {'apple': 2,
#          'banana': 3,
#          'pear': 1,
#          'watermelon': 10,
#          'chocolate': 5}
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for item in order:
#     if item in incomes:
#         # print(item, "-", incomes[item])
#         print(item, "-", incomes.get(item))
#     else:
#         print(f"Такого товара ({item}) нет в наличие")
#
# summ = 0
# for item in order:
#     if item in incomes:
#         quantity = order[item]
#         price = incomes.get(item)
#         total_price = quantity * price
#         summ += total_price
#         print(f'Общая цена за товар ({item}) в кол-ве {quantity} составит {total_price}')
# print(f'Общая стоимость заказа составит {summ}')
#
# # или так
# total_sum = sum(
#     order[item] * incomes[item]
#     for item in order
#     if item in incomes
# )
# print(f'Общая стоимость заказа составит {total_sum}')

# Вариант от скилбокса
# result_sum = 0
# for fruit_name in order:
#     cost = incomes.get(fruit_name, 0) * order[fruit_name]
#     result_sum += cost
#
# print("Итоговая стоимость товаров из заказа составляет:", result_sum)

# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет,
# а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
# Напишите программу, которая выводит на экран следующие данные в разных строках:
# Все члены команды А, которые отдыхают.
# Все члены команды B, которые тренируются.
# Все члены команды C, которые путешествуют.

team_a_rest = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
team_a = ', '.join(team_a_rest)
print(f'Все члены команды А, которые отдыхают {team_a}')

team_b_training = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
team_b = ', '.join(team_b_training)
print(f'Все члены команды B, которые тренируются {team_b}')

team_c_travel = [
    player['name'] for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
team_c = ', '.join(team_c_travel)
print(f'Все члены команды C, которые путешествуют {team_c}')

# Вариант от скилбокса
# Чтобы не прописывать решение "в лоб", вручную подставляя статус и команду - попробуем сформировать дополнительные словарь и список,
# чтобы автоматизировать этот процесс:
# help_dict = {"Rest": "отдыхают",
#              "Training": "тренируются",
#              "Travel": "путешествуют"}
# team_order = ["A", "B", "C"]
# # Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать одну из команд:
# index = 0
# for state in help_dict:
#     print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
#     for player in players_dict.values():
#         if player["status"] == state and player["team"] == team_order[index]:
#             print(player["name"])
#     index += 1
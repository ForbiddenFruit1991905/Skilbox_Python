# Задача 1. Конвертация.
# При оплате покупок картой за рубежом банки делают конвертацию через промежуточную валюту.
# Например, если оплачивать отечественной картой товар в евро, то сначала эта сумма
# конвертируется в доллары, а потом — в рубли.
# Что нужно сделать.
# Напишите программу, которая получает на вход стоимость покупки в евро, а затем выводит
# ответ в рублях. Представим, что мы живём в альтернативной реальности, где 1 евро = 1.25
# доллара, а 1 доллар = 60.87 рубля.

cost_euro = int(input("Стоимость покупки в евро: "))

print("Стоимость в рублях:", round((cost_euro * 1.25 * 60.87), 2))
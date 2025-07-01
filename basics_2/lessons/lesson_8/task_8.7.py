def print_tax_document(tax, *args, **kwargs):
    price_sum = 0
    for i_price in args:
        price_sum = price_sum + i_price * tax / 100
    print('Сумма цен с учетом  налога: ', price_sum)

    for i_info, i_value in kwargs.items():
        print('{}: {}'.format(i_info, i_value))


my_tax = int(input('Величина налога: '))
print_tax_document(my_tax, 1000, 950, 880, 920, 990,
                   year=1997, doc_type='Report', operation_id=1110034)
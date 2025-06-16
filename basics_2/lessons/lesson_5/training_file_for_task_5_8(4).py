# some_list = '10.20.30.40'.split('.')
# new_list = []
# for i in some_list:
#     new_list.append(int(i))
# print(some_list)
# print(new_list)



# f_list = ['128.0.0.255', ['file_1.txt document_2024.docx notes2022.txt']]
# ip_str = f_list[0]
# ip_parts = ip_str.split('.')
# int_ip = [int(ip) for ip in ip_parts]
# print(int_ip)



data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.dosx"]]
    ]

# для ip-адресов
# ip_parts = [parts[0].replace(',', '.') if ',' in parts[0] else parts[0] for parts in data]
# ip_part = [ip_str.split('.') for ip_str in ip_parts]
# int_ip = [[int(ip_quarter) if ip_quarter.isdigit() else int(ip_quarter[1:]) for ip_quarter in ip] for ip in ip_part]
# check_num = [[-num_ip if num_ip < 0 else 255 if num_ip > 255 else num_ip for num_ip in int_ip_part] for int_ip_part in int_ip]
# print(ip_parts)
# print(ip_part)
# print(int_ip)
# print(check_num)


bad_start = ["@", "№", "$", "%", "^", "&", "*", "()"]
addresses_sublist = [parts[1][0].split(' ') for parts in data]
file_index = [
    (
        filename_address if (filename_address.endswith('.txt') or filename_address.endswith('.docs'))
        else filename_address[:-5] + (
            '.docs' if ('d' in filename_address[-5:] or 'o' in filename_address[-5:])
            else '.txt' if ('t' in filename_address[-4:] or 'x' in filename_address[-4:])
            else '.txt'
        )
    ) if not any(filename_address.startswith(bad) for bad in bad_start)
    else filename_address[1:]
    for addresses in addresses_sublist
    for filename_address in addresses
]
address_finish = [file_index[i:i+3] for i in range(0, len(file_index), 3)]

print(addresses_sublist)
print(file_index)
print(address_finish)

# for sublist in data:
#     if sublist[0].split('.') in ip_list:
#         file_index = sublist[1].split()
#         for i in sublist:
#             if file_index[i].endswith('.txt') or file_index[i].endswith('.docs') and not file_index[i].startswith(bad_start):
#                 new_data.append(sublist)

"""
Задача на программирование: декодирование Хаффмана
"""

sym_count, len_str = map(int, input().split())

dict_codes = dict()
for i in range(sym_count):
    sym, code = map(str, input().split(': '))
    dict_codes[code] = sym

cur_code = ''
for i in input():
    cur_code += i
    if cur_code in dict_codes.keys():
        print(dict_codes[cur_code], end='')
        cur_code = ''
print()
"""
Задача на программирование: двоичный поиск
"""


def bin_finder(input_array, start, end, key):
    if start > end:
        return -1

    cur_id = (start + end) // 2

    if input_array[cur_id] == key:
        return cur_id + 1

    if input_array[cur_id] > key:
        return bin_finder(input_array, start, cur_id - 1, key)

    return bin_finder(input_array, cur_id + 1, end, key)


input_array_info = [int(i) for i in input().split()]
array = input_array_info[1:]

input_find_keys = [int(i) for i in input().split()]
keys = input_find_keys[1:]

for i in keys:
    print(bin_finder(array, 0, len(array) - 1, i), end=' ')
print()

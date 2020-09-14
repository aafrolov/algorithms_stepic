"""
Задача на программирование: число инверсий
"""
res_inv = 0


def merge(array0, array1):
    result = []
    global res_inv
    it0 = 0
    it1 = 0
    while it0 != len(array0) and it1 != len(array1):
        if array0[it0] <= array1[it1]:
            result.append(array0[it0])
            it0 += 1
        else:
            result.append(array1[it1])
            it1 += 1
            res_inv += len(array0) - it0

    result += array0[it0:]
    result += array1[it1:]

    return result


def insert_sort(input_array, start, end):
    if end == start:
        return [input_array[start]]

    m = (start + end) // 2
    return merge(insert_sort(input_array, start, m), insert_sort(input_array, m + 1, end))


len_array = int(input())
array = [int(i) for i in input().split()]
insert_sort(array, 0, len(array) - 1)
print(res_inv)

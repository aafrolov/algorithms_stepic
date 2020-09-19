"""
Задача на программирование: сортировка подсчётом
"""

size = int(input())
array = [int(i) for i in input().split()]

counter = [0] * 11
for i in array:
    counter[i] += 1

it = 0
for i in counter:
    if i != 0:
        print((str(it) + ' ') * i, end='')
    it += 1
print()

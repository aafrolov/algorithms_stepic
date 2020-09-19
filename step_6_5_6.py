"""
Задача на программирование: точки и отрезки
"""
import random
import bisect


def partition(array, start, end):
    x = array[start]
    #            j
    # | x | <= x | > x |
    j = start
    for i in range(start + 1, end + 1):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]

    array[start], array[j] = array[j], array[start]
    return j


def rand_partition(array, start, end):
    rand_elem = random.randint(start, end)
    array[rand_elem], array[start] = array[start], array[rand_elem]

    x = array[start]
    #            j
    # | x | <= x | > x |
    j = start
    for i in range(start + 1, end + 1):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]

    array[start], array[j] = array[j], array[start]
    return j


def rand_partition_3parts(array, start, end):
    rand_elem = random.randint(start, end)
    array[rand_elem], array[start] = array[start], array[rand_elem]

    x = array[start]
    #            j
    # | x | <= x | > x |
    j = start
    i = start + 1
    end_iter = end
    while i < end_iter + 1:
        if array[i] < x:
            j += 1
            array[i], array[j] = array[j], array[i]
        elif array[i] > x:
            array[end_iter], array[i] = array[i], array[end_iter]
            end_iter -= 1
            i -= 1
        i += 1

    array[start], array[j] = array[j], array[start]
    return j, end_iter


def quick_sort(array, start, end):
    if start >= end:
        return

    mid, mid1 = rand_partition_3parts(array, start, end)
    quick_sort(array, start, mid - 1)
    quick_sort(array, mid1 + 1, end)


num_of_sections, num_of_points = map(int, input().split())
sections_start = []
sections_end = []
for i in range(num_of_sections):
    start, end = map(int, input().split())
    sections_start.append(start)
    sections_end.append(end)

points = [int(i) for i in input().split()]
quick_sort(sections_start, 0, len(sections_start) - 1)
quick_sort(sections_end, 0, len(sections_end) - 1)

for point in points:
    it_start = bisect.bisect_right(sections_start, point, 0, len(sections_start))
    it_end = bisect.bisect_left(sections_end, point, 0, len(sections_start))

    print(it_start - it_end, end=' ')

print()

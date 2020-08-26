"""
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
хотя бы одну из точек.
Каждая из последующих nn строк содержит по два числа,
задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько,
выведите любое из них.
"""

n = int(input())

lines = list()
for i in range(n):
    x0, x1 = map(int, input().split())
    lines.append((x0, x1))

sort_lines = sorted(lines, key=lambda x: x[1])

result = list()
result.append(sort_lines[0][1])
for line in sort_lines:
    if line[0] <= result[-1]:
        continue
    result.append(line[1])

print(len(result))
for i in result:
    print(i, end=' ')

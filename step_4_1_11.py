"""
Задача на программирование: различные слагаемые
"""
num = int(input())
cur_step = 1
result = list()
while num >= cur_step:
    result.append(cur_step)
    num -= cur_step
    cur_step += 1

result[-1] += num
print(len(result))
for i in result:
    print(i, end=' ')

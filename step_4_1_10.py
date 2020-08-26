"""
Задача на программирование: непрерывный рюкзак
"""

n, w = map(int, input().split())

things = list()
for i in range(n):
    cost, numbers = map(int, input().split())
    things.append((cost, numbers))

sort_things = sorted(things, key=lambda x: x[0]/x[1], reverse=True)

res_cost = 0
for thing in sort_things:
    if w == 0:
        break
    cur_w = min(thing[1], w)
    w -= cur_w
    res_cost += cur_w * thing[0] / thing[1]

print(res_cost)

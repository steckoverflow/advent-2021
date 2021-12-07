# 7-1
with open("input7-1.txt", "r") as f:
    data = f.read()

import time

numbers = [int(num) for num in data.split(",")]
mn, mx = min(numbers), max(numbers)
total_cost = len(numbers)**2
minimum_num = None

for mv in range(mn, mx):
    cost = 0
    for num in numbers:
        cost += abs((num)-mv)
    if cost < total_cost:
        total_cost = cost
        minimum_num = mv
        print(f"Cost={cost} is less than total cost={total_cost} for number={mv}")

print(f"Result 1= {total_cost}, min-num={minimum_num}")

t0 = time.perf_counter()

from functools import cache

@cache
def sum_prevs(n):
    t = 0
    while n >= 1:
        t += n
        n -= 1
    return t
    

numbers = [int(num) for num in data.split(",")]
mn, mx = min(numbers), max(numbers)

for mv in range(mn, mx):
    cost = 0
    for num in numbers:
        cost += sum_prevs(abs((num)-mv))
    if mv == mn:
        total_cost = cost
    if cost < total_cost:
        print(f"Cost={cost} is less than total cost={total_cost} for number={mv}")
        total_cost = cost
        minimum_num = mv

print(f"Result 2= {total_cost}, min-num={minimum_num}")

t1 = time.perf_counter()
print(t1-t0)
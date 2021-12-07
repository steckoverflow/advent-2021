# 7-1
with open("input7-1.txt", "r") as f:
    data = f.read()


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

def sum_prevs(n):
    t = 0
    while n >= 1:
        t += n
        n -= 1
    return t
    

numbers = [int(num) for num in data.split(",")]
mn, mx = min(numbers), max(numbers)

print("Len of numbers=", len(numbers))

for mv in range(mn, mx):
    print("Testing mv=", mv)
    cost = 0
    for num in numbers:
        cost += sum_prevs(abs((num)-mv))
    if mv == mn:
        print(f"Move={mv}, Min={mn}")
        total_cost = cost
    if cost < total_cost:
        print(f"Cost={cost} is less than total cost={total_cost} for number={mv}")
        total_cost = cost
        minimum_num = mv

print(f"Result 2= {total_cost}, min-num={minimum_num}")

# 11 
# 1 1
# 2 2
# 3 3
# 4 4
# 
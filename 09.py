import io

with io.open("input9-1.txt", "r") as f:
    dt = f.read()

from copy import deepcopy

s = []
m = [list(v) for v in dt.split("\n") if len(v) > 0]
f = deepcopy(m)
basins = []


def calculate_basin(m, j, i, b, v):
    """Recursively calculate basin, i.e. all numbers around a low-point"""
    print(f"basin={b} row={j} col={i}")
    
    if (j, i) not in v:
        v.append((j, i))

        if j - 1 >= 0 and int(m[j-1][i]) != 9 and int(m[j-1][i]) > int(m[j][i]):
            print("Basin=Above is higher")
            b.append(int(m[j-1][i]))
            calculate_basin(m, j - 1, i, b, v)

        if j + 1 < len(m) and int(m[j+1][i]) != 9 and int(m[j+1][i]) > int(m[j][i]):
            print("Basin= Below is higher")
            b.append(int(m[j+1][i]))
            calculate_basin(m, j + 1, i, b, v)

        if i - 1 >= 0 and int(m[j][i-1]) != 9 and int(m[j][i-1]) > int(m[j][i]):
            print("Basin=Left is higher")
            b.append(int(m[j][i-1]))
            calculate_basin(m, j, i - 1, b, v)

        if i + 1 < len(m) and int(m[j][i+1]) != 9 and int(m[j][i+1]) > int(m[j][i]):
            print("Basin=Right is higher")
            b.append(int(m[j][i+1]))
            calculate_basin(m, j, i + 1, b, v)
        
        return b # return basin

print("\nBefore calculation")
for row in f:
    print("".join(row))

for j, r in enumerate(m):
    for i, c in enumerate(r):
        # print(j, i, c) # check up, down, left, right (skipping edge cases)
        if not j == 0:  # UP
            u = int(m[j-1][i])
            if u <= int(c):
                f[j][i] = "."
                continue

        if not j == len(m) - 1:  # DOWN
            b = int(m[j+1][i])
            if b <= int(c):
                f[j][i] = "."
                continue

        if not i == 0:  # LEFT
            l = int(m[j][i-1])
            if l <= int(c):
                f[j][i] = "."
                continue

        if not i == len(r) - 1:  # RI
            rt = int(m[j][i+1])
            if rt <= int(c):
                f[j][i] = "."
                continue

        f[j][i] = c
        basins.append(calculate_basin(m, j, i, [int(c)], []))
        # NOTE: unclear if I need + 1 but it doesn't work?
        s.append(int(c) + 1)

print("\nAfter calculation")
for row in f:
    print("".join(row))

print("Res 1=", sum(s))

basins.sort(key=len)
print(len(basins[0]) * len(basins[1]) * len(basins[2]))

d = dt.splitlines()
d = [[int(value) for value in row] for row in d]
v = []
b = []

def basin(d, x, y, count = 0):
    if (x, y) not in v:
        v.append((x, y))
        if d[x][y] != 9:
            count += 1
            if x < (len(d) -1):
                count += basin(d, x+1, y)
            if x > 0:
                count += basin(d, x-1, y)
            if y > 0:
                count += basin(d, x, y-1)
            if y < (len(d[0]) -1):
                count += basin(d, x, y+1)
            return count
    return 0

for x in range(len(d)):
    for y in range(len(d[0])):
        basins.append(basin(d, x, y))

top_basins = list(sorted(basins))[-3:]
print(top_basins[0] * top_basins[1] * top_basins[2])
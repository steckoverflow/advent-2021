with open("input1-1.txt", "r") as f:
    lines = [r.replace("\n","") for r in f.readlines()]

groups = [[int(i) for i in lines[i:i+3]] for i in range(len(lines))]

prev = None
curr = None
cnt = 1


while lines: # 180 152 159
    curr = lines.pop(0)
    if prev is not None and curr >= prev:
        #print(f"{curr} > {prev}")
        cnt += 1
    prev = curr

print(cnt)

prev = None
curr = None
cnt = 0

while groups:
    curr = groups.pop(0)
    if prev is not None and sum(curr) > sum(prev):
        cnt += 1
    prev = curr

print(cnt)
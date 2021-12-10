with open("input10-1.txt", "r") as f:
    data = f.read().splitlines()

# 10-1
total = 0
valid_open, valid_close = "([{<", ")]}>"
close_map, open_map = {")": "(", "]": "[", "}": "{", ">": "<"}, {"(": ")", "[": "]", "{": "}", "<": ">"}
pts_map, score_map, corrupt_idx = {")": 3, "]": 57, "}": 1197, ">": 25137}, {")": 1, "]": 2, "}": 3, ">": 4}, []

for j, row in enumerate(data):
    opn = []
    for char in row:
        if char in valid_open:
            opn.append(char)
        if char in valid_close:
            lst_opn = opn.pop()
            if close_map[char] != lst_opn:
                #print(f"Row {j} corrupted. Removing from incomplete")
                total += pts_map[char]
                corrupt_idx.append(j)

print("Res 1=", total)

data = [row for i, row in enumerate(data) if i not in corrupt_idx] # incomplete row for part 2
all_remainers = []

for j, row in enumerate(data):
    opn = []
    remaining = []
    for char in row:
        if char in valid_open:
            opn.append(char)
        if char in valid_close:
            lst_opn = opn.pop()
    
    for char in opn[::-1]: # reverse
        remaining.append(open_map[char])
    all_remainers.append(remaining)

scores = []

for remainder in all_remainers:
    score = 0
    for char in remainder:
        score = score * 5
        score = score + score_map[char]
    scores.append(score)

middleIdx = int((len(scores) - 1)/2)
print("Res 2=", sorted(scores)[middleIdx])



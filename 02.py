#### 2-1

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

with open("input2-1.txt", "r") as f:
    data = [r.replace("\n","") for r in f.readlines()]

pos = {"x":0, "y":0}

for change in data:
    direction, value = change.split(" ")
    match direction:
        case "forward":
            pos["x"] += int(value)
        case "down":
            pos["y"] += int(value)
        case "up":
            pos["y"] -= int(value)

print(pos)
print("Result 1: ", pos["x"] * pos["y"])

#### 2-2

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

stats = {"x":0, "y":0, "aim": 0}

for change in data:
    direction, value = change.split(" ")
    #print("Iteration: ", stats, stats["x"] * stats["y"])
    match direction:
        case "forward":
            stats["x"] += int(value)
            stats["y"] += stats["aim"] * int(value)
        case "down":
            stats["aim"] += int(value)
        case "up":
            stats["aim"] -= int(value)

print(stats)
print("Result 1: ", stats["x"] * stats["y"])

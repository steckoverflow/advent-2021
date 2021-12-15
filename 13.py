with open("input13-1.txt", "r") as f:
    d = f.read().splitlines()
    
def print_grid(grid):
    for row in grid:
        print("".join(row))

empty_line = [i for i, v in enumerate(d) if len(v) == 0][0]
positions, folds = d[0: empty_line], d[empty_line + 1:]
mx, my = max([int(v.split(",")[0]) for v in positions]), max([int(v.split(",")[1]) for v in positions])

# build grid
grid = []
for y in range(my + 1):
    grid.append([])
    for x in range(mx + 1):
        grid[y].append(".")

for position in positions:
    x, y = map(int, position.split(","))
    grid[y][x] = "#"

print("Before start")
print_grid(grid)

for fold in folds:
    axis, pos = fold.split(" ")[2:][0].split("=")
    
    if axis == "y":
        new_grid = grid[:int(pos)]
        for j, row in enumerate(grid[int(pos) + 1:]):
            for i, col in enumerate(row):
                if col == "#":
                    flip_j = abs((len(grid[int(pos) + 1:])-1) - j)
                    new_grid[flip_j][i] = "#"
        grid = new_grid
        print("grid after fold y")
        print_grid(grid)
    
    if axis == "x":
        new_grid = [row[:int(pos)] for row in grid]
        for j, row in enumerate(grid):
            for i, col in enumerate(row[int(pos) + 1:]):
                if col == "#":
                    flip_i = abs((len(row[int(pos) + 1:])-1) - i)
                    new_grid[j][flip_i] = "#"
        grid = new_grid
        print("grid after fold x")
        print_grid(grid)
    
    break # folding just once

print("Result 1=", sum([1 for row in grid for v in row if v == "#"]))
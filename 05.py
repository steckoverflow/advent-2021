# 5-1
with open("input5-1.txt", "r") as f:
    data = f.read().split("\n")

lines = []


class Line():
    def __init__(self, from_x, from_y, to_x, to_y) -> None:
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    def is_horizontal(self):
        return self.from_x != self.to_x and self.from_y == self.to_y

    def is_vertical(self):
        return self.from_y != self.to_y and self.from_x == self.to_x
    
    def is_diagonal(self):
        return self.from_x != self.to_x and self.from_y != self.to_y
    
    def __repr__(self) -> str:
        return f"Line(from_x={self.from_x}, from_y={self.from_y}, to_x={self.to_x}, to_y={self.to_y})"


# Clean data and add lines
for line in data:
    line_from, line_to = line.split("->")
    from_x, from_y = line_from.split(",")
    to_x, to_y = line_to.split(",")

    lines.append(Line(int(from_x.strip()), int(from_y.strip()),
                 int(to_x.strip()), int(to_y.strip())))

# find max_x, max_y
max_x = max_y = 0
for line in lines:
    if line.from_x > max_x:
        print(f"found new max_x={line.from_x}")
        max_x = line.from_x
    if line.to_x > max_x:
        print(f"found new max_x={line.to_x}")
        max_x = line.to_x
    if line.from_y > max_y:
        print(f"found new max_y={line.from_y}")
        max_y = line.from_y
    if line.to_y > max_y:
        print(f"found new max_y={line.to_y}")
        max_y = line.to_y

print(f"max_x={max_x}")
print(f"max_y={max_y}")


class Grid():
    grid = []

    def __init__(self, max_x, max_y) -> None:
        for _ in range(max_y + 1):
            row = []
            for _ in range(max_x + 1):
                row.append(0)
            self.grid.append(row)

    def plot_line(self, line):
        if line.is_horizontal():
            #print("Plotting horizontal line")
            for i in range(max(line.from_x, line.to_x)-min(line.from_x, line.to_x) + 1):
                #print("i ", i, " in ", max(line.from_x, line.to_x)-min(line.from_x, line.to_x))
                self.grid[line.from_y][min(line.from_x, line.to_x) + i] += 1


        elif line.is_vertical():
            #print("Plotting vertical line")
            for i in range(max(line.from_y, line.to_y)-min(line.from_y, line.to_y) + 1):
                #print("i ", i, " in ", max(line.from_y, line.to_y)-min(line.from_y, line.to_y))
                self.grid[min(line.from_y, line.to_y) + i][line.from_x] += 1
        
        elif line.is_diagonal():
            print("Plotting diagonal line")
            # because lines are always going to be 45 degrees I can just chicken out and go over +1 on both sides
            for i in range(max(line.from_y, line.to_y)-min(line.from_y, line.to_y) + 1):
                if line.from_x > line.to_x:
                    x = line.from_x - i
                elif line.from_x < line.to_x:
                    x = line.from_x + i
                if line.from_y > line.to_y:
                    y = line.from_y - i 
                elif line.from_y < line.to_y:
                    y = line.from_y + i
            
                self.grid[y][x] += 1
                
    def print_grid(self):
        print("=== Grid ===")
        for row in self.grid:
            print(row)

    def count_overlap(self):
        return sum([1 for v in [v for sub in self.grid for v in sub] if v > 1])


grid = Grid(max_x, max_y)
#grid.print_grid()

for line in lines:
    print(line)
    grid.plot_line(line)
    #grid.print_grid()

grid.print_grid()
print("Result 2: ", grid.count_overlap())



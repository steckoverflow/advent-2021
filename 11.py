from pprint import pprint
with open("input11-1.txt", "r") as f:
    d = f.read().splitlines()

MAX_Y = len(d)
MAX_X = len(d[0])


class Octopus:
    total_flashes = 0  # tracks total flashes for all octopus
    steps = {}  # tracks so that one octopus can only flash once per step

    def __init__(self, energy, pos_y, pos_x) -> None:
        self.energy = energy
        self.pos_y = pos_y
        self.pos_x = pos_x

    def increase_energy(self, current_step):
        if current_step not in Octopus.steps:
            Octopus.steps[current_step] = []

        chain_reactions = []

        # if I haven't flashed I can increase energy
        if (self.pos_y, self.pos_x) not in Octopus.steps[current_step]:
            self.energy += 1

        if self.energy > 9:  # 9-causes flash, calculate surronding positions
            self.energy = 0
            Octopus.total_flashes += 1

            # add myself so I don't flash again
            Octopus.steps[current_step].append((self.pos_y, self.pos_x))

            if self.pos_y > 0:  # up
                chain_reactions.append((self.pos_y - 1, self.pos_x))
                if self.pos_x > 0:  # up-left
                    chain_reactions.append((self.pos_y - 1, self.pos_x - 1))
                if self.pos_x < MAX_X - 1:  # up-right
                    chain_reactions.append((self.pos_y - 1, self.pos_x + 1))
            if self.pos_y < MAX_Y - 1:  # down
                chain_reactions.append((self.pos_y + 1, self.pos_x))
                if self.pos_x > 0:  # down-left
                    chain_reactions.append((self.pos_y + 1, self.pos_x - 1))
                if self.pos_x < MAX_X - 1:  # down-right
                    chain_reactions.append((self.pos_y + 1, self.pos_x + 1))
            if self.pos_x > 0:  # left
                chain_reactions.append((self.pos_y, self.pos_x - 1))
            if self.pos_x < MAX_X - 1:  # right
                chain_reactions.append((self.pos_y, self.pos_x + 1))

        return chain_reactions

    def __repr__(self) -> str:
        return f"{self.energy}"


# Build grid
grid = []

for y in range(MAX_Y):
    grid.append([])
    for x in range(MAX_X):
        grid[y].append(Octopus(int(d[y][x]), y, x))


all_flashed = False

# Run computations!
for step in range(1000):
    if all_flashed:
        break
    for j, row in enumerate(grid):
        for i, octopus in enumerate(row):
            chain_reactions = octopus.increase_energy(str(step))
            while chain_reactions:
                #print(f"On chain reaction from source {j}, {i}. Current reactions to process={chain_reactions}")
                y, x = chain_reactions.pop(0)
                more_reactions = grid[y][x].increase_energy(str(step))
                chain_reactions = chain_reactions + more_reactions

            # if len(all flashes for step=) == MAX_Y * MAX_X means all octopusses flashed during this step and we have to return the round
            if len(Octopus.steps[str(step)]) == MAX_X * MAX_Y:
                all_flashed = True
                print(f"Result 2.... All flashed on step= {step+1}")

    if step + 1 == 100:
        print("Result 1=", grid[0][0].total_flashes)

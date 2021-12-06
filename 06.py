# 5-1
with open("input-test", "r") as f:
    data = f.read()

### NOTE: have to admit I got some help to understand this ingenius solution.

state = [0 for _ in range(9)]
for f in data.strip().split(','):
    state[int(f)] += 1

print(f"Initial state: {state}, total fish: {sum(state)}")

for day in range(1, 257):
    popped = state.pop(0)
    state.append(popped)
    state[6] += popped
    if day == 18 or day == 80 or day == 256:
        print(f"After {day} days: {state}, total fish: {sum(state)}")



#14-1
with open("input14-1.txt", "r") as f:
    d = f.read().splitlines()

empty_line = [i for i, v in enumerate(d) if len(v) == 0][0]
seq, raw_mappings = d[0: empty_line][0], d[empty_line + 1:]

mappings = {}

for mapping in raw_mappings:
    pattern, insert = map(str.strip, mapping.split("->"))
    mappings[pattern] = insert

from datetime import datetime
n = datetime.now()

for s in range(10):
    print(f"iteration={s} {datetime.now() - n}")
    new_str = seq
    inserts = 0
    for i in range(len(seq)):
        try:
            chunk = seq[i:i+2]
            if chunk in mappings.keys():
                #print(f"found chunk={chunk} in segment={seq} at pos[{i},{i+2}]")
                c = mappings[chunk]
                #print(f"inserting {c} into {new_str} at pos {i+inserts+1}")
                new_str = f"{new_str[:i+inserts+1]}{c}{new_str[i+inserts+1:]}"
                inserts += 1
        except:
            pass

    seq = new_str
    #print(f"After step {s+1}: {seq}")

from collections import Counter
def chunk_string(s, n):
    return [s[i:i+n] for i in range(len(s)-n+1)]

counter = Counter(chunk_string(seq, 1))
print(max(counter.values())-min(counter.values()))

# 14-2
from datetime import datetime
with open("input14-1.txt", "r") as f:
    d = f.read().splitlines()

empty_line = [i for i, v in enumerate(d) if len(v) == 0][0]
seq, raw_mappings = d[0: empty_line][0], d[empty_line + 1:]

mappings = {}
for mapping in raw_mappings:
    pattern, insert = map(str.strip, mapping.split("->"))
    mappings[pattern] = insert

n = datetime.now()

group_counter = {}
# initialising results
for l in [seq[i:i+2] for i in range(len(seq)-2+1)]:
    if l not in group_counter:
        group_counter[l] = 1
    else:
        group_counter[l] += 1

print("Groups initialised: ", group_counter)

char_counter = {}
for char in seq:
    if char not in char_counter:
        char_counter[char] = 1
    else:
        char_counter[char] += 1

for step in range(40):
    current_counter = {k: v for k, v in group_counter.items()}
    result_keys = [k for k, v in current_counter.items() if v > 0]

    for chunk in result_keys:
        if chunk in mappings.keys():
            spawns = group_counter[chunk]
            current_counter[chunk] -= spawns

            c = mappings[chunk]
            chunk_a = chunk[:1] + c
            chunk_b = c + chunk[1:]

            if chunk_a not in current_counter:
                current_counter[chunk_a] = spawns
            else:
                current_counter[chunk_a] += spawns

            if chunk_b not in current_counter:
                current_counter[chunk_b] = spawns
            else:
                current_counter[chunk_b] += spawns

            if c not in char_counter:
                char_counter[c] = spawns
            else:
                char_counter[c] += spawns

    group_counter = current_counter

print(max(char_counter.values()) - min(char_counter.values()))
print(datetime.now() - n, "time to execute part 12")
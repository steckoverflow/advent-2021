# 8-1
import io

with io.open("input8-1.txt", "r") as f:
    data = [x.split("|") for x in f]

tot = 0
for line in data:
    for each in line[1].split():
        if len(each) in (2, 3, 4, 7):
            tot += 1

print("Result 1=", tot)
import itertools
from pprint import pprint

with open("input8-1.txt") as fin:
    raw_data = fin.read().strip().split("\n")
    data = [
        [
            sorted(line[:line.index("|") - 1].split(" ")),
            line[line.index("|") + 2:].split(" ")
        ] for line in raw_data
    ]

# No cred for second part. I'm a shitty developer. I understood after way to long how to solve it but couldn't bother to solve it. #sob
digits_key = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]
digits = sorted(digits_key)
digits = tuple(digits)

ans = 0

for line in data:
    clues = line[0]
    assert len(clues) == 10

    num = line[1]

    # Try all possible substitutions
    for sigma in itertools.permutations("abcdefg"):
        # Reencode digits
        key = {}
        for c in "abcdefg":
            key[c] = sigma["abcdefg".index(c)]

        new_clues = [] * 10
        for clue in clues:
            x = ""
            for char in clue:
                x += key[char]
            x = "".join(sorted(x))
            new_clues.append(x)

        new_clues.sort()

        if tuple(new_clues) == digits:
            # Get the number it's supposed to be
            n = []
            for d in num:
                x = ""
                for char in d:
                    x += key[char]
                x = "".join(sorted(x))
                n.append(digits_key.index(x))

            ans += int("".join([str(i) for i in n]))

            break

print(ans)
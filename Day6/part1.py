from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")
with open(PATH, "rt") as stream:
    inp = stream.readlines()

inp[0] = inp[0].replace("\n", "")

# Data in correct format
T_MAX = [int(x) for x in filter(lambda x: x != "", inp[0][inp[0].find(":") + 1:].split(" "))]
D_MAX = [int(x) for x in filter(lambda x: x != "", inp[1][inp[1].find(":") + 1:].split(" "))]

# Iterate per second of holding to check if d > Dmax, store number in list
ways_to_win = []

for i, t in enumerate(T_MAX):
    ways = 0

    for s in range(t):
        d = s * (t - s)

        if d > D_MAX[i]:
            ways += 1
    
    ways_to_win.append(ways)

mult = 1
for w in ways_to_win:
    mult *= w

print(mult)

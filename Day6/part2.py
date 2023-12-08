from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")
with open(PATH, "rt") as stream:
    inp = stream.readlines()

inp[0] = inp[0].replace("\n", "")

T_MAX = int(inp[0][inp[0].find(":") + 1:].replace(" ", ""))
D_MAX = int(inp[1][inp[1].find(":") + 1:].replace(" ", ""))

ways_to_win = 0

for s in range(T_MAX):
    d = s * (T_MAX - s)

    if d > D_MAX:
        ways_to_win += 1

print(ways_to_win)

from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.read()

data = [[point for point in line] for line in inp.split("\n")]

empty_rows = []
empty_columns = []

for row, line in enumerate(data):
    if "#" not in line:
        empty_rows.append(row)

for col in range(len(data[0])):
    column = [data[r][col] for r in range(len(data))]

    if "#" not in column:
        empty_columns.append(col)

for row in empty_rows[::-1]:
    data.insert(row, ["." for _ in range(len(data[0]))])

for col in empty_columns[::-1]:
    for row, line in enumerate(data):
        line.insert(col, ".")

galaxy_coords = []

for row, line in enumerate(data):
    for col, point in enumerate(line):
        if point == "#":
            galaxy_coords.append((row, col))

output = 0

for index, g1 in enumerate(galaxy_coords):
    for g2 in galaxy_coords[(index + 1):]:
        output += (abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]))

print(output)

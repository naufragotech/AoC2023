from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.read()

data = [[point for point in line] for line in inp.split("\n")]

connections = {
    "N": {"|": "N", "7": "W", "F": "E"},
    "W": {"-": "W", "L": "N", "F": "S"},
    "S": {"|": "S", "L": "E", "J": "W"},
    "E": {"-": "E", "7": "S", "J": "N"}
}

r0 = c0 = 0

for row, line in enumerate(data):
    for col, symbol in enumerate(line):
        if symbol == "S":
            r0 = row
            c0 = col

loop_found = False
for direction in connections:
    # Starting coordinates
    r, c = r0, c0

    # Ending condition
    dead_end = False

    # Coordinates of the loop points
    coordinates_arr = [(r0, c0)]
    
    while not dead_end and not loop_found:

        connectors = list(connections[direction].keys())

        if direction == "N":
            next_point = data[r - 1][c]
            r1 = r - 1
            c1 = c
        
        elif direction == "W":
            next_point = data[r][c - 1]
            r1 = r
            c1 = c - 1
        
        elif direction == "S":
            next_point = data[r + 1][c]
            r1 = r + 1
            c1 = c
        
        elif direction == "E":
            next_point = data[r][c + 1]
            r1 = r
            c1 = c + 1

        if next_point == "S":
            loop_found = True
            coordinates_arr.append((r1, c1))
        
        else:
            if next_point not in connectors:
                dead_end = True
            
            else:
                r, c = r1, c1
                coordinates_arr.append((r1, c1))
                direction = connections[direction][next_point]
    
    if loop_found:
        break

area = sum(r1 * c2 - r2 * c1 for (r1, c1), (r2, c2) in zip(coordinates_arr, coordinates_arr[1:])) / 2

points_inside = int(abs(area) - 0.5 * len(coordinates_arr[:-1]) + 1)

print(points_inside)



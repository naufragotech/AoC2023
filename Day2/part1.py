from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as s:
    games = s.readlines()

# Convert the data to a better format
data = []

for game in games:
    game = game[game.find(":") + 1:].replace(" ", "")
    sets =  game.split(";")

    game_data = []

    for set in sets:
        set = set.split(",")

        r = g = b = 0

        for color in set:
            if "red" in color:
                r = int(color.replace("red", ""))
            
            elif "green" in color:
                g = int(color.replace("green", ""))
            
            elif "blue" in color:
                b = int(color.replace("blue", ""))
        
        game_data.append((r, g, b))
    
    data.append(game_data)

MAX = (12, 13, 14)

# Check each set of each game against the maximum
x = 0

for index, game in enumerate(data):
    valid = True

    for set in game:
        if set[0] > MAX[0] or set[1] > MAX[1] or set[2] > MAX[2]:
            valid = False
            break
    
    if valid:
        x += (index + 1)

print(x)
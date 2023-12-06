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

# Check for each game the max numbers of red, green and blue cubes in the sets
# The max in the game are the minimum numbers of cubes needed per color
minimums = []

for game in data:
    r = g = b = 0

    for set in game:
        if set[0] > r:
            r = set[0]
        
        if set[1] > g:
            g = set[1]
        
        if set[2] > b:
            b = set[2]
    
    minimums.append((r, g, b))

# Multiply the red x green x blue minimums for each game
powers = [r * g * b for r, g, b in minimums]

print(sum(powers))
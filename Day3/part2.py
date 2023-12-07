from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as s:
    inp = s.readlines()

# Clean data
for index, line in enumerate(inp):
    new_line = line.replace("\n", "")
    inp[index] = new_line

# Declare constants
NUMBERS = [str(i) for i in range(10)]
GEAR_SYMBOL = "*"
INCREMENTS = [-1, 0, 1]

ROW_MAX = len(inp) - 1
COL_MAX = len(inp[0]) - 1

# Function to read get whole number given the adjacent
def get_whole_number(row, col):
    digits = [inp[row][col]]

    # Digits to left (go backwards)
    Ci = col - 1
    while Ci >= 0:
        if inp[row][Ci] in NUMBERS:
            digits.insert(0, inp[row][Ci])
            Ci -= 1
        
        else:
            break
    
    Ci += 1
    
    # Digits to right (go forward)
    Cf = col + 1
    while Cf <= COL_MAX:
        try:
            if inp[row][Cf] in NUMBERS:
                digits.append(inp[row][Cf])
                Cf += 1
            
            else:
                break
        
        except IndexError:
            print(COL_MAX)
            print(row)
            print(Cf)
            quit()
    
    Cf -= 1
    
    number = int("".join(digits))
    
    return number, row, Ci, Cf

# Script that runs for every char in every line
output = []

for row, line in enumerate(inp):
    for col, char in enumerate(line):
        if char is GEAR_SYMBOL:
            gear_adjacents = []

            for r in INCREMENTS:
                if row + r >= 0 and row + r <= ROW_MAX:
                    for c in INCREMENTS:
                        if col + c >= 0 and col + c <= COL_MAX:
                            if inp[row + r][col + c] in NUMBERS:
                                gear_adjacents.append(get_whole_number(row + r, col + c))
            
            # Remove duplicates
            gear_adjacents = list(set(gear_adjacents))

            if len(gear_adjacents) == 2:
                gear_numbers = [x[0] for x in gear_adjacents]
                gear_ratio = gear_numbers[0] * gear_numbers[1]
                
                output.append(gear_ratio)

print(sum(output))
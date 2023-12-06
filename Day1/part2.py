from os import path
from pathlib import Path

NUMS = [str(i) for i in range(10)]
NUM_LETTERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMBERS = NUMS + NUM_LETTERS
TRANSLATOR_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as s:
    text = s.readlines()

validators = []

for line in text:
    positions = []

    for num in NUMBERS:
        if num in line:
            first_pos = last_pos = line.find(num)

            while line.find(num, last_pos + 1) != -1:
                last_pos = line.find(num, last_pos + 1)
            
            positions.append((num, first_pos, last_pos))
    
    # Sorted by the first appearance to get the first digit
    positions = sorted(positions, key=lambda x: x[1])

    if positions[0][0] in NUM_LETTERS:
        first = TRANSLATOR_DICT[positions[0][0]]
    
    else:
        first = positions[0][0]
    
    # Sorted by the last appearance to get the final digit
    positions = sorted(positions, key=lambda x: x[2])
    
    if positions[-1][0] in NUM_LETTERS:
        last = TRANSLATOR_DICT[positions[-1][0]]
    
    else:
        last = positions[-1][0]
    
    validators.append(int(f"{first}{last}"))

print(sum(validators))
from os import path
from pathlib import Path

NUMS = [str(i) for i in range(10)]

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as s:
    text = s.readlines()

validators = []

for line in text:
    for i in range(len(line)):
        if line[i] in NUMS:
            first = line[i]
            break
    
    for i in range(-1, -len(line) - 1, -1):
        if line[i] in NUMS:
            last = line[i]
            break
    
    validators.append(int(f"{first}{last}"))

print(sum(validators))
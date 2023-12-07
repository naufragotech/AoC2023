from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as s:
    inp = s.readlines()

# Clean data
for index, line in enumerate(inp):
    inp[index] = line.replace("\n", "")

# Format the data into two lists of lists (winners and numbers)
winners = []
numbers = []

for card in inp:
    w, n = card[card.find(":") + 1:].split("|")

    w = tuple(filter(lambda x: x != "", w.split(" ")))
    n = tuple(filter(lambda x: x != "", n.split(" ")))

    winners.append(w)
    numbers.append(n)

points = []

# Loop through every index of both lists and count the the matches
for i in range(len(numbers)):
    matches = 0

    for num in numbers[i]:
        if num in winners[i]:
            matches += 1
    
    # For the number in winners of each card, if x > 0 -> 2^(x - 1) else 0
    if matches != 0:
        points.append(pow(2, matches - 1))
    
    else:
        points.append(0)

print(sum(points))

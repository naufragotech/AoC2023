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

matches = []
copies = [1 for _ in range(len(numbers))]

# Loop through every index of both lists and count the the matches
for i in range(len(numbers)):
    match = 0

    for num in numbers[i]:
        if num in winners[i]:
            match += 1
    
    # Add copies of the nexts cards depending on the number of matches
    add = copies[i]

    for x in range(match):
        copies[i + x + 1] += add

print(sum(copies))

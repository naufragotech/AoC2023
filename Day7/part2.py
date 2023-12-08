from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.readlines()

for index, line in enumerate(inp):
    inp[index] = line.replace("\n", "")

# Format data
hands = []

for hand in inp:
    data = hand.split(" ")
    new_hand = {
        "cards": data[0],
        "bid": int(data[1])
    }

    hands.append(new_hand)

# Declare constans
CARDS = ["J"] + [str(i) for i in range(2, 10)] + ["T", "Q", "K", "A"]

TYPES = [
    "High card",
    "One pair",
    "Two pair",
    "Three of a kind",
    "Full house",
    "Four of a kind",
    "Five of a kind",
]

COMBINATIONS = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 2],
    [1, 1, 3, 3, 3],
    [2, 2, 3, 3, 3],
    [1, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]

# Determine the strength of each card in each hand
for hand in hands:
    positions = [CARDS.index(card) for card in hand["cards"]]

    hand.update({"positions": positions})

# Determine the strength of each hand
for hand in hands:
    counts = sorted([hand["cards"].count(card) for card in hand["cards"]])
    strength = COMBINATIONS.index(counts)

    J = hand["cards"].count("J")

    if J != 0:
        if strength == 0:
            strength = 1
        
        elif strength == 1:
            strength = 3
        
        elif strength == 2 and J == 1:
            strength = 4
        
        elif strength == 2 and J == 2:
            strength = 5
        
        elif strength == 3:
            strength = 5
        
        else:
            strength = 6
    
    hand.update({"strength": strength})

# Sort by the strength of hand and then by the positions (strength of cards)
hands = sorted(hands, key=lambda x: (x["strength"], x["positions"]))

total_winnings = 0
rank = 1
for hand in hands:
    total_winnings += (hand["bid"] * rank)

    rank += 1

print(total_winnings)

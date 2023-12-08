from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.read()

inp = list(filter(lambda x: x != "", inp.split("\n")))

instructions = list(map(lambda x: 1 if x == "R" else 0, inp[0]))

network = {}

for node in inp[1:]:
    start = node[:3]
    connections = node[node.find("(") + 1:-1].split(", ")

    network.update({start: connections})

steps = 0
i = 0
curr_node = "AAA"

while curr_node != "ZZZ":
    # Change node according to next instruction
    curr_node = network[curr_node][instructions[i]]

    steps += 1
    i += 1

    if i == len(instructions):
        i = 0

print(steps)

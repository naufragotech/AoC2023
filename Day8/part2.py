from os import path
from pathlib import Path
from math import lcm

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


nodes_A = [node for node in network.keys() if node[-1] == "A"]
steps_arr = []

for node in nodes_A:
    curr_node = node
    steps = 0
    i = 0

    while curr_node[-1] != "Z":
        curr_node = network[curr_node][instructions[i]]

        steps += 1
        i += 1

        if i == len(instructions):
            i = 0
    
    steps_arr.append(steps)


print(lcm(*steps_arr))
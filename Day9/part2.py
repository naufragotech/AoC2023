from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.readlines()

output = 0

for line in inp:
    sequence = [[int(x) for x in line.split(" ")[::-1]]]
    n = 0

    all_zeros = False

    while not all_zeros:
        prev = sequence[n]
        seq = [prev[i + 1] - prev[i] for i in range(len(prev[:-1]))]
        sequence.append(seq)

        zero_array = [0 for _ in range(len(seq))]

        if seq == zero_array:
            all_zeros = True
        
        else:
            n += 1

    for n in range(len(sequence) - 1).__reversed__():
        sequence[n].append(sequence[n + 1][-1] + sequence[n][-1])

    output += sequence[0][-1]

print(output)
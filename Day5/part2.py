from os import path
from pathlib import Path
from math import inf

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.read()

# Test Data (complete execution takes about 4 hours)
# inp = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

inp = inp.split("\n\n")

def construct_map(data):
    output = list(filter(lambda x: x != "", data[data.find(":") + 1:].split("\n")))
    output = [tuple([int(x) for x in rng.split(" ")]) for rng in output]

    return output

seed_to_soil = construct_map(inp[1])
soil_to_fertilizer = construct_map(inp[2])
fertilizer_to_water = construct_map(inp[3])
water_to_light = construct_map(inp[4])
light_to_temperature = construct_map(inp[5])
temperature_to_humidity = construct_map(inp[6])
humidity_to_location = construct_map(inp[7])

seeds_rng = filter(lambda x: x != "", inp[0][inp[0].find(":") + 1:].split(" "))
seeds_rng = [int(s) for s in seeds_rng]

min_location = inf

def compute_destination(x, whole_map):
    for rng in whole_map:
        if rng[1] <= x < (rng[1] + rng[2]):
            distance = x - rng[1]
            return rng[0] + distance
    
    else:
        return x

for i in range(0, len(seeds_rng), 2):

    for x in range(seeds_rng[i + 1]):
        seed = seeds_rng[i] + x

        # 1 Match seed to soil
        soil = compute_destination(seed, seed_to_soil)

        # 2 Match soil to fertilizer
        fertilizer = compute_destination(soil, soil_to_fertilizer)

        # 3 Match fertilizer to water
        water = compute_destination(fertilizer, fertilizer_to_water)

        # 4 Match water to light
        light = compute_destination(water, water_to_light)

        # 5 Match light to temperature
        temperature = compute_destination(light, light_to_temperature)
        
        # 6 Match temperature to humidity
        humidity = compute_destination(temperature, temperature_to_humidity)
        
        # 7 Match humidity to location
        location = compute_destination(humidity, humidity_to_location)
    
        # Determine if its minimum
        min_location = location if location < min_location else min_location

print(min_location)

from os import path
from pathlib import Path

PATH = path.join(Path(__file__).parent.resolve(), "input.txt")

with open(PATH, "rt") as stream:
    inp = stream.read()

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

seeds = filter(lambda x: x != "", inp[0][inp[0].find(":") + 1:].split(" "))
seeds = [int(s) for s in seeds]

locations = []

def compute_destination(x, whole_map):
    for rng in whole_map:
        if rng[1] <= x < (rng[1] + rng[2]):
            distance = x - rng[1]
            return rng[0] + distance
    
    else:
        return x

for seed in seeds:
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
    locations.append(location)
    
print(min(locations))

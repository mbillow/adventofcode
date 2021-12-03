# Advent of Code Day 2 - Prompt 1
# Marc Billow

import operator
from functools import partial

with open("input.txt") as f:
    lines = f.readlines()

depth = 0
distance = 0

# Honestly, the trickiest part here is going to be keeping the inverted
# up/down <-> plus/minus relationships straight. I am just going to knock
# that out in a name to operation dictionary.

depth_operations = {
    "down": operator.__add__,
    "up": operator.__sub__,
}

distance_operations = {
    "forward": operator.__add__,
}

for line in lines:
    curr = line.strip().split(" ")

    # If the current command is meant to adjust depth...
    if curr[0] in depth_operations.keys():
        depth = depth_operations[curr[0]](depth, int(curr[1]))
    
    # Otherwise, it is probably propelling us forward.
    elif curr[0] in distance_operations.keys():
        distance = distance_operations[curr[0]](distance, int(curr[1]))

print(depth * distance)


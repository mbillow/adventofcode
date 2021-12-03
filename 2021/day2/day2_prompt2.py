# Advent of Code Day 2 - Prompt 2
# Marc Billow

import operator

with open("input.txt") as f:
    lines = f.readlines()

aim = 0
depth = 0
distance = 0

# Honestly, the trickiest part here is going to be keeping the inverted
# up/down <-> plus/minus relationships straight. I am just going to knock
# that out in a name to operation dictionary.

aim_operations = {
    "down": operator.__add__,
    "up": operator.__sub__,
}

distance_operations = {
    "forward": operator.__add__,
}

for line in lines:
    curr = line.strip().split(" ")
    
    # If the current command is meant to adjust aim...
    if curr[0] in aim_operations.keys():
        operation = aim_operations[curr[0]]
        aim = operation(aim, int(curr[1]))
    
    # Otherwise, we are probably read to move...
    elif curr[0] in distance_operations.keys():
        operation = distance_operations[curr[0]]
        distance = operation(distance, int(curr[1]))
        depth = depth + (aim * int(curr[1]))


print(depth * distance)


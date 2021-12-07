# Advent of Code Day 6 - Prompt 1
# Marc Billow

with open("input.txt") as f:
    lines = f.readlines()

fish = [int(x) for x in lines[0].strip().split(",")]

for _ in range(80):
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            fish.append(9)
        else:
            fish[i] -= 1

print(len(fish))

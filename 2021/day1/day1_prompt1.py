# Advent of Code Day 1 - Prompt 1
# Marc Billow

with open("input.txt") as f:
    lines = f.readlines()

prev = None
total = 0
for line in lines:
    curr = int(line.strip())
    if prev is not None and curr > prev:
        total += 1
    prev = curr

print(total)

# Advent of Code Day 7 - Prompt 1
# Marc Billow

from statistics import median

with open("input.txt") as f:
    lines = f.readlines()

positions = [int(x) for x in lines[0].strip().split(",")]
median_pos = median(positions)
print(f"Median: {median_pos}")

fuel = sum([abs(x-median_pos) for x in positions])

print(f"Total Fuel: {fuel}")


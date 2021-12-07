# Advent of Code Day 7 - Prompt 2
# Marc Billow

from statistics import mean
from math import floor

with open("input.txt") as f:
    lines = f.readlines()

positions = [int(x) for x in lines[0].strip().split(",")]
mean_pos = floor(mean(positions))
print(f"Mean: {mean_pos}")

fuel = sum([sum(range((abs(x-mean_pos)+1))) for x in positions])

print(f"Total Fuel: {fuel}")

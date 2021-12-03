# Advent of Code Day 1 - Prompt 2
# Marc Billow

with open("input.txt") as f:
    lines = f.readlines()

total = 0
sliding_window = [int(l.strip()) for l in lines[:3]]
prev = sum(sliding_window)

for line in lines:
    curr = int(line.strip())

    # We need to pop the first value to maintain a three value sliding window.
    popped = sliding_window.pop(0)
    
    # Now that we have room, add our current value.
    sliding_window.append(curr)

    curr_sum = sum(sliding_window)
    if curr_sum > prev:
        total += 1
    prev = curr_sum


print(total)

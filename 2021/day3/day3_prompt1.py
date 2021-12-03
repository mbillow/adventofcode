# Advent of Code Day 3 - Prompt 1
# Marc Billow

with open("input.txt") as f:
    lines = f.readlines()

# We'll need the length to easily determine most/least common bits.
diag_length = len(lines)
# Initialize the sum list with the first line.
index_sums = [int(x) for x in lines[0].strip()]

# For every other line, split the binary string and add up the bits.
for line in lines[1:]:
    curr = line.strip()
    for index, bval in enumerate(curr):
        index_sums[index] = index_sums[index] + int(bval)

# Calculate the most and least common bits in each index.
gamma = [1 if x >= diag_length/2 else 0 for x in index_sums]
epsil = [0 if x >= diag_length/2 else 1 for x in index_sums]

# Convert integer bit arrays to decimal integers.
# XXX: Honestly not sure if there is a better way to do this.
gamma_int = int("".join(str(x) for x in gamma), 2)
epsil_int = int("".join(str(x) for x in epsil), 2)

print(gamma_int * epsil_int)

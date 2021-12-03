# Advent of Code Day 3 - Prompt 2
# Marc Billow


with open("input.txt") as f:
    lines = f.readlines()


# Because we are filtering the list for each calculation, lets do it
# recursively.
# Filter bit here is 1 for most common and 0 for least common.
def rating_filter(values: list, filter_bit: int, index: int = 0) -> str:
    # Initialize the sum list with the first line.
    index_sums = [int(x) for x in values[0].strip()]

    # For every other line, split the binary string and add up the bits.
    for line in values[1:]:
        curr = line.strip()
        for bidx, bval in enumerate(curr):
            index_sums[bidx] = index_sums[bidx] + int(bval)

    filter_list = [
        filter_bit
        if x >= len(values) / 2
        # Use XOR to flip bits for our else condition.
        else filter_bit ^ 1
        for x in index_sums
    ]
    filtered_values = [
        x.strip()
        for x in values
        if x[index] == str(filter_list[index])
    ]

    # If our filtered list has more than one value, recurse deeper.
    if len(filtered_values) > 1:
        return rating_filter(filtered_values, filter_bit, index + 1)

    # Return the filtered value.
    return int("".join(filtered_values[0]), 2)


oxygen = rating_filter(lines, 1)
co2 = rating_filter(lines, 0)

print(oxygen * co2)

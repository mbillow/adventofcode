# Advent of Code Day 5 - Prompt 1
# Marc Billow

with open("input.txt") as f:
    lines = f.readlines()

vent_map_line = [0] * 1000
vent_map = []
for i in range(1000):
    vent_map.append(list(vent_map_line))

vents = [x.strip().split(" -> ") for x in lines]
total_intersections = 0

for vent in vents:
    start = vent[0].split(",")
    end = vent[1].split(",")

    # Vertical Lines
    if start[0] == end[0]:
        start_y = int(start[1])
        end_y = int(end[1])
        if start_y > end_y:
            start_y, end_y = end_y, start_y
        for i in range(start_y, end_y + 1):
            if vent_map[i][int(start[0])] == 1:
                total_intersections += 1
            vent_map[i][int(start[0])] += 1

    # Horizontal Lines
    elif start[1] == end[1]:
        start_x = int(start[0])
        end_x = int(end[0])
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        for i in range(start_x, end_x + 1):
            if vent_map[int(start[1])][i] == 1:
                total_intersections += 1
            vent_map[int(start[1])][i] += 1

    else:
        print(start, end)
        start_x = int(start[0])
        end_x = int(end[0])
        start_y = int(start[1])
        end_y = int(end[1])
        ys = range(start_y, end_y + 1)
        xs = range(start_x, end_x + 1)
        if start_x > end_x:
            xs = range(start_x, end_x - 1, -1)
        if start_y > end_y:
            ys = range(start_y, end_y - 1, -1)
        print(list(xs), list(ys))
        for i, x in enumerate(xs):
            print(x, ys[i])
            if vent_map[ys[i]][x] == 1:
                total_intersections += 1
            vent_map[ys[i]][x] += 1

for row in vent_map:
    print(" ".join([str(x) if x != 0 else "." for x in row]))

print(total_intersections)

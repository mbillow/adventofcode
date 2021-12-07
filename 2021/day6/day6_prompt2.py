# Advent of Code Day 6 - Prompt 2
# Marc Billow

from concurrent.futures import ProcessPoolExecutor, as_completed

with open("input.txt") as f:
    lines = f.readlines()

all_fish = [int(x) for x in lines[0].strip().split(",")]
unique_ages = set(all_fish)
age_counts = {x: all_fish.count(x) for x in unique_ages}


def calculate_fish_in_days(fish: list, days: int = 256) -> tuple:
    initial_age = fish[0]
    # TODO: We could save a _boat load_ of time by batching days into weeks.
    for _ in range(days):
        print(initial_age, _)
        for i, fi in enumerate(fish):
            if fi == 0:
                fish[i] = 6
                fish.append(9)
            else:
                fish[i] -= 1

    return initial_age, len(fish)


if __name__ == '__main__':
    workers = 15
    with ProcessPoolExecutor(max_workers=workers) as executor:
        total = 0
        children = [executor.submit(calculate_fish_in_days, [age], 256) for age in unique_ages]
        for future in as_completed(children):
            age, age_total = future.result()
            total += age_counts[age] * age_total
        print(total)

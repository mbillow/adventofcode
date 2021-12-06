# Advent of Code Day 4 - Prompt 1
# Marc Billow

import re

BINGO = [True] * 5

with open("input.txt") as f:
    lines = f.readlines()

drawn_numbers = [int(x) for x in lines[0].strip().split(",")]

# Board Storage
# boards = [
#     [
#         [(22, False), (13, False), (17, False), (11, False), ( 0, False)]
#         [(21, False), ( 9, False), (14, False), (16, False), ( 7, False)]
#         [( 8, False), ( 2, False), (23, False), ( 4, False), (24, False)]
#         [(22, False), (13, False), (17, False), (11, False), ( 0, False)]
#         [( 1, False), (12, False), (20, False), (15, False), (19, False)]
#     ],
#     ...
# ]

boards = []

curr_board = []
for line in lines[2:]:
    line = line.strip()
    if line != "":
        curr_board.append(
            [(int(x), False) for x in re.split(" +", line)]
        )
    else:
        boards.append(curr_board)
        curr_board = []

for number in drawn_numbers:
    print(f"Calling drawn number: {number}")
    for board_number, board in enumerate(boards):
        for row_number, row in enumerate(board):
            for column_number, column in enumerate(row):
                if column[0] == number:
                    print(f"  - [MATCH] Board {board_number} [Row: {row_number}, Column: {column_number}]")
                    boards[board_number][row_number][column_number] = (number, True)
                    # Check for a winner.
                    horizontal = [x[1] for x in row]
                    vertical = [x[1] for x in [r[column_number] for r in board]]
                    if horizontal == BINGO or vertical == BINGO:
                        print(f"[WIN] Board {board_number}")
                        unmarked_sum = 0
                        for r in board:
                            print(f"  {r}")
                            for c in r:
                                if not c[1]:
                                    unmarked_sum += c[0]
                        print(f"Final Winning Score: {unmarked_sum * number}")
                        exit()


for board_number, board in enumerate(boards):
    print(f"\n Board {board_number}")
    for row in board:
        print(f"  {row}")


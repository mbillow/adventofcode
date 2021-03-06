# Advent of Code Day 4 - Prompt 2
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
winning_boards = []

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
last_winner = -1
for number in drawn_numbers:
    print(f"Calling drawn number: {number}")
    for board_number, board in enumerate(boards):
        if board_number in winning_boards:
            continue
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
                        winning_boards.append(board_number)
                        if len(winning_boards) == (len(boards) - 1):
                            last_winner = list(set(range(len(boards))) - set(winning_boards))[0]
                            print(f"Found the last winner: {last_winner}")
                        if len(winning_boards) == len(boards):
                            unmarked_sum = 0
                            for r in boards[last_winner]:
                                print(f"  {r}")
                                for c in r:
                                    if not c[1]:
                                        unmarked_sum += c[0]
                            print(f"Final Winning Score: {unmarked_sum * number}")
                            exit()



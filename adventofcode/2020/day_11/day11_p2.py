import sys
import copy
from functools import reduce


def is_out_range(board, i, j):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])


def first_index_seat(board, i, j, i_mod, j_mod):
    if is_out_range(board, i, j): return [i, j]

    while(board[i][j] == "."):
        i += i_mod
        j += j_mod

        if is_out_range(board, i, j): break

    return [i, j]


def occupied_direction_seats(board, i, j):
    count = 0

    new_i, new_j = first_index_seat(board, i-1, j-1, -1, -1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i-1, j, -1, 0)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i-1, j+1, -1, 1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i, j-1, 0, -1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i, j+1, 0, 1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i+1, j-1, 1, -1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i+1, j, 1, 0)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    new_i, new_j = first_index_seat(board, i+1, j+1, 1, 1)
    if not is_out_range(board, new_i, new_j) and board[new_i][new_j] == "#": count += 1

    return count


def simulate_round(board):
    next_board = copy.deepcopy(board)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] != ".":
                occupied_seats = occupied_direction_seats(board, i, j)

                seat = next_board[i][j]
                if occupied_seats == 0:
                    seat = "#"
                elif occupied_seats >= 5:
                    seat = "L"

                next_board[i][j] = seat

    return next_board


def main():
    board = []
    for line in sys.stdin:
        board.append(list(line.rstrip()))

    while True:
        next_board = simulate_round(board)
        if board == next_board: break
        board = copy.deepcopy(next_board)

    print(reduce(lambda x, y: x+y.count("#"), board, 0))


if __name__ == "__main__":
    main()

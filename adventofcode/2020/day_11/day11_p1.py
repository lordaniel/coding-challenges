import sys
import copy
from functools import reduce

def occupied_adjacent_seats(board, i, j):
    count = 0

    if i > 0 and j > 0 and board[i-1][j-1] == "#": count += 1
    if i > 0 and board[i-1][j] == "#": count += 1
    if i > 0 and j < len(board[0])-1 and board[i-1][j+1] == "#": count += 1
    if j > 0 and board[i][j-1] == "#": count += 1
    if j < len(board[0])-1 and board[i][j+1] == "#": count += 1
    if i < len(board)-1 and j > 0 and board[i+1][j-1] == "#": count += 1
    if i < len(board)-1 and board[i+1][j] == "#": count += 1
    if i < len(board)-1 and j < len(board[0])-1 and board[i+1][j+1] == "#": count += 1

    return count


def simulate_round(board):
    next_board = copy.deepcopy(board)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] != ".":
                occupied_seats = occupied_adjacent_seats(board, i, j)

                seat = next_board[i][j]
                if occupied_seats == 0:
                    seat = "#"
                elif occupied_seats >= 4:
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

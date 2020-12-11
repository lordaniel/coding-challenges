import sys
from functools import reduce

def calc_trees(board, right, down):
    width = len(board[0])
    trees = 0
    col = right
    row = down

    while row < len(board):
        if board[row][col] == "#":
            trees += 1
        row += down
        col = (col + right) % width

    return trees

def main():
    board = []
    for line in sys.stdin:
        board.append(line.rstrip())

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    slopes = list(map(lambda x: calc_trees(board, x[0], x[1]), slopes))
    total = reduce(lambda x, y: x * y, slopes)

    print(total)

if __name__ == "__main__":
    main()

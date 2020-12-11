import sys

def main():
    board = []
    for line in sys.stdin:
        board.append(line.rstrip())

    row , col, trees = 1, 3, 0
    width = len(board[0])

    while row < len(board):
        if board[row][col] == "#":
            trees += 1
        row += 1
        col = (col + 3) % width

    print(trees)

if __name__ == "__main__":
    main()

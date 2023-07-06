#!/usr/bin/python3
"""A file for dealing with N-queens puzzle game.
A game of determining all possible result for placing N non-attacking queens

For Example: ./101-nqueens.py N
where `N` must be an integer which is greater than or equal to 4.

Attributes:
    board (list): is a list of lists representing a chessboard.
    result (list): is a list of lists containings solutions of a game

result is represented in format like this [[r, c], [r, c], [r, c], [r, c]]
Where `r` for represanting row and `c` for representing column.
"""

import sys


def init_board(n):
    """A function to initialize size of chessboard with 0's by `n`x`n`."""
    board = []
    [board.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in board]

    return (board)


def board_copy(board):
    """A function to return a copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_copy, board))

    return (board)


def get_result(board):
    """Retuns lists of solved chessboard."""
    result = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                result.append([r, c])
                break

    return (result)


def queen_xout(board, row, column):
    """A function to Xout of spots on a chessboard. All spots where
    non-attacking queens and can no longer be played are X-ed out.

    Args:
        board (list): is a current working chessboard.
        row (int): is the row where queen was played last.
        column (int): is the row where queen was played last.
    """

    # Xout to all forward spots of chessboard
    for c in range(column + 1, len(board)):
        board[row][c] = "x"

    # Xout to all backwards spots of chessboard
    for c in range(column - 1, -1, -1):
        board[row][c] = "x"

    # Xout to all spots below of chessboard
    for r in range(row + 1, len(board)):
        board[r][column] = "x"

    # Xout to all spots above of chessboard
    for r in range(row - 1, -1, -1):
        board[r][column] = "x"

    # Xout to all spots diagonally down to the right of chessboard
    c = column + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # Xout to all spots diagonally up to the left of chessboard
    c = column - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    # Xout to all spots diagonally up to the right of chessboard
    c = column + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # Xout to all spots diagonally down to the left
    c = column - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve(board, row, queens, result):
    """A functon for solving N-queens puzzle game

    Args:
        board (list): is current working chessboard.
        row (int): is current working row.
        queens (int): is a current value of a placed queens.
        result (list): is a list of list of results.

    Return:
        result as final resulting of a game
    """
    if queens == len(board):
        result.append(get_result(board))
        return (result)

    for i in range(len(board)):
        if board[row][i] == " ":
            temp_board = board_copy(board)
            temp_board[row][i] = "Q"
            queen_xout(temp_board, row, i)
            result = solve(temp_board, row + 1, queens + 1, result)

    return (result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    result = solve(board, 0, 0, [])
    for res in result:
        print(res)

#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def is_safe(board, row, col, N):
    """
    Check this row on the left side
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """
    Check upper diagonal on left side
    """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """
    Check lower diagonal on left side
    """
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    """
    utils to solve
    """
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def solve_nqueens(N):
    """
    Solution to nqueens problem
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("No solution exists")
        sys.exit(1)

    for row in board:
        print(row)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])

#!/usr/bin/python3
"""Module for N queens problem."""
import sys


def create_board(n):
    """Create an n x n board initialized with zeros."""
    board = [[0] * n for _ in range(n)]
    return board


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board at [row][col]."""
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve(board, col, n):
    """Use backtracking to solve the N queens problem."""
    if col == n:
        print_solution(board, n)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def print_solution(board, n):
    """Print the solution as a list of lists."""
    queens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(n)
    solve(board, 0, n)

#!/usr/bin/python3
"""Module for N queens problem."""

import sys


class NQueens:
    """Class to solve the N queens problem."""

    def __init__(self, n):
        """Initialize the board."""
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]

    def is_safe(self, row, col):
        """Check if it's safe to place a queen at board[row][col]."""
        for i in range(col):
            if self.board[row][i]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        return True

    def solve_nqueens(self, col):
        """Use backtracking to solve the N queens problem."""
        if col == self.n:
            self.print_solution()
            return True
        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_nqueens(col + 1) or res
                self.board[i][col] = 0
        return res

    def print_solution(self):
        """Print the board."""
        queens = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
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

    nqueens = NQueens(n)
    nqueens.solve_nqueens(0)

#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """Computes the square value of all integers of a matrix using map.

    Args:
        matrix (list): The matrix to square.

    Returns:
        list: The squared matrix."""
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))

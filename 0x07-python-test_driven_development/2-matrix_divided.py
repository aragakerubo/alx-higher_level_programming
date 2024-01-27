#!/usr/bin/python3

"""This module contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with the results of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]

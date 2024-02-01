#!/usr/bin/python3

"""
Module to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.

    Returns:
        list: A new matrix with the results of the multiplication.

    Raises:
        TypeError: If m_a is not a list of lists of integers/floats.
        TypeError: If m_b is not a list of lists of integers/floats.
        TypeError: If rows of m_a are not the same size.
        TypeError: If rows of m_b are not the same size.
        TypeError: If m_a or m_b are empty lists.
        TypeError: If m_a or m_b contain elements that are not integers/floats.
        ValueError: If m_a or m_b are not 2D matrices.
        ValueError: If m_a or m_b cannot be multiplied.
    """
    if not isinstance(m_a, list) or m_a == []:
        raise TypeError("m_a must be a list of lists" " of integers/floats")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists" " of integers/floats")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a must be a list of lists" " of integers/floats")
    if not isinstance(m_b, list) or m_b == []:
        raise TypeError("m_b must be a list of lists" " of integers/floats")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists" " of integers/floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b must be a list of lists" " of integers/floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("m_a must be a matrix")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("m_b must be a matrix")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]

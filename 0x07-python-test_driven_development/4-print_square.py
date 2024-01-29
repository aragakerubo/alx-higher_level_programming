#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is a float and is less than 0.
        TypeError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        print("#" * size)

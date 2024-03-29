#!/usr/bin/python3

"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

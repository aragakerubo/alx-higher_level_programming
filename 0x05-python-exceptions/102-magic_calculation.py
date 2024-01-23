#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Function that emulates the bytecode of a Python function.

    Args:
        a (int): The first value.
        b (int): The second value.

    Returns:
        int: The result of the calculation.
    """
    result = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception("Too far")
            else:
                result += a**b / item
        except Exception:
            result = b + a
            break

    return result

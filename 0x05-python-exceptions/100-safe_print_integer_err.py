#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Function that prints an integer.

    Args:
        value (int): The value to be printed.

    Returns:
        bool: True if value was printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False

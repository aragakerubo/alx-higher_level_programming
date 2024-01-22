#!/usr/bin/python3


def safe_print_integer(value):
    """
    Function that prints an integer with "{:d}".format().

    Args:
        value (int): The value to be printed.

    Returns:
        bool: True if value was printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False

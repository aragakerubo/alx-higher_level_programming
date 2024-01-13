#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number.

    Args:
        my_list (list): The list to multiply.
        number (int): The number to multiply by.

    Returns:
        list: The new list."""
    return list(map(lambda x: x * number, my_list))

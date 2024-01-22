#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Function that prints the first x elements of a list.

    Args:
        my_list (list): The list to be printed.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements printed.
    """
    try:
        for index in range(x):
            print(my_list[index], end="")
        print()
        return x
    except IndexError:
        print()
        return index

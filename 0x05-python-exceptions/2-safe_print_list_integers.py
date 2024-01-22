#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Function that prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list to be printed.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements printed.
    """
    count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

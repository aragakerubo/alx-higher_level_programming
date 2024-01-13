#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns the weighted average of all integers in a list of tuples.

    Args:
        my_list (list): The list of tuples to average.

    Returns:
        float: The weighted average."""
    if not my_list:
        return 0
    return sum([x * y for x, y in my_list]) / sum([y for x, y in my_list])

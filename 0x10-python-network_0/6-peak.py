#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of unsorted integers

    Returns:
        int: Peak of the list
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid = len(list_of_integers) // 2
    if (
        list_of_integers[mid] > list_of_integers[mid - 1]
        and list_of_integers[mid] > list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1 :])
    return find_peak(list_of_integers[:mid])

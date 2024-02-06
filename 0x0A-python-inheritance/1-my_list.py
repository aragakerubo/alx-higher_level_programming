#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """
    Class that inherits from list
    Args:
        list (list): list to inherit

    Methods:
        print_sorted: prints the list sorted
    """

    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))

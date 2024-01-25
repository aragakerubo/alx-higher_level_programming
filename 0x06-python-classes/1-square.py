#!/usr/bin/python3

"""This module contains a class that defines a square."""


class Square:
    """This class contains a private attribute that defines a square."""

    def __init__(self, size):
        """Initializes private attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

#!/usr/bin/python3

"""This module contains a class that defines a square."""


class Square:
    """This class contains a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    def __eq__(self, other):
        """Returns True if the square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns True if the square is not equal to another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Returns True if the square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns True if the square is greater/equal to another square."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Returns True if the square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Returns True if the square is less/equal to another square."""
        return self.area() <= other.area()

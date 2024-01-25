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

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        string = ""
        if self.__size == 0:
            return string
        for i in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            string += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                string += "\n"
        return string

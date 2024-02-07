#!/usr/bin/python3
"""Module for Square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class that defines a square"""

    def __init__(self, size):
        """
        Initializes a new Square.
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square
        Returns:
            str: representation of the Square
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

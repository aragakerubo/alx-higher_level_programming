#!/usr/bin/python3
"""
Module that defines a rectangle.
"""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ method that sets the intial state of the object
        and checks for any exception errors.
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """__del__ method that prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Property for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.
        Args:
            value (int): width value to set the rectangle to.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.
        Args:
            value (int): height value to set the rectangle to.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__ method that returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width] * self.__height
        )

    def __repr__(self):
        """__repr__ method that returns the string representation of the rectangle
        for reproduction.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

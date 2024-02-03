#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """A rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message for every deletion of a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Print the rectangle with the character #."""
        if self.width == 0 or self.height == 0:
            return ""
        return (
            (str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """Property to retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Public method that returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest
        rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle
        instance with width == height == size."""
        return cls(size, size)

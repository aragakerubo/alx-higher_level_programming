#!/usr/bin/python3
"""Module for Rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        Returns:
            str: representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

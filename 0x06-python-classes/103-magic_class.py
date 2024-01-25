#!/usr/bin/python3

"""This module contains a class that defines a magic class."""

import math


class MagicClass:

    """This class contains a magic class."""

    def __init__(self, radius=0):
        """Initializes the magic class.

        Args:
            radius (int): The radius of the magic class.
        """
        self.radius = radius

    @property
    def radius(self):
        """int: The radius of the magic class."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Returns the area of the magic class."""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Returns the circumference of the magic class."""
        return 2 * math.pi * self.__radius

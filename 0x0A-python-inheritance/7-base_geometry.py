#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Class that defines a base geometry"""

    def area(self):
        """
        Raises an exception when called
        Raises:
            Exception: always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value
        Args:
            name (str): name of the value
            value (int): value to validate
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

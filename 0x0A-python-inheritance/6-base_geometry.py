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

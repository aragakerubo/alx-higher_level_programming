#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Class that defines a MyInt"""

    def __eq__(self, other):
        """Returns the opposite of the equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns the opposite of the inequality"""
        return super().__eq__(other)

#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible
    Args:
        obj (object): object to add the attribute to
        name (str): name of the attribute
        value (any): value of the attribute
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

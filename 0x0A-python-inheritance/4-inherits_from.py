#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited from
    the specified class; otherwise False.
    Args:
        obj (object): object to check
        a_class (class): class to check
    Returns:
        bool: True if the object is an instance of a class that inherited from
        the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

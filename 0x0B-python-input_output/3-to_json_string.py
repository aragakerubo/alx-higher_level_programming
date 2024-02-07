#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: The object to be represented as a JSON string.

    Returns:
        The JSON representation of the object.
    """
    return json.dumps(my_obj)

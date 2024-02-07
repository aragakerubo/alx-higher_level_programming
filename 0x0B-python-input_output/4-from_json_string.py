#!/usr/bin/python3
"""Module for from_json_string"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be represented as an object.

    Returns:
        The object represented by the JSON string.
    """
    return json.loads(my_str)

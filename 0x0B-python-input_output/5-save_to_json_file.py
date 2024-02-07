#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to be represented as a JSON string.
        filename: The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))

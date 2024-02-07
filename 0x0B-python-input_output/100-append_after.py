#!/usr/bin/python3
"""Module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string after a specific string in a text file

    Args:
        filename (str): The file to append the string to
        search_string (str): The string to search for
        new_string (str): The string to append
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

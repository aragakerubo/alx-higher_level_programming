#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added

    Args:
        filename: The name of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)

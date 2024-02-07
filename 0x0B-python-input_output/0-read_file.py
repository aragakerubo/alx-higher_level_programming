#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """
    Read a text file and print it to stdout.

    Args:
        filename: The name of the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

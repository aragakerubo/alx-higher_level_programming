#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print("\n".join([line.strip() for line in text.split("\n")]), end="")

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (any): The key to replace or add.
        value (any): The value to replace or add.

    Returns:
        dict: The updated dictionary."""
    a_dictionary[key] = value
    return a_dictionary

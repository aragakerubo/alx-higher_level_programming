#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete from.
        value (any): The value to delete.

    Returns:
        dict: The updated dictionary."""
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

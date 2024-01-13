#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): The dictionary to search.

    Returns:
        any: The key with the biggest integer value, or None if empty."""
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None

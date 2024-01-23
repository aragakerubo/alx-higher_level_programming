#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Function that executes a function safely.

    Args:
        fct (function): The function to be executed.
        args (list): The arguments to be passed to the function.

    Returns:
        Any: The result of the function, or None if an exception occurred.
    """
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None

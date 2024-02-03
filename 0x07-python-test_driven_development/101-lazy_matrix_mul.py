#!/usr/bin/python3
"""
Module that multiplies 2 matrices by using the module NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.

    Returns:
        list: A new matrix with the results of the multiplication.
    """
    return np.matmul(m_a, m_b)

#!/usr/bin/python3
"""
Module that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    Args:
        a: integer or float
        b: integer or float
    Returns:
        The addition of a and b
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in [int, float]:

        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(float(a) + float(b))

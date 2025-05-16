#!/usr/bin/python3

"""Module that provides a function to add two integers."""


def add_integer(a, b=98):
    """Returns the sum of a and b as integers.
    Floats are cast to ints. Raises TypeError if inputs are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

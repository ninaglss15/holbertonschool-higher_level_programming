#!/usr/bin/python3

"""Module that provides a function to add two integers."""


def add_integer(a, b=98):
    """
    that adds 2 integer, transform float in to integer and handle wrong type
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""
This module defines a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj.__class__ is a_class, False otherwise.
    """

    return obj.__class__ is a_class

#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class or a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class
    or of a class that inherited from it; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or a subclass.
    """

    return isinstance(obj, a_class)

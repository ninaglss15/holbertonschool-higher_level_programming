#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class that inherited (directly or indirectly)
from the specified class, but is not exactly an instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    from a_class, but not if it is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj inherits from a_class, False otherwise.
    """

    if isinstance(obj, a_class) and obj.__class__ is not a_class:
        return True
    else:
        return False

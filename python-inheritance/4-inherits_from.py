#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class that inherited (directly or indirectly)
from the specified class, but is not exactly an instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False

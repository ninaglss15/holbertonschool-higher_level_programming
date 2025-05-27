#!/usr/bin/python3

"""Module that defines the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,\
        or inherited instance of, a_class.

    Args:
        obj: The object to check.
        a_class: The class or superclass to compare against.

    Returns:
        True if obj is an instance or inherited instance of a_class,\
            otherwise False.
    """

    return isinstance(obj, a_class)

#!/usr/bin/python3
"""This module defines a function to return available."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods will be listed.

    Returns:
        list: A list of strings containing the attributes and methods.
    """
    return dir(obj)

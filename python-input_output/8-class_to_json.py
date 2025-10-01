#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""


def class_to_json(obj):
    """Return the dictionary representation of a class instance."""
    return obj.__dict__

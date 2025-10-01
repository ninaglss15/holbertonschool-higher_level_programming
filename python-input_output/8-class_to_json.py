#!/usr/bin/python3


def class_to_json(obj):
    """Return the dictionary representation of a class instance."""
    return obj.__dict__

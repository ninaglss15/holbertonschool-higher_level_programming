#!/usr/bin/python3
""" Function that returns a dictionary description of a class instance """


def class_to_json(obj):
    """Returns the dictionary description for
    JSON serialization of an object"""
    return obj.__dict__

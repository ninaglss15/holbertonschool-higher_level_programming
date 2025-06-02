#!/usr/bin/python3
import json
"""
This module defines a function that returns the JSON\
    representation of an object.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object (string format).
    """
    json_string = json.dumps(my_obj)
    return json_string

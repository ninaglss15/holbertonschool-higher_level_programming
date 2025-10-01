#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)

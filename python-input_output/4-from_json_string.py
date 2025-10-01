#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)

#!/usr/bin/python3
"""
This module defines a function that returns a Python object from a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns a Python object (data structure) represented by a JSON string.
    """
    json_string = json.loads(my_str)
    return json_string

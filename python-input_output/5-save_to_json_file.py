#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a file in JSON format (UTF-8)."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""
This module defines a function that writes an object\
    to a text file in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as fichier:
        json.dump(my_obj, fichier)

#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""


def write_file(filename="", text=""):
    """Write text to a file (UTF-8) and return the number."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

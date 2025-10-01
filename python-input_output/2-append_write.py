#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""


def append_write(filename="", text=""):
    """Append text to a file (UTF-8) and return number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

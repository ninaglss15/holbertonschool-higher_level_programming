#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write text to a file (UTF-8) and return the number."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

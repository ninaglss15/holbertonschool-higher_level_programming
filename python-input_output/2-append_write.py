#!/usr/bin/python3


def append_write(filename="", text=""):
    """Append text to a file (UTF-8) and return number of characters written."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3


def read_file(filename=""):
    """
    Read a text file (UTF-8) and print its content to stdout.

    This function opens the specified file in read mode using UTF-8
    encoding, reads its entire content, and prints it to the standard
    output without adding an extra newline at the end.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")

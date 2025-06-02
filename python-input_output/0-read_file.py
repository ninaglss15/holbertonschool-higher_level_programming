#!/usr/bin/python3
"""
This module defines a function that reads a text file and prints its content.
"""


def read_file(filename="my_file_0.txt"):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """
    with open(filename, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")

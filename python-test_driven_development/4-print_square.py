#!/usr/bin/python3
"""Function that prints a square using the '#' character.
Validates that the input size is a positive integer.
Raises a TypeError if the size is not an integer.
Raises a ValueError if the size is negative.
Does not use any imported modules."""


def print_square(size):
    """Prints a square made of '#' characters.
Validates that size is a positive integer.
Raises TypeError or ValueError depending on input."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

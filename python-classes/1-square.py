#!/usr/bin/python3
"""Module that defines a Square class with private size attribute."""


class Square:
    """Class that defines a square with a private size attribute."""
    def __init__(self, size):
        """Initializes a new Square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

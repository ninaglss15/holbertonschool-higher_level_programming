#!/usr/bin/python3


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            # If size is not an integer, raise an error
            raise TypeError("size must be an integer")

        if size < 0:
            # If size is negative, raise an error
            raise ValueError("size must be >= 0")

        # Private instance attribute to store the square's size
        self.__size = size

#!/usr/bin/python3

"""Module that defines a Square class with position handling."""


class Square:
    """Class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with size and position.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not isinstance(position[0], int) or position[0] < 0 or
            not isinstance(position[1], int) or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or value[0] < 0 or
            not isinstance(value[1], int) or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using the '#' character and position offset.

        If size is 0, prints an empty line.
        The position is used to offset the square horizontally and vertically.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

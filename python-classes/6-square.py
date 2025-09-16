#!/usr/bin/python3
"""Square class with size and position."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using # and underscores _ instead of spaces."""
        if self.__size == 0:
            print("$")
            return

        for _ in range(self.__position[1]):
            print("$")

        for _ in range(self.__size):
            print("_" * self.__position[0] + "#" * self.__size + "$")

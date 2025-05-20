#!/usr/bin/python3
"""Defines a class Square with size and position attributes."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
            position (tuple): Tuple of 2 positive integers for position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter: returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter: returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter: sets the position of the square.

        Args:
            value (tuple): Tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character,
        respecting the size and position.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical spacing
        for _ in range(self.__position[1]):
            print()

        # Print square lines with horizontal spacing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

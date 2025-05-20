#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Utilise le setter pour valider la taille dès la création
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square with validation.

        Args:
            value (int): The new size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        # Assignation après validation
        self.__size = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area computed as size * size.
        """
        return self.__size * self.__size

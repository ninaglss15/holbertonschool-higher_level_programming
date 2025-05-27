#!/usr/bin/python3
"""
Module 11-square
Defines class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that defines a square inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the string representation of the square.
        """
        return "[square] {}/{}".format(self.__size, self.__size)

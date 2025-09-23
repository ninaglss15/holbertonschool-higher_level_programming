#!/usr/bin/python3
"""
This module defines BaseGeometry, Rectangle, and Square classes.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square with validated size.

        Args:
            size (int): Size of the square sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: Area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return string representation of the square.

        Returns:
            str: [Rectangle] size/size
        """
        return f"[Rectangle] {self.__size}/{self.__size}"

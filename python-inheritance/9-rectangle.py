#!/usr/bin/python3
"""
This module defines a BaseGeometry class and a Rectangle.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.
    """

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable
            value (int): The value to validate

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with validated.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: Rectangle in the format [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

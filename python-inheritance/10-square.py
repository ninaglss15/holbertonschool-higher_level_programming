#!/usr/bin/python3
"""
This module defines BaseGeometry, Rectangle, and Square classes.
"""


class BaseGeometry:
    """
    Base class representing geometry.
    """

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.

        Args:
            name (str): Name of the variable (for error messages)
            value (int): Value to validate

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' <= 0
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
        Initialize a rectangle with validated width and height.

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
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of the rectangle.

        Returns:
            str: [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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

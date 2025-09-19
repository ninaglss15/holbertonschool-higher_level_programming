#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle defined by width and height.

    Attributes:
        number_of_instances (int): Counter for the number of Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle with '#'.

        Returns:
            str: The rectangle drawn with '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """Return a string representation that can recreate the instance.

        Returns:
            str: String in the form Rectangle(width, height).
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method.

        Decrements the instance counter and prints a message when
        the object is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

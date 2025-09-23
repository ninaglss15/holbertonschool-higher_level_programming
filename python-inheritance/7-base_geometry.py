#!/usr/bin/python3

"""
This module defines an empty class BaseGeometry.
It can be used as a base class for other geometry-related classes.
"""


class BaseGeometry:
    """Base class with area method and integer validator"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name: the name of the value (used in exception messages)
            value: the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

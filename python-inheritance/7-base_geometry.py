#!/usr/bin/python3

"""
This module defines an empty class BaseGeometry.
It can be used as a base class for other geometry-related classes.
"""


class BaseGeometry:
    """
    An empty class representing base geometry.

    This class does not define any methods or attributes.
    It serves as a base class for inheritance purposes.
    """

    def area(self):
        """
        Public method to compute the area of the geometry.

        Raises:
            Exception: Always raises "area() is not implemented" to
            indicate that subclasses should override this method.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable (used in error messages)
            value (int): The value to validate

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

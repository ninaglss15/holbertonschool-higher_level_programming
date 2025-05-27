#!/usr/bin/python3

"""Module that defines the BaseGeometry
class with area and validation methods."""


class BaseGeometry:
    """Base class for geometric objects."""

    def area(self):
        """Raises an exception indicating that the area method
        is not implemented."""
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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with an area method."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

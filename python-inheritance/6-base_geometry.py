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

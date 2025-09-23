#!/usr/bin/python3

"""
This module defines an empty class BaseGeometry.
It can be used as a base class for other geometry-related classes.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur validées.

        Args:
            width (int): largeur du rectangle
            height (int): hauteur du rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

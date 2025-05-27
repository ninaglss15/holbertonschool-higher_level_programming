#!/usr/bin/python3

"""Module defining abstract shape interface and concrete shape classes."""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape with methods to compute area and perimeter."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.__radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return pi * self.__radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * (pi * self.__radius)


class Rectangle(Shape):
    """Rectangle shape with methods to compute area and perimeter."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Prints the area and perimeter of any shape implementing\
        area() and perimeter()."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

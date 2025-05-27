#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.

    Subclasses must implement:
    - area() -> float
    - perimeter() -> float
    """

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Return the circle's area."""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Return the circle's perimeter (circumference)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the rectangle's area."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape: Shape) -> None:
    """
    Print the area and perimeter of the given shape.

    Relies on duck typing: assumes shape implements
    area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

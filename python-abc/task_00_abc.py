#!/usr/bin/env python3

"""Module defining an abstract Animal class and its concrete subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    Subclasses must implement:
    - sound() -> str
    """

    @abstractmethod
    def sound(self) -> str:
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog implementation of Animal."""

    def sound(self) -> str:
        return "Bark"


class Cat(Animal):
    """Cat implementation of Animal."""

    def sound(self) -> str:
        return "Meow"

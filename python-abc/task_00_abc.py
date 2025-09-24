#!/usr/bin/env python3
"""
Module defining an abstract Animal class and concrete subclasses
Dog and Cat, each implementing their own sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class implementing Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"

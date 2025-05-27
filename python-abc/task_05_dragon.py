#!/usr/bin/python3

"""Module defining mixins and a Dragon class using multiple inheritance."""


class SwimMixin:
    """Mixin class to add swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A mythical creature that can swim, fly, and roar."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")

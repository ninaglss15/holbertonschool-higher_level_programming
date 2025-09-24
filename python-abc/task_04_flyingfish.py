#!/usr/bin/env python3

"""Module demonstrating multiple inheritance with Fish and Bird classes."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints how the fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints how the bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Prints how the flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints how the flying fish swims."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    """Main block to demonstrate FlyingFish behavior and MRO."""
    ff = FlyingFish()
    ff.fly()
    ff.swim()
    ff.habitat()
    print(FlyingFish.mro())

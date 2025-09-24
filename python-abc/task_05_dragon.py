
#!/usr/bin/env python3

"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin class to add swimming ability."""
    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying ability."""
    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming, flying, and roaring abilities."""
    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    """Test the Dragon class and its abilities."""
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
    print(Dragon.mro())

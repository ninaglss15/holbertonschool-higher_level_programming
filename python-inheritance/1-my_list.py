#!/usr/bin/python3

"""Module that defines the MyList class, which inherits from list."""


class MyList(list):
    """Custom list class that extends the built-in list class
        with a sorted printer."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without
            modifying the original list."""
        print(sorted(self))

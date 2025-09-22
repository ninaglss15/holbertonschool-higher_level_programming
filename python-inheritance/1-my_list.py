#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from
Python's built-in list and adds a method to print a sorted list.
"""


class MyList(list):
    """
    Custom list class that inherits from Python's built-in list.
    """

    def print_sorted(self):
        """
        Print the list in ascending order without modifying
        the original list.

        Uses the built-in sorted() function to create a new
        sorted list and prints it. The original list remains unchanged.
        """
        print(sorted(self))

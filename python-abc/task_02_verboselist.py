#!/usr/bin/env python3
"""
Module defining the VerboseList class that extends Python's built-in list.
This class prints notifications whenever items are added or removed.
"""


class VerboseList(list):
    """Custom list that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item at index (default last) and print a notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

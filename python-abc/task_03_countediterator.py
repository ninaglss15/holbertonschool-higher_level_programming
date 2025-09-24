#!/usr/bin/env python3
"""
Module defining the CountedIterator class.
This class wraps an iterator and keeps track of how many items
have been iterated over.
"""


class CountedIterator:
    """Iterator that counts the number of items returned."""

    def __init__(self, iterable):

        self.iterator = iter(iterable)

        self.count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """
        Return the next item from the iterator,
        incrementing the counter each time.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

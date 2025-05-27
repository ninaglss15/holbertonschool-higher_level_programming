#!/usr/bin/env python3

"""Module defining CountedIterator class that counts iterated items."""


class CountedIterator:
    """
    Iterator wrapper that counts the number of items iterated.

    Attributes:
        iterator (iterator): The underlying iterator object.
        count (int): Number of items iterated so far.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment count.

        Raises:
            StopIteration: When the iterator is exhausted.
        """
        item = next(self.iterator)  # May raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items iterated so far.

        Returns:
            int: The count of iterated items.
        """
        return self.count

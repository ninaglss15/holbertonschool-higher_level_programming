#!/usr/bin/python3

class Square:
    # Definition of a class called "Square".

    def __init__(self, size):
        # The constructor method (__init__) is called automatically
        # when a new Square object is created.
        # It initializes the attribute(s) of the object.

        self._Square__size = size
        # This creates a private attribute called "__size".
        # The special name "self._Square__size" is how Python
        # "mangles" the name to make it less accessible from outside.
        # It’s a way to indicate that this attribute should not be
        # directly modified from outside the class.

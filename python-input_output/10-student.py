#!/usr/bin/python3
"""
Defines a Student class with JSON serialization capabilities.
"""

import json


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of attribute names, return only those attributes
        that exist in the instance. Otherwise, return all attributes.
        """
        if isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

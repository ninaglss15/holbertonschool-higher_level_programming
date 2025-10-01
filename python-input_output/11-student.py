#!/usr/bin/python3

"""
Module that defines the Student class.
"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            result = {}
            for key in attrs:
                if isinstance(key, str) and key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with those
        from the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)

#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of a Student."""
        return (self.__dict__)

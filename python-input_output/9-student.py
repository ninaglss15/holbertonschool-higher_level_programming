#!/usr/bin/python3
"""
This module defines a Student class with serializable attributes.
"""


class Student:
    """
    Represents a student with first name, last name and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, value in a_dictionary.items():
        result = value*2
        new[key] = result
    return new

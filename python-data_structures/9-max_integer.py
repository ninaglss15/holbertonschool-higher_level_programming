#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = None
    for num in my_list:
        if max_value is None or num > max_value:
            max_value = num
    return max_value

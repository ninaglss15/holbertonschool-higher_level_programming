#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = i
        return max

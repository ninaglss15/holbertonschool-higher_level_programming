#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_listt = my_list[:]
    if idx < 0:
        return new_listt
    elif idx >= len(my_list):
        return new_listt
    else:
        new_listt[idx] = element
        return new_listt

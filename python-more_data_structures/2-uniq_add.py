#!/usr/bin/python3

def uniq_add(my_list=[]):
    views = 0
    uniq = set(my_list)
    for i in uniq:
        views += i
    return views

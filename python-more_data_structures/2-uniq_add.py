#!/usr/bin/python3
def uniq_add(my_list=[]):
    compt = 0
    uniq = set(my_list)
    for i in uniq:
        compt += i
    return compt

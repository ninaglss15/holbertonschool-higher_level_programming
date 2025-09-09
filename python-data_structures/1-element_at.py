#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx <= 0:
            return None
        elif idx > i:
            return None
        else:
            print("Element at index {} is {}".format(i, idx))

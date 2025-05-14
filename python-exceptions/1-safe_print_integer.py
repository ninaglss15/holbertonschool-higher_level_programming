#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return True
    except:  # noqa: E722
        return False

#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    argc = sys.argv
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments")
    elif argc == 1:
        print("1 arguents")
    else:
        print("{} arguments:" .format(argc))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

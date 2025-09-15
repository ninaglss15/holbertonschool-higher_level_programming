#!/usr/bin/python3
class Square:
     def __init__(self, size=0) :
        self._Square__size = size
        if size != int:
            print("size must be an integer")
        if size < 0:
            print("size must be >= 0")

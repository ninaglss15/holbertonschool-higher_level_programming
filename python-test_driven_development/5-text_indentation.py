#!/usr/bin/python3
"""
This module defines a function that prints a text with
2 new lines after each '.', '?' and ':'
"""



def text_indentation(text):
    """
    that handle if text is wrong type and add 2 spaces after : ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

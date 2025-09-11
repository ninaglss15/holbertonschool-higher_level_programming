#!/usr/bin/python3
"""
Module for text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.
    Args:
        text (str): The text to process.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ".?:"

    result = ""
    skip_spaces = True

    for char in text:
        if char == '\n':
            result += '\n'
            skip_spaces = True

        elif char in punctuation:
            while result and result[-1] == ' ':
                result = result[:-1]
            result += char
            result += "\n\n"
            skip_spaces = True

        elif char == ' ':
            if not skip_spaces:
                result += ' '
        else:
            result += char
            skip_spaces = False

    lines = result.split('\n')
    stripped_lines = [line.strip() for line in lines]
    final_result = "\n".join(stripped_lines)

    print(final_result, end="")

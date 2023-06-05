#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing whitespace
    result = ""
    skip_space = False

    for char in text:
        if char == "." or char == "?" or char == ":":
            result += char + "\n\n"
            skip_space = True
        else:
            if skip_space and char == " ":
                continue
            result += char
            skip_space = False

    print(result, end="")

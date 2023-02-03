#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_t = ""
    for i in range(len(text)):
        new_t += text[i]
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            new_t += "\n\n"
    print(new_t, end="")

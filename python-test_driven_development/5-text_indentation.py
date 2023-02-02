#!/usr/bin/python3
"""text indentation"""

#(.?:) chars
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            print()
        else:
            print(text[i].strip(), end="")

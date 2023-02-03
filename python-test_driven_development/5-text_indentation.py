#!/usr/bin/python3
"""text indentation"""

#(.?:) chars
def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_t = ""
    for i in range(len(text)):
        new_t += text[i] 
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            new_t += '\n\n'
    print(new_t, end="")


#!/usr/bin/python3
'''Append text to a file'''


def append_write(filename="", text=""):
    '''append text to a file and return number of chars in'''
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    words = text
    num_chars = 0
    for word in words:
        for i in word:
            num_chars += 1
    return num_chars
    f.close()

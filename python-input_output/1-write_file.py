#!/usr/bin/python3
'''Write to a file'''


def write_file(filename="", text=""):
    '''write text in a file and return number of chars in'''
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    words = text
    num_chars = 0
    for word in words:
        for i in word:
            num_chars += 1
    return num_chars
    f.close()

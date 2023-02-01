#!/usr/bin/python3
'''Integers addition'''


def add_integer(a, b=98):
    '''add int a and b'''
    if type(a) == int and type(b) == int:
        return a + b
    elif type(a) == float:
        return int(a) + b
    elif type(b) == float:
        return a + int(b)
    else:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")

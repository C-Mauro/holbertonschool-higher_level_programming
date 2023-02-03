#!/usr/bin/python3
'''Integers addition'''


def add_integer(a, b=98):
    '''add int a and b'''
    if type(a) == float or type(b) == float:
        return int(a) + int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b

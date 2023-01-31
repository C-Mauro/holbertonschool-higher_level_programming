#!/usr/bin/python3
'''size validation'''


class Square:
    '''A square with attribute size'''
    def __init__(self, size=0):
        '''Initialize variables'''
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

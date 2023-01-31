#!/usr/bin/python3
'''Area of Square'''


class Square:
    '''square with size attribute'''
    def __init__(self, size=0):
        '''Initialize variables'''
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Return the squeare area'''
        return (self.__size ** 2)

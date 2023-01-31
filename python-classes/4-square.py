#!/usr/bin/python3
'''Access and update private attribute'''


class Square:
    '''square with size attribute'''
    def __init__(self, size=0):
        '''Initialize variables'''
        self.__size = size

    @property
    def size(self):
        '''retieve the data'''
        return self.__size

    @size.setter
    def size(self, value):
        '''update data'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the squeare area'''
        return (self.__size ** 2)

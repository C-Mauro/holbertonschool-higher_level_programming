#!/usr/bin/python3
'''Printing a square'''


class Square:
    '''square with size attribute'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize variables'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''retrieve position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''update position'''
        if type(value) != int or value < 0 or type(self.__position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the squeare area'''
        return (self.__size ** 2)

    def my_print(self):
        '''print a square'''
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

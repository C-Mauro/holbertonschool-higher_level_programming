#!/usr/bin/python3
'''Area and Perimeter'''


class Rectangle:
    '''defines a rectangle with atributte width and height'''

    def __init__(self, width=0, height=0):
        '''initialize variables'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieve rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''update the width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieve rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''update rectangle height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

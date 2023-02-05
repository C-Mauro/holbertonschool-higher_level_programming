#!/usr/bin/python3
'''Definition of a rectangle'''


class Rectangle:
    '''define a rectangle atributes: width and height'''
    def __init__(self, width=0, height=0):
        '''initialize variables'''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' retrieve the data'''
        return self.__width

    @width.setter
    def width(self, value):
        '''update data'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieve data'''
        return self.__height

    @height.setter
    def height(self, value):
        '''update data'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

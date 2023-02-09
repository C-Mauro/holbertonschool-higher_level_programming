#!/usr/bin/python3
''' Rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle'''
    def __init__(self, width, height):
        '''initialize variables and check with integer_validator'''
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

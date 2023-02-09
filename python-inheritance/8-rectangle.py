#!/usr/bin/python3
'''rectange'''


class BaseGeometry:
    '''base class'''

    def area(self):
        '''not define area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''check if the value is int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''rectangle'''
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

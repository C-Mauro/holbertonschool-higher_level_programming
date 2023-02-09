#!/usr/bin/python3
'''integer validator'''


class BaseGeometry:
    '''integer validator'''
    def area(self):
        '''not define area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''check if the value is int'''
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")

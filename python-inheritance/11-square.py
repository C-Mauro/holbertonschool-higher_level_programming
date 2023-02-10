#!/usr/bin/python3
'''Square #1'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size):
        '''define square size'''
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        '''square area'''
        area = self.__size * self.__size
        return area

    def __str__(self):
        '''print operation'''
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
'''define a square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''define a square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize variables'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns string'''
        id = self.id
        x = self.x
        y = self.y
        size = self.height
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

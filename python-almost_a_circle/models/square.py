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

    def update(self, *args, **kwargs):
        '''update arguments'''
        args_len = len(args)
        kwargs_len = len(kwargs)
        add_args = ['id', 'size', 'x', 'y']
        if args_len > 0:
            for arg in range(args_len):
                setattr(self, add_args[arg], args[arg])
        if kwargs_len > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation of a Square'''
        s_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
        return s_dict

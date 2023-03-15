#!/usr/bin/python3
'''first rectangle'''
from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''define the rectangle area'''
        return self.__width * self.__height

    def display(self):
        '''display a rectangle'''
        if self.__y > 0:
            for i in range(self.__y):
                print("")
        for i in range(self.__height):
            x = " "*self.__x
            width = "#"*self.__width
            print("{}{}".format(x, width))

    def __str__(self):
        '''returns string'''
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        '''update arguments'''
        args_len = len(args)
        kwargs_len = len(kwargs)
        add_args = ['id', 'width', 'height', 'x', 'y']
        if args_len > 0:
            for arg in range(args_len):
                setattr(self, add_args[arg], args[arg])
        if kwargs_len > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation of a Rectangle'''
        r_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }
        return r_dict

#!/usr/bin/python3
'''Student to JSON with filter'''


class Student:
    '''define student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation of a Student instance'''
        
        new_dict ={}
        for key, value in self.__dict__.items():
            for key in attrs:
                new_dict[key] = key
        return new_dict

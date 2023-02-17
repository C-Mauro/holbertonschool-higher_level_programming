#!/usr/bin/python3
'''base class'''
import json


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialize'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

#!/usr/bin/python3
''' Student to disk and reload'''


class Student:
    '''define student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation of a Student instance'''
        my_dict = self.__dict__
        filter_dict = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return my_dict

                if attr in my_dict:
                    filter_dict[attr] = my_dict[attr]

            return filter_dict

        return my_dict

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            setattr(self, key, value)

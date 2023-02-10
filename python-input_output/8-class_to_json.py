#!/usr/bin/python3
'''Class to JSON'''
from_json_string = __import__('4-from_json_string').from_json_string
to_json_string = __import__('3-to_json_string').to_json_string


def class_to_json(obj):
    '''returns the dictionary description'''
    new_c = to_json_string(obj.__dict__)
    return from_json_string(new_c)

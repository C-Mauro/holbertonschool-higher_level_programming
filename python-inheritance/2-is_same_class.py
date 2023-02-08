#!/usr/bin/python3
'''check if the object is an instance of the specified class'''


def is_same_class(obj, a_class):
    '''true if is an intance of an especific class'''
    if a_class is object or a_class is not type(obj):
        return False
    return isinstance(obj, a_class)

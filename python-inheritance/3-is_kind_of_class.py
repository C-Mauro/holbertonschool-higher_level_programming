#!/usr/bin/python3
'''same class or inherit from'''


def is_kind_of_class(obj, a_class):
    ''' return true if have the same class or inherit from'''
    if isinstance(obj, a_class):
        return True

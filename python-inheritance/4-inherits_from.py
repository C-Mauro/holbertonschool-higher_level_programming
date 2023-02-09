#!/usr/bin/python3
'''Only sub class of'''


def inherits_from(obj, a_class):
    '''return True if is an instance of a class that inherited'''
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)

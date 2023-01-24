#!/usr/bin/python3


def no_c(my_string):
    ch = 'cC'
    new_str = ''.join(x for x in my_string if x not in ch)
    return new_str

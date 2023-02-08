#!/usr/bin/python3
''' func. that prints the list, but sorted '''


class MyList(list):
    '''Mylist class'''
    def print_sorted(self):
        '''print a sorted list'''
        new = sorted(self)
        print(new)

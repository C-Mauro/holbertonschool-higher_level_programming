#!/usr/bin/python3
'''Save Object to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file'''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

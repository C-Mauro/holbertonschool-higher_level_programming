#!/usr/bin/python3
'''Create object from a JSON file'''
import json


def load_from_json_file(filename):
    '''return a "json file" into an object'''
    with open(filename) as f:
        obj = json.loads(f.read())
        return obj

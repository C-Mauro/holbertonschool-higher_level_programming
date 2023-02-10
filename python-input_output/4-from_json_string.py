#!/usr/bin/python3
'''From JSON string to Object'''
import json


def from_json_string(my_str):
    '''Deserializes a JSON object to a standard python object'''
    return json.loads(my_str)

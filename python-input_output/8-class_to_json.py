#!/usr/bin/python3
'''Class to JSON'''
import json


def class_to_json(obj):
    '''returns the dictionary description'''
    class_dic = json.dumps(obj.__dict__)
    return json.loads(class_dic)

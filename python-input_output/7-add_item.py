#!/usr/bin/python3
'''Load, add, save'''

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = argv[1:]
n_list = []

try:
    load_from_json_file("add_item.json")

except:
    n_list = []

finally:
    for arg in arguments:
        n_list.append(arg)
    save_to_json_file(n_list, "add_item.json")

#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list == []:
        return []

    new = my_list.copy()
    for i in range(len(my_list)):
        if new[i] == search:
            new[i] = replace
    return new

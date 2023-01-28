#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    size = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            size += 1
        except (ValueError, TypeError) as Error:
            continue
    print()
    return size

#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        if b != 0:
            print("Inside result: {}".format(a / b))
            return a / b

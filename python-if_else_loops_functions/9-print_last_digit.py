#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if number < 0:
        last_digit = 10 - last_digit
    print(last_digit, end="")
    return last_digit

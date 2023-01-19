#!/usr/bin/python3

for j in range(0, 9):
    for i in range(0, 10):
        if j < i and j != i and j != 8:
            print(f"{j}{i}".format(range), end=", ")
    if j == 8:
        print(f"{j}{i}".format(range))

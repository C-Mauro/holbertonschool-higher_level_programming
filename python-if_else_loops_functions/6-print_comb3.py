#!/usr/bin/python3

for j in range(0, 9):
    for i in range(0, 10):
        if j < i and j != i:
            print(f"{j}{i}".format(range), end=", ")


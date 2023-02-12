#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    '''representing the Pascal’s triangle'''
    if n <= 0:
        return []

    tri = []
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        tri.append(row)
        row = [left + right for left, right in zip(row + y, y + row)]
    return tri

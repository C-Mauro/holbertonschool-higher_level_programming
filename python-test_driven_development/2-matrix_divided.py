#!/usr/bin/python3
"""divide a matrix"""


def matrix_divided(matrix, div):

    """Take the values of a matrix en divide"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if check_matrix(matrix) is not True or int_values(matrix) is not True:
        raise TypeError(err)
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round((x / div), 2) for x in i] for i in matrix]
    return new_matrix


def check_matrix(matrix):
    """check if a matrix is a list of lists"""
    if all(isinstance(i, list) for i in matrix):
        return True


def int_values(matrix):
    """ check if the values in matrix are float or int"""
    for row in matrix:
        for i in row:
            if isinstance(i, (int, float)):
                return True

#!/usr/bin/python3
""" matrix dividednd class """


def matrix_divided(matrix, div):
    """ uses two args, matrix and div """
    if type(matrix) is not list or not all((type(i) is list)for i in matrix) \
        or not all((isinstance(j, (int, float))for j in i)for i in matrix) \
            or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    i = len(matrix[0])
    if not all((len(x) == i)for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), r))for r in matrix])

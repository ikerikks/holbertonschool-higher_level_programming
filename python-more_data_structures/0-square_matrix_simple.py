#!/usr/bin/python3
from re import M


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    
    for i in range(len(new_matrix)):
        new_matrix[i] = list(map(lambda y: y * y, matrix[i]))

    return new_matrix


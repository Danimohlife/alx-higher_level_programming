#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matr = [row[:] for row in matrix]

    for x in range(len(new_matr)):
        for y in range(len(new_matr[x])):
            new_matr[x][y] = new_matr[x][y] ** 2
    return new_matr

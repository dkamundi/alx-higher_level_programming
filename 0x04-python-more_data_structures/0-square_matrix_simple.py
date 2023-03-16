#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        row = list(map((lambda col: col * col), row))
        sq_matrix.append(row)
    return sq_matrix

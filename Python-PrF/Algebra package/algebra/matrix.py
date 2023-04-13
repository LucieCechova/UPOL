from algebra.vector import dot_product
"""Editing matrices""" 
def matrix_multiplication(matrix_1, matrix_2):
    """Multiplication of two matrices. """
    mul_matrix = []
    trans_matrix_2 = []

    """Transpositioning the second matrix."""
    t_matrix = zip(*matrix_2)
    for row_2 in t_matrix:
        trans_matrix_2.append(row_2)

    """Multiplying first matrix with transpositioned second one."""
    for row_1 in matrix_1:
        mul_matrix_row = []
        for row_2 in trans_matrix_2:
            mul_matrix_row.append(dot_product(row_1, row_2))
        mul_matrix.append(mul_matrix_row)
    return(mul_matrix)

def matrix(shape,fill):
    """Creating an "x,y(shape)" sized matrix filled with "fill" number.""" 
    x, y = shape
    new_matrix = []
    for _ in range(x):
        new_matrix.append([fill] * y)
    return(new_matrix)

def submatrix(matrix, drop_rows= [], drop_columns = []):
    """Creating new matrix with some deleted rows and columns."""
    trans_column_matrix = []
    column_matrix = []
    trans_row_matrix = []
    row_matrix = []

    """Sub-function for transpositioning the matrix."""
    def transmatrix(matrix):
        trans_matrix = []
        t_matrix = zip(*matrix)
        for row in t_matrix:
            trans_matrix.append(row)
        return(trans_matrix)
    
    """Sub-function for creating new matrix and removing rows(columns) from it."""
    def remove_row(matrix, drop):
        new_matrix = []
        row_list = []
        for idx, row in enumerate(matrix):
            row_list = list(row)
            new_matrix.append(row_list)
            print(new_matrix)
            if idx in drop:
                new_matrix.remove(row_list)
        return(new_matrix)

    trans_column_matrix = transmatrix(matrix)
    column_matrix = remove_row(trans_column_matrix, drop_columns)
    trans_row_matrix = transmatrix(column_matrix)
    row_matrix = remove_row(trans_row_matrix, drop_rows)

    return(row_matrix)
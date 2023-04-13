matrix = (
    (-1, -2, -5, -20),
    (-10, -2, -3, -400),
    (-100, -2, -3, -4)
    )
matrix_list = []

for idx, row in enumerate(matrix):
    matrix_list.extend(row)
    print(idx, row)

maximal = max(matrix_list)
summation = sum(matrix_list)
print(f"maximal={maximal}, summation={summation}")

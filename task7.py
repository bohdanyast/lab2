import numpy as np

matrix = np.arange(1, 101).reshape(10, 10)
matrix_as_string = np.array2string(matrix, separator=', ')

print(matrix_as_string)

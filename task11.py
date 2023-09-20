import numpy as np

matrix = np.arange(1,10).reshape(3,3)
max_in_rows = np.max(matrix, axis=0)
min_in_rows = np.min(matrix, axis=0)
max_in_columns = np.max(matrix, axis=1).reshape(3,1)
min_in_columns = np.min(matrix, axis=1).reshape(3,1)


print(f'''
{max_in_rows}, 
{min_in_rows}, 
{max_in_columns}, 
{min_in_columns}''')
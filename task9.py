import numpy as np

arr = np.array([1, 2, 3])
new_arr = np.resize(arr, (1, len(arr)*10))
print(new_arr)

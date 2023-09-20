import numpy as np


a = np.arange(1, 101)
a_reshaped = np.reshape(a, (100, 1))

print(a, np.shape(a_reshaped), a_reshaped)

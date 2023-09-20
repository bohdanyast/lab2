import numpy as np

a = np.array(np.arange(1.0, 101.0))
np.set_printoptions(precision=1, floatmode='fixed')
b = a.reshape(10, 10)

print(b)


import numpy as np
a = np.array([10, 20, 30, 40, 50])

print(a[(a > 20) & (a < 50)])

a = np.array([10, 20, 30, 40])

result = np.where(a > 20, 1, 0)

print(result)
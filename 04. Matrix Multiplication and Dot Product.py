import numpy as np

#A. Element-wise multiplication
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print(a * b)  


#B. Actual matrix multiplication

print(a @ b)
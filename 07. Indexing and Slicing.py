import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])    # 10
print(a[2])    # 30
print(a[-1])   # 50

#slicing
a = np.array([10, 20, 30, 40, 50])

print(a[1:4])   # [20 30 40]
print(a[:3])    # [10 20 30]
print(a[2:])    # [30 40 50]
print(a[::2])   # [10 30 50]

#indexing in 2d array 
a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(a[0, 1])    # 20
print(a[2, 2])    # 90
print(a[0, :])    # [10 20 30]
print(a[:, 1])    # [20 50 80]
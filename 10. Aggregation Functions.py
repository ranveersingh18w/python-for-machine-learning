import numpy as np

a = np.array([10, 20, 30, 40])

print(np.sum(a))    # 100
print(np.mean(a))   # 25.0
print(np.max(a))    # 40
print(np.min(a))    # 10
print(np.std(a))    # 11.18 approximately
print(np.var(a))    # 125.0

"""Function	Purpose
np.sum()	Sum
np.mean()	Average
np.median()	Median
np.min()	Minimum
np.max()	Maximum
np.std()	Standard deviation
np.var()	Variance
np.prod()	Product
np.argmin()	Index of minimum value
np.argmax()	Index of maximum value"""
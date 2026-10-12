from numpy import average
import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(np.average(a[0,:]))

print((a[a>50]))


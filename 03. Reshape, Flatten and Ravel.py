import numpy as np

#A. reshape()
a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print(b)

#flaten
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.flatten())

#ravel
print(a.ravel())

"""flatten() copy banata hai. ravel() possible hone par view return karta hai, matlab original data share ho sakta hai."""
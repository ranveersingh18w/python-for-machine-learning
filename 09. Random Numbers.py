import numpy as np

rng = np.random.default_rng()

a = rng.integers(1, 10, size=5)
print(a)


a = rng.random(5)
print(a)

#random matrix

a = rng.integers(1, 10, size=(2, 3))
print(a)

"""
Function	Purpose
rng.integers()	Random integers
rng.random()	Random decimals from 0 to 1
rng.uniform()	Random decimals within a chosen range
rng.normal()	Random numbers from a normal distribution
rng.choice()	Randomly select elements
rng.shuffle()	Shuffle elements in place
rng.permutation()	Generate a random ordering"""
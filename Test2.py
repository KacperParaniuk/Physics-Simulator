import matplotlib.pyplot as plt
import numpy as np 

a = np.array([1,2,3])
print(a)

b = np.ones((2,3))
print(b)

c = np.zeros((2,3))

h = np.hstack([b,c])
print(h)

v = np.vstack([b,c])
print(v)
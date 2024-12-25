import matplotlib.pyplot as plt
import numpy as np 

#a = np.array([1,2,3])
# print(a)

# print(a[0])

# b = np.ones((2,3))
# print(b)

# c = np.zeros((2,3))

# h = np.hstack([b,c])
# print(h)

# v = np.vstack([b,c])
# print(v)

# a = np.array([[1,2],[2,1]])
# b = np.ravel(a)
# c = b.ravel()
# d = a.flatten()

# d[1]=11
# b[2] =22

# print(a)
# print(b)
# print(c)
# print(d)

a = np.arange(12)
b = np.reshape(a, (3,4)) # size is consistent 3 x 4 = 12
print(a)
print(b)

c = b.reshape((2,6)) # size is consistent 3 x 4 = 12
print(c)

d = c.reshape((2,3,2))
print(d)

# ndarray is an array object with the same data as original array

# Reshaping any array into a row vector or column vector. 

z = np.arange(10)
z_row = z.reshape(1,-1) # creating a row vector 
print(f"Normal Array: {z}")
print(f"Row Vector: {z_row} ")

z_column = z.reshape(-1, 1)
print(f"Column Vector: {z_column}")

# list indices

aa = np.arange(10,21)
b  = [2, 4, 5]

print(aa[b])

bb = np.arange(-10, 11)
print(bb)
less_than_five = (abs(bb)<5) ## returns an array of trues / falses of the condition using values from array given
print(less_than_five)
cc = bb[less_than_five] ## looks for elements of less than five 
print(cc)

# orr (prints same thing)

dd = bb[abs(bb)<5]
print(dd)

s = "{1:d} plus {0:d} is {2:d}"
print(s.format(2,4, 2+4))
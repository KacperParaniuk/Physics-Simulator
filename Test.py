from random import randint
import numpy as np
import matplotlib.pyplot as plt

# a = np.zeros((3,5))
# b = np.ones((3,5))
# c = np.eye(3)

# a = np.arange(1,10) # prints 1 - 9 in an array 
#a =  np.arange(5)  prints 0 - 4 in an array 
# a= np.arange(2.1, 5.4, 0.1) prints 2.1 - 5.4 for every .1 increment np.arrange(start,end,increment)

# d = [2.71, 3.14, 3000] # simple array of those valuesd
# e = np.array([2.71, 3.14,3000]) # row
# f = np.array([[2.71], [3.14], [3000]]) # column
# g = np.array([[2.71, 3], [3.14, 5], [3000, 6]]) # 2 x 3
# h = np.array([[2,3,5], [7,11,13]])

#a = np.arange(0,10,2)
#a = np.arange(0,10,1.5)
#b= np.linspace(0,10,7)
#b = np.linspace(2,10,6)

print("Arrays")
x_min = 0
x_max =10
dx = 0.1
x_array = np.arange(x_min, x_max+dx, dx)
print(x_array)

a = np.zeros((2,3))
b = np.ones((2,3))
h = np.hstack([a,b])
v = np.vstack([a,b])

print(a)
print(b)
print(h)
print(v)

print(v.shape) # not adding values adding matrices together 2x3 + 2x3 vertically = 4x3
print(h.shape) # not adding values adding matrices together 2x3 + 2x6 horizontally = 2x6
sum = 0 

A = np.array( [2,3,4])
print(A)
A[0]
A[1] = 100
print(A)

B = np.array([[2,3,5], [7,11,13]])
B[0,1]
B[1,2]= 999
print(B)

g = np.arange(20)
print(g)
print(f"{g[:]} :Slicing")
print(g[::])
print(g[5:15])
print(g[5:15:3])
print(g[5::])
print(g[:5:])
print(g[::5])

print(g)
print(g[:5])

print(g[1::2])


# Flattening  

print("Flattening / Reshaping")
d = np.array([[1,2], [2,1]])
print(d)
print(np.ravel(d))
print(d.ravel())
print(d.flatten())

# Reshaping





print(f"{np.sqrt(4)}: Result of Sqrt 4") # imported from numpy

print("You are going to add two numbers")
num1 = int(input("What is the first number? \n>"))
num2 = int(input("What is the second number? \n>"))


print(f"{num1+num2} :User Sum")

num3 = randint(0,20)
num4 = randint(0,20)

print(f"{num3+num4} :Random Sum")

for x in range(20):
    sum+=x
    print(x)

print(sum)

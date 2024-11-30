from random import randint
import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((3,5))
b = np.ones((3,5))
c = np.eye(3)

print(a)

d = [2.71, 3.14, 3000] # simple array of those valuesd
e = np.array([2.71, 3.14,3000]) # row
f = np.array([[2.71], [3.14], [3000]]) # column
g = np.array([[2.71, 3], [3.14, 5], [3000, 6]]) # 2 x 3
print(f)


sum = 0 

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

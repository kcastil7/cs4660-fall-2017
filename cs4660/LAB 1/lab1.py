##Question 1
import numpy as np


##Question 2

a = np.arange(10)
a[4] = 1
print(a)

#Question 3

b = np.arange(9).reshape(3,3)
print(b)

a = np.zeros((3,4))

a[:,:-1] = b
print(a)

#Question 4

a = np.arange(10,50)
print(a)

#question 5
a = a[::-1]
print(a)

#Question 6

a = np.arange(0,16).reshape(4,4)
print(a)

#Question 7

a = np.floor(10 * np.random.rand(27).reshape(3,3,3))
print(a)

#Question 8

a = np.floor(10 * np.random.rand(100)).reshape(10,10)
print ("min is : ",a.min(axis = 1).min(axis = 0))
print("max is : ", a.max(axis=1).max(axis = 0))

#Question 9

a =np.floor(100 * np.random.rand(30))
print(a)

sum = a.sum(axis = 0)

sum = sum/30
print("mean is " ,sum)


#Question 10 NaN is Not a Number
def myFunc(a):
    a[(a>3) & (a<8)] = False
    print(a)


myFunc(np.arange(10))




















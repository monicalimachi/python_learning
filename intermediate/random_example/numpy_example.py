import numpy as np

a=np.random.rand(3)         #Add dimension to random int
print(a)

a=np.random.randint(0,10,3) #Add 0 -10 random values with size 3
print(a)

a=np.random.randint(0,10,(3,4))     #Add random values 1-10 in tuples 3x4 high array
print(a)

arr=np.array([[1,2,3],[4,5,6,],[7,8,9]])    #Add array and sort in different way, np.generator uses different than python standar library
print(arr)                                  #Shuffle, modify position not mix values, only first axes
np.random.shuffle(arr)
print(arr)

np.random.seed(1)                           #Another way to create random values for high array
np.random.seed(1)
print(np.random.rand(3,3))

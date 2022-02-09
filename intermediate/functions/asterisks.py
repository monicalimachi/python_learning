# * * * * * * *
result= 5*7
result2=2**4
print(result)
print(result2)

#Creates a list with 10 elements
zeros=[0] * 10
print(zeros)

#Create tuples
zeros = (0,1) * 10
print(zeros)
zeros = "AB" *10
print(zeros)

#Create args with * and kwargs with **

def foo(a,b,*args,**kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)

# Use one * in function - enforce only key words arguments
def foo(a,b,*,c):
    print(a,b,c)

foo(1,2,c=3)

#Use * for  argument unpacking
def foo(a,b,c):
    print(a,b,c)

my_list=[0,1,2]
foo(*my_list)

#Use ** in dictionaries to unpack . always key must match
def foo(a,b,c):
    print(a,b,c)

my_dict={'a':1,'b':2,'c':3}
foo(**my_dict)

# Unpack list comming from a list or tuple
numbers=[1,2,3,4,5,6]
#tuples_numbers=(9,8,7,6,5,4)
*beginning,last=numbers
print(beginning)        #Shows unpack in a list
print(last)             #displays the last value

#Unpack from the middle in a list
numbers=(1,2,3,4,5,6)

beginning,*middle,last=numbers
print(beginning)
print(middle)
print(last)

#Unpack from the middle in a list without the second last
numbers=(1,2,3,4,5,6)

beginning,*middle,secondlast,last=numbers
print(beginning)
print(middle)
print(secondlast)
print(last)

# * To add *tuples, *lists, *sets , merge elements
my_tuple=(1,2,3)
my_list=[4,5,6]
my_set={7,8,9}

new_list=[*my_tuple,*my_set,*my_list]
print(new_list)

# * to merge elements in dictionaries

dict_a = {'a':1,'b':2}
dict_b = {'c':3,'d':4}

my_dict={**dict_a,**dict_b}
print(my_dict)
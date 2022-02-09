""" 
- 1. The difference between arguments and parameters: arguments are passed while calling a function, parameters are the varaiables defined used in parenthesis
- 2. Position and keyword arguments
- 3. Default arguments
- 4. Variable lenght arguments (*args and **kwargs)
- 5. Container unpacking into function arguments
- 6. Local vs Global arguments
- 7. Parameter passing (by value or by reference)
 """

# 1. Arguments and parameters
#Variable: name
def print_name(name):
    print(name)

#argument: Alex
print_name('Alex')

# 2. Position and Keywords
def foo(a,b,c):
    print(a,b,c)

foo(1,2,3)          #Position
foo(a=1,b=2,c=3)   #Keyword

#3. Default argument
def foo(a,b,c,d=4):             #Add default value d value d=4
    print(a,b,c,d)

foo(1,2,3,88)                    #Pass another value   
foo(a=1,b=2,c=3)                #Don't pass any value for d

#4. Variable lenght arguments (*args and **kwargs)
def foo(a,b,*args,**kwargs):        # you can pass any number of position in args and kwargs shows key words and the values
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)
foo(1,2,3,4)                    #args 1,2, *args=3,4

#Add force keywords arguments after *
def foo(a,b,*,c,d):
    print(a,b,c,d)

foo(1,2,c=3,d=4)

#other example to force args and add last argument
def foo(*args,last):
    for arg in args:
        print(arg)
    print(last)

foo(1,2,3,last=100)

# 5. Container unpacking into function arguments the lenght must match the number of parameters
def foo(a,b,c):
    print(a,b,c)

my_list=[0,1,2]
my_tuple=(0,1,2)
my_dict={'a':1,'b':2,'c':3}     #for dict it must have the same keys as function - unpack into a function
foo(*my_list)
foo(*my_tuple)
foo(**my_dict)

# 6. Local vs Global arguments
def foo():
    global number                   #To modify a global variable inside a func
    x = number
    number=3
    print('number inside function', x)

number=0            #Start global variable
foo()
print(number)

#Other example
def foo():
    number=3            #it is a local variable

number=0                #it is a global variable
foo()
print(number)           #it call to global variable

# 7. Parameter passing (by value or by reference)
#Passing var int, it's immutable, then can't change
def foo(x):
    x=5

var=10
foo(var)
print(var)

# list is muttable, it can change
def foo(a_list):
    a_list.append(4)        #added 4 at the end
    a_list[0]=-100          #changed the first element [0] to -100

my_list = [1,2,3]
foo(my_list)
print(my_list)

#Creates local variables
def foo(a_list):
    a_list=[200,300,400]    #create a list with local variables,rebind the list, then it can't process list from main
    a_list.append(4)        
    a_list[0]=-100          

my_list = [1,2,3]           
foo(my_list)                #No value is processed in function
print(my_list)              # Original values of list are printed

#create a list and add other values in function
def foo(a_list):
   # a_list=a_list + [200,300,400]      #This option can't change values
    a_list+=[200,300,400]               #This option can change the list

my_list=[1,2,3]
foo(my_list)
print(my_list)

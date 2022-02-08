#Fibonacci
def fibonacci(limit):       #Start with 0 1 1 2 3 5 8 13 ...
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

fib = fibonacci(30)
for i in fib:
    print(i)



#Example1 expression For in loop
import sys
mygenerator=(i for i in range(100) if i%2==0)
print(sys.getsizeof(mygenerator))                   #The size of memory is less
""" for i in mygenerator:
    print(i)
 """
 
#Example2 expression for in loop list
mylist=[i for i in range(100) if i%2==0]
#print(mylist)                           
print(sys.getsizeof(mylist))                        #The size of memory is more
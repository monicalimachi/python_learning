#lambda arguments: expression - onle line function
add10 =lambda x: x+10               # same lambda function in one line
print(add10(6))

def add10_func(x):                  # Same function
    return x+10
print(add10_func(8))

mult= lambda x,y: x*y               # simple function used once or to hire other functions arguments
print(mult(5,9))


#---- sorting
points2D = [(1,2),(15,1),(5,-1),(10,4)]                 
points2D_sorted=sorted(points2D, key=lambda x: x[1])            # uses lambda to sort the points in the list

def sort_by_y(x):                                               # use function and lambda, long way, to sort the points in the list
    return x[1]
points2D_sorted2=sorted(points2D, key=sort_by_y)

print(points2D)
print(points2D_sorted)
print(points2D_sorted2)

points2D_sorted_2v=sorted(points2D, key=lambda x: x[0]+x[1])
print(points2D_sorted_2v)


#map(func, seq)   map function transforms each element with a function   
a=[1,2,3,4,5]                       # lambda function sintax
b=map(lambda x: x*4,a)
print(list(b))

c= [x*4 for x in a]                 #Another sintax without use map and lambda, same result
print(c)

#Filter: filter(func,seq)
a=[1,2,3,4,5,6]
b=filter(lambda x: x%2==0,a)
print(list(b))

c=[x for x in a if x%2==0]
print(c)

#Reduce(func,seq)                   #It applies in functions,repeteadly in values to return a single value, always two arguments
from functools import reduce
a=[1,2,3,4,5,6]
product_a=reduce(lambda x,y: x*y,a)
print(product_a)
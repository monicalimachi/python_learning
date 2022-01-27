#itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

#iterators used in a for loop

#product
from ast import operator
from itertools import combinations, product
from multiprocessing.sharedctypes import Value
a=[1,2]
b=[3,4]
prod=product(a,b)                      # combine both lists
print(list(prod))                     # to see elements convert to list
c=[3]
prod=product(a,c, repeat=2)
print(list(prod))

#permutations
from itertools import permutations
a=[1,2,3]
perm=permutations(a)                    # permute all fields combinations
perm1=permutations(a,2)                 # permute the values using only 2 fields
print(list(perm))
print(list(perm1))

#combinations
from itertools import combinations, combinations_with_replacement
a=[1,2,3,4]
comb=combinations(a,2)
print(list(comb))
comb_wr=combinations_with_replacement(a,2)              # send the list and the lenght 
print(list(comb_wr))

#accumulate functions
from itertools import accumulate
import operator
a=[1,2,5,3,4]
acc=accumulate(a)                                       # compute the sum from every field and accumulate it
print(a)
print(list(acc))
acc2=accumulate(a, func=operator.mul)
print(list(acc2))
acc2=accumulate(a, func=max)                            # compare and add the maxin the next fields
print(list(acc2))

#groupby
from itertools import groupby                           # returns keys and groups from an iterable
def smaller_than3(x):                                   # Function1
    return x<3
a=[1,2,3,4]
group_obj=groupby(a,key=smaller_than3)
for key, value in group_obj:
    print(key,list(value))

#Same exercise with lambda function                     # Function2: another way to group by the values accord some requisite
group_obj=groupby(a,key=lambda x:x<3)
for key, value in group_obj:
    print(key,list(value))

#groupby exercise2
persons=[{'name':'Tim','age':25},{'name':'Dan','age':25},
            {'name':'Lisa','age':27},{'name':'Claire','age':28}]

group_obj=groupby(persons,key=lambda x:x['age'])
for key,value in group_obj:
    print(key,list(value))

# itertools: infinite iterators-loops: count,cycle,repeat
from itertools import count,cycle,repeat

#count
for i in count(10):
    print(i)
    if i==15:
        break

#cycle 
a=[1,2,3]
j=0
for i in cycle(a):
    print(i)
    j+=1
    if j==15:
        break

# repeat
for i in repeat(1,4):                       # it will repeat eh value 1 , 4 times in this case
    print(i)
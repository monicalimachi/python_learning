def firstn(n):
    nums=[]
    num=0
    while num <n:
        nums.append(num)
        num+=1
    return nums
    
def firstn_generator(n):
    num=0
    while num<n:
        yield num
        num+=1

mylist=firstn(10)
print(mylist)

print(sum(firstn(10)))
print(sum(firstn_generator(10)))

import sys
print(sys.getsizeof(firstn(10000)))             #This uses more memory
print(sys.getsizeof(firstn_generator(10000)))   #This uses less memory
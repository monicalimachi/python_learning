import sys

my_list=[0,1,2,"hello",True]
my_tuple= (0,1,2,"hello","True")
print(sys.getsizeof(my_list),"bytes") #size is more
print(sys.getsizeof(my_tuple),"bytes") # size is less this is more recommended


import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) # take much longer to create a list
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)) # take less time to create a tuple
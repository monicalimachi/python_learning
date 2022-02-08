import random

a=random.uniform(1,10)
print(a)

a=random.randrange(1,10)    #Integer random values
print(a)

a= random.normalvariate(0,1)         #For normal and standard deviation
print(a)

#Using List with random chars
mylist=list("ABCDEFGH")
a=random.choice(mylist)
print(a)
a=random.sample(mylist,3)       #Will pick unique elements
print(a)
a=random.choices(mylist,k=3)    # can pick multiple times same elements
print(a)
random.shuffle(mylist)          # reorganize the list
print(mylist)


#Use seed random option
random.seed(1)                  #reproduce data <1
print(random.random())
print(random.randint(1,10))        #random numbers between 1 -10

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))
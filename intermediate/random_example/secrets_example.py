import secrets

a=secrets.randbelow(10)     #random int not include 10
print(a)

a=secrets.randbits(4)       #1010 it's 4 ways to generate random values
print(a)

mylist=list("ABCDEFGH")
a=secrets.choice(mylist)
print(a)
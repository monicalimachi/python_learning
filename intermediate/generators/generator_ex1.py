def mygenerator():
    yield 3
    yield 2
    yield 1

g=mygenerator()
print(g)

#Print all the yield values
""" for i in g:
    print(i) """

#Stop iteration until all yield created in this case 3 yields
""" value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
 """

#sort yield values
print(sorted(g))


#ANOTHER EXAMPLE
def countdown(num):
    print('Starting')
    while num >0:
        yield num
        num-=1

cd=countdown(4)

value=next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
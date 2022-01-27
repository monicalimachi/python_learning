#Sets: unordered, mutable, no duplicates

myset={1,2,3,1,2}
myset2=set("Hello")
myset3=set()        #to create  set empty, this is the correct form
print(myset)
print(myset2)
print(type(myset3))

myset3.add(1)
myset3.add(2)
myset3.add(3)
print(myset3)

""" myset3.remove(3)
#myset3.remove(4)  #wrong way to remove inexistent value
myset3.discard(4)  # if value is not found then nothing happens
myset3.clear()      # Empty the sets
print("Return Arbitrary values and empty set", myset.pop())         # return arbitrary value and remove set
print(myset)
print(myset3) """


for x in myset3:
    print(x)

if 1 in myset:
    print("yes")


odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}
u=odds.union(evens)                 #Calculate the union of two sets
print(u)
i=odds.intersection(primes)         #Calculate the intersection of two sets
print(i)


setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}
setC=set(setA)
diff1=setA.difference(setB)             # Returns all elements that are not in SetB
diff2=setB.difference(setA)             # Returns all elements that are not in setA
diff3=setB.symmetric_difference(setA) #Returns all elements that  are not in both sets
print(f"diff1: {diff1}")
print(f"diff2:{diff2}")
print(diff3)


setA.update(setB)
print(f"SetA updated:{setA}")           # Updates the setA adding the values from other set

setA.intersection_update(setB)          # Updates the set keeping only the elements found in both sets
print(setA)

setC.difference_update(setB)            # It updates the set by removing the values found in another set
print(setC)

setC.symmetric_difference_update(setB)  # it updates the set by only keeping the elements in both sets, but not the elements found in both sets
print(setC)

setD={1,2,3,4,5,6}
setE={1,2,3}
setF={7,8}
print(setD.issubset(setE))              # All elements from first setD set are in second set setE > False (in the example)
print(setD.issuperset(setE))            # All elements from setD contains all the numbers from the second set setE >> True
print(setD.isdisjoint(setF))            # Elements from both sets are different >> True

setX={1,2,3,4,5,6}
setY=setX.copy()
setY.add(7)
print(setY , setX)

a=frozenset([1,2,3,4])                  # Immutable version of normal set, can't change after creation, add,removes doesn't work
a.remove(1)
#print(a)                                # Error if tryes to modify set
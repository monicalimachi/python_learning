# Dictionary: Key-Value pairs , Unordered, Mutable

mydict={"name":"Max" , "age":28,"city":"New York"}
print(mydict)

""" value= mydict["age"]    # Use key to point to the Value
print(value)

mydict["email"]="max@xyz.com"   # can be possible add a new key-value
print(mydict)

mydict["email"]="coolmax@xyz.com"
print(mydict)

del mydict["name"]      # delete specific key - value
print(mydict)

mydict.pop("age")       # delete specific key- value other way
print(mydict)

mydict.popitem()        # delete last key-value
print(mydict)
 """
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["age"])
except:
    print("Error")

for key in mydict.keys():
    print(key)
for values in mydict.values():
    print(values)

for x in mydict:
    print(x,mydict[x])

mydict_cpy=mydict           # it creates both dicitionaries are pointing to same values in memory, same changes
mydict2_cpy=dict(mydict)    # in this way it creates a new dictionary with same values of old dictionary, old dictionary is not affected
print(f"Original dictionary{mydict_cpy}")
mydict_cpy["email"]="max@xyz.com"
print(mydict_cpy)
print(mydict)    
print(mydict2_cpy)        


mydict={"name":"Max" , "age":28,"email":"max@xyz.com"}
mydict_2={"name":"Mary" , "age":27,"city":"Boston"}
mydict.update(mydict_2)     # All the existing key-values are overwritten and added to mydict 
print(mydict)


mydict = {3:9,6:36,9:81}
value=mydict[9]
print(value)
mytuple=(8,7)
mydict={mytuple:15}
print(mydict)


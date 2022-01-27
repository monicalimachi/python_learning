# Tuple: ordered, immutable, allows duplicate elements
my_tuple=("Max",)
tuple2=tuple(["Max",28,"Boston"])
print(type(my_tuple))
print(tuple2[2])
print(tuple2[-2])
for i in tuple2:
    print(f"print all tuple {i}")


tuple3=('a','p','p','l','e')
print(tuple3.index('e'))
my_list=list(tuple3)
print(my_list)
tuple3_2=tuple(my_list)
print(tuple3_2)


a=(1,2,3,4,5,6,7,8,9,10)
b=a[:5]
c=a[::-2]
print(b,c)

my_tuple="Max",28,"Boston"
name,age,city=my_tuple
print(f"This is the option to save every value in every variable matching the same Qty: Name {name} with {age} in the city {city}")

my_tuple=(0,1,2,3,4)
i1,*i2,i3=my_tuple #All numbersin between are added with * in *i2
print(f"printing values i1= {i1}, i2= {i2} and i3= {i3}")


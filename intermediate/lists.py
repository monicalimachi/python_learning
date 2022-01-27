#Lists: ordered,mutable,allows duplicate elements
my_list=["banana","cherry","apple"]
print(my_list)

my_list2=[5,True,"apple","apple"]
print(my_list2)

item=my_list[0]
print(item)
print(len(my_list2))
my_list2.append("lemon")
print(my_list2)
item=my_list.pop()
print(f"This is the item >>> {item}")

my_nlist=[-4,-8,0,4,7,100,-68]
my_nlist2=my_nlist
print(my_nlist)
my_nlist2.sort()
print(f"Original list2 sorted using .sort only can be sorted itself {my_nlist2}")
item2=sorted(my_nlist)
print(f"Results saved using other list, using sorted returns this values: {item2}")

item_zeros=[0]*5
print(item_zeros)
new_list=my_nlist+item_zeros
print(new_list)

my_list=[1,2,3,4,5,6,7,8,9]
a=my_list[1:9] 
b=my_list[:7]
c=my_list[::2]
d=my_list[::-1]
print(f"Print the list from index 1 to 9 {a}")
print(f"Print list from  the beginning to index position 7 : {b}")
print(f"Print list every 2 indexs : {c}")
print(f"Print list inverse : {d}")


list_orig=["banana","cherry","apple"]
list_cp2=list_orig      #both lists will have same values always, even after modify them
list_cp=list_orig.copy() # to copy values to list_cp
list_orig.append("pineapple")
print(list_orig,list_cp,list_cp2)


origen=[1,2,3,4,5,6]
b=[i*i for i in origen]     #Create second list with expression using first list origen
print(origen)
print(b)


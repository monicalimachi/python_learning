#LISTS
""" lucky_numbers=[47,8,15,16,23,42]
friends=["Kevin","KAren","Jim","Jim","Oscar","Toby"]
friends.append("Creed")
friends.insert(1,"Kelly")
#friends.remove("Jim")
friends.pop()  #Remove last value from the list
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2=friends.copy()
print(friends2) """

#SETS
my_set={"January","February","March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)

#TUPLES == Tuples values can't change
""" coordinates=[(4,5),(6,7),(8,9)]
coordinates[1]=10,11
print(coordinates[0])
print(coordinates[1])
print(coordinates)  """


#FUNCTIONS
""" def say_hi():
    print("Hello user")

print("Top")
say_hi()
print("Bottom")


def say_hi2(name):
    print("Hello " + name)
    print(f"Hello {name} this is a test")
    print(f"This is a test {3*6*3}")

say_hi2("Mike")
say_hi2("Peter") """

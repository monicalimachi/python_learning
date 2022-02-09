#Int vlues can modify the values from copies and original values
org = 5
cpy = org

cpy = 6

print(cpy)
print(org)

#In lists the values are the same, the value on [0] was applied to copy and org
org = [0,1,2,3,4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

#Do a shallow copy , originl was not affected only copy
import copy
org = [0,1,2,3,4]
cpy = copy.copy(org)
#cpy = org.copy()           #All of this options works well to copy when it's only one level copy
#cpy = list(org)
#cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

#Nested list - deep copying for more levels
#import copy
org = [[0,1,2,3,4],[5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

#for dcts or lists, tuples, custom objects can also be used /shallow copy
#import copy

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

p1 = Person('Alex',27)
p2 = copy.copy(p1)

p2.age = 28

print(p2.age)
print(p1.age)

#For deep structures, add to class Person the class Company

class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.name,company_clone.boss.age)
print(company.boss.name,company.boss.age)
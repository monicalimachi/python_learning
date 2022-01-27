# collections: Counter , namedtuple, OrderedDict, defaultDict, deque

#Counter -  # counter dictionary values
from collections import Counter    

a= "aaaaabbbbccc"
my_counter=Counter(a)
print(my_counter.values())      # show all values
print(my_counter.items())       # show all key,values >> items
print(my_counter.most_common(2)[1][0]) ## show most common 2 items where the index 1 shows only the key (position0) 
print(list(my_counter.elements()))  #Get all the different elements as a list

# namedtuple 
from collections import namedtuple
Point=namedtuple('Point','x,y')         #Create a class point with two fields
pt=Point(1,-4)
print(pt.x,pt.y)                        # Can get the coordinates, values for x,y

# OrderedDict
from collections import OrderedDict     # REgular dictionary with ordered
ordered_dict=OrderedDict()              # Remember the order of the values introduced
ordered_dict['b']=3
ordered_dict['a']=2
ordered_dict['d']=5
ordered_dict['c']=4
print(ordered_dict)

# defaultdict
from collections import defaultdict         # It will have a default value
d=defaultdict(int)                          # in this case the default value for an int it's 0 .... also check(bool, float,list, {}) {} is default dict
d['a'] =1
d['b']=2
print(d['c'])

# deque
from collections import deque               # add or remove elements from bot ends
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)                             # add in the left side
d.appendleft(4)                         
d.popleft()                                 # remove in the left side
d.clear()                                   # remove all elements from deque
d.extend([4,5,6])                            # add , extend elementd at the rightside
d.extendleft([7,8,9])                          # add, extend elements at the leftside
print(d)
d.rotate(2)
d.rotate(-3)                                    # rotate to the left
print(d)




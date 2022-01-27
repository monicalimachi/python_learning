#Strings: ordered, immutable, text representation

my_string="Hello World"
my_string2="""Hello \ 
World"""
print(my_string, my_string2)
char = my_string2[-2]
print(char)

substring=my_string[1:5]            #From 1 until 5, not include index 5
substr2=my_string[::1]              # Takes every char
substr3=my_string[::2]              # Takes every second char
substr4=my_string[::-1]             #Invert values
print(substring)
print(substr2, substr3, substr4)

greeting= "Hello"
name="Tom"
sentence=greeting + "   " + name
print(sentence)

for i in greeting:
    print(i)

if 'ell' in greeting:
    print('yes')
else:
    print('no')

my_string='     Hello World     '
my_string=my_string.strip()                 #Remove the spaces in the field in the sides, need to assign again to the original string to run this option
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('World'))        # REview if char starts with some word, char >> false in this case
print(my_string.find('o'))                  # Returns the first index found in the char >> Return -1 if it's found
print(my_string.count("o"))                 # Returns qty of words
print(my_string.replace('World',"Universe"))    #REplace characters , the substring of the string, in this case Universe , if the value World is not found then nothing is replaced


my_string='How are you doing'               
my_list=my_string.split(" ")                # list is created with the elemenets from previous string, separated by space
print(my_list)

new_string=' '.join(my_list)                # Join elements of a list back to a string
print(new_string)

my_list1=['a']*10000
#print(my_list1)

#Bad method
my_string=''
for i in my_list1:
    my_string+=i
#print(my_string)

#Recommended - Good method
my_string=''.join(my_list1)
#print(my_string)

#Review the time both methos takes
from timeit import default_timer as timer

start=timer()
#Bad
my_string=''
for i in my_list1:
    my_string+=i
stop=timer()
print(stop - start)

#Good                           # join method is the best way, for the time, response
start=timer()
my_string=''.join(my_list1)
stop=timer()
print(stop - start)


# %, .format(), f-Strings
var="Tom"
my_string="the variable is %s"%var      # %s is for placeholder with a string variable
print(my_string)

var =3.123
my_nstring="the variable is %d" % var   # %d is for placeholder with a number, int and decimal value shows as int
my_fstring="the variable is %f" % var 
print(my_nstring, " " ,my_fstring)
my_fstring="the variable is %.2f" % var     # the float will show two digits %.2f
print(my_fstring)

#.format()
var=3.122
var2=6
my_string="the variable is {:.3f} and {}".format(var,var2)
print(my_string)

# NEW FORMAT STYLE: f-Strings since python 3.6
my_string2=f"In the updated python: the variable is {var} and {var2}"
print(my_string2)

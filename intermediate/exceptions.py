#Errors and Exceptions
#a =5 print(a)       # Error for syntaxError, parentesis, enters, spaces
#a=5+'10'               # Type Error, int with string
#import somemodulexyz    #Module errors, when it doesn't exist
#a=c                    # NameError, c variable doesn't exist
#f=open('somefile.txt')  #FileError not found

""" a=[1,2,3]               #ValueError, the value doesn't exist, x not in list
#a.remove(4)
print(a)
#or
a[4]
print(a)                # IndexError, list index out of range """

#my_dict={'name':'Max'}  
#my_dict['age']          # Key Error whe the key doesn't exist


""" x=-5
if x<0:
    raise Exception('x should be positive')         # add exceptions messages """

#Other way add assert statement                     # also can be added the assertion to validate value
#x=-5                    
#assert(x>=0),'x is not positive'

# try exceptions                                    # display a  message
""" try:
    a=5/0
except:
    print('an error happened') """

# catch the exception                           #Catch the exception for this case
""" try:
    a=5/0
except Exception as e:                              # General exception: division by zero
     print(e) """

#CAtch exceptions accord the type
""" try:
    a=5/1
    b=a + 4

except ZeroDivisionError as e:                      # TypeError: Division by Zero
    print(e)
except TypeError as e:                              # TypeError: Unsupported mixed types float , str, int
    print(e)
else:
    print('everything is fine')
finally:
    print ('cleaning up...') """


#Class exception - Add exceptions in  using classes and functions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value


def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)



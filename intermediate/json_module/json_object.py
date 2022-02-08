from email.policy import default
from html.entities import name2codepoint
import json

class User:

    def __init__(self,name,age):
        self.name=name
        self.age=age

user = User('Max',27)

#Create a custom function to encode User data into json format
def encode_user(o):
    if isinstance(o,User):
        return{'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON=json.dumps(user,default=encode_user)
print(userJSON)

#Another way to encode json data
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o,User):
            return{'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)


userJSON=UserEncoder().encode(user)
print(userJSON)

#To decode dictionary
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name,user.age)

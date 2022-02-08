import json

person={"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineer","programmer"]}

#personJSON=json.dumps(person, indent=4,separators=(';','='))

personJSON=json.dumps(person, indent=4, sort_keys=True) #Better use sortKeys to sort alphabetically

print(personJSON)


# To write and save the json data into a file
with open('json_module/person.json','w') as file:               
    json.dump(person,file, indent=4)

#Move from json format into a python format - dictionary 
person=json.loads(personJSON)
print(person)

#Open from json file with python format - data in dictionary
with open('json_module/person.json','r') as file:
    person = json.load(file)
    print(person)
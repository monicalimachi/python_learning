#FUNCTION1: DAYS_TO_HOURS
""" calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}") #Always  the input comes as String, need to convert the numbers

my_var=days_to_units(20)
user_input=input("Hey user, enter a number of days and I will convert it to hours!\n")
print(user_input) """



#FUNCTION2: ADD INPUTS

""" calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")

user_input=input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number=int(user_input)
calculated_value=days_to_units(user_input_number)
print(calculated_value) """



#FUNCTION3: CONDITIONALS

""" calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
   # condition_check=num_of_days>0
   # print(type(condition_check))
        return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")


def validate_and_execute():
    try:  
        user_input_number=int(user_input)
        if user_input_number > 0:
            calculated_value=days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number==0:
            print("You entered a 0, please enter a positive number")    
        else:
            print("you entered a negative number, no convertion for you!")

    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input=input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()
 """

 #FUNCTION4: WHILE LOOPS - LISTS
""" calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
   # condition_check=num_of_days>0
   # print(type(condition_check))
        return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")


def validate_and_execute():
    try:  
        user_input_number=int(num_of_days_element)
        if user_input_number > 0:
            calculated_value=days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number==0:
            print("You entered a 0, please enter a positive number")    
        else:
            print("you entered a negative number, no convertion for you!")

    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input=""
while user_input!="exit":
    user_input=input("Hey user, enter a number of days as a comma separated list and I will convert it to hours!\n")
    print(type(user_input.split()))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(","): #split return a list 
        validate_and_execute() """



####       FUNCTION5   -   LOOPS   -   SET
""" calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
   # condition_check=num_of_days>0
   # print(type(condition_check))
        return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")


def validate_and_execute():
    try:  
        user_input_number=int(num_of_days_element)
        if user_input_number > 0:
            calculated_value=days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number==0:
            print("You entered a 0, please enter a positive number")    
        else:
            print("you entered a negative number, no convertion for you!")

    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input=""
while user_input!="exit":
    user_input=input("Hey user, enter a number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days=user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(user_input.split(",")): #split return a list and set remove duplicated values inside the list
        validate_and_execute() """

       
#####     FUNCTION6   -   DICTIONARY
""" 
def days_to_units(num_of_days,conversion_unit):                 ## This code is moved to helper.py
    if conversion_unit=="hours":
        return(f"{num_of_days} days are {num_of_days * 24} hours")
    elif conversion_unit =="minutes":
        return(f"{num_of_days} days are {num_of_days*24*60} minutes")
    else:
        return "Unsupported units!!"

def validate_and_execute():
    try:  
        user_input_number=int(days_and_unit_dictionary["days"]) #Use de Key to enter to days in dictionary
        if user_input_number > 0:
            calculated_value=days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number==0:
            print("You entered a 0, please enter a positive number")    
        else:
            print("you entered a negative number, no convertion for you!")
    except ValueError:
        print("Your input is not a number, don't ruin my program") """

""" user_input=""                                             ## This code is moved to main.py
while user_input!="exit":
    user_input=input("Hey user, enter a number of days and conversion unit!\n")
    days_and_unit=user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute() """


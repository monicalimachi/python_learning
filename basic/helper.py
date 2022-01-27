


def days_to_units(num_of_days,conversion_unit):
    if conversion_unit=="hours":
        return(f"{num_of_days} days are {num_of_days * 24} hours")
    elif conversion_unit =="minutes":
        return(f"{num_of_days} days are {num_of_days*24*60} minutes")
    else:
        return "Unsupported units!!"

def validate_and_execute(days_and_unit_dictionary):
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
        print("Your input is not a number, don't ruin my program")

user_input_message="Hey user, enter a number of days and conversion unit!\n"
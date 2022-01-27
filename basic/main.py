from asyncio.log import logger
#from helper import validate_and_execute, user_input_message     #Import values from module, don't need to add names of module , the * import everything

#import helper  as h     #Import module then we need to agregate the names of the module into the functions
import logging
logger=logging.getLogger("MAIN")
logger.error("Error happened in the app")

""" user_input=""
while user_input!="exit":
    user_input=input(user_input_message)
    days_and_unit=user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary) """
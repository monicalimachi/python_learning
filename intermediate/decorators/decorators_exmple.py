
from curses import wrapper
from unittest import result


def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


#USING FUNCTIONS WITHOUT DECORATOR
""" def print_name():
    print('Alex new command to test')

print_name=start_end_decorator(print_name)
print_name() """


# NOW USING DECORATOR
@start_end_decorator
def print_name():
    print('Alex')
print_name()


#Add Decorator with parameter
def decorator_with_parameter(func):
    def wrapper(*args,**kwargs):
        print('Start')
        result = func(*args,**kwargs)
        print('End')
        return result
    return wrapper

@decorator_with_parameter
def added_5(x):
    return x+5

result=added_5(10)
print(result)
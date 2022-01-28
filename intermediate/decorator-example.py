""" def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Luisa')

print_name=start_end_decorator(print_name)

print_name()


#Same example adding decorator
def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Luisa')

print_name() """


#Decorator using kwarks
from unittest import result


def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result=func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

result = add5(10)
print(result)
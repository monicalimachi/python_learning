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






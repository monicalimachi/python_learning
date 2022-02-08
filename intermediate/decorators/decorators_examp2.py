import functools

#Create decorator with functools - template for any decorator preserving information

# Decorator with parameter
def decorator_with_parameter(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #Do something before
        print('Start')
        result = func(*args,**kwargs)
        #Do something after
        print('End')
        return result
    return wrapper

@decorator_with_parameter
def added_5(x):
    return x+5

result=added_5(10)
print(result)

print(help(added_5))
print(added_5.__name__)



#Execute the number times some function with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')




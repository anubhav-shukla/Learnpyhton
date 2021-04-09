# print_function_data
from functools import wraps

def print_func_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"You are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper    

@print_func_data
def add(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b
print(add(4,5))
# output
# You are calling add function
# This function takes two numbers as parametre and return their sum

# 9

# Now hope it is clear
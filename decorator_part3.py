from functools import wraps 
def decorator_f(any):
    def wrapper_f(*args,**kwargs):
        '''this is a wrapper function'''
        print('This is a  awesome function')
        return any(*args,**kwargs)
    return wrapper_f


@decorator_f
def add(a,b):
    '''this is add function'''
    return a+b
print(add.__doc__)
print(add.__name__)
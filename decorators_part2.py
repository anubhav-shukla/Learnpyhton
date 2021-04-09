def decorator_f(any):
    def wrapper_f(*args,**kwargs):
        print('This is a  awesome function')
        return any(*args,**kwargs)
    return wrapper_f

@decorator_f
def func(a):
    print(f'this is function {a}')

func(7)    

@decorator_f
def add(a,b):
    return a+b
print(add(2,4))
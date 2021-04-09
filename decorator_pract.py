def add_all(*args):
    total=0
    for i in args:
        total += i
    return total
# print(add_all(1,2,3,4,5,[1,2,3]))    #it gives error

from functools import wraps
def only_int9(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return fun(*args,**kwargs)
        print("Invalid arguments")

        # data_types=[]
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function (*args,**kwargs)    
        # else:
        #     print("invalid arguments")
    return wrapper           

@only_int9
def add_all(*args):
    total=0
    for i in args:
        total += i
    return total    
print(add_all(1,2,3,4,5))   
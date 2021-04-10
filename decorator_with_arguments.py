from functools import wraps
def only_data_type(data_type):
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args,**kwargs):
            if all([type(arg)== data_type for arg in args]):
                return fun(*args,**kwargs)
            print("Invalid argument")
        return wrapper
    return decorator
@only_data_type(str)
def string_join(*args):
    string=''
    for i in args:
        string +=i
    return string

print(string_join('Anubhav','Shukla'))                    

# exercise
from functools import wraps
import time

def calculate_time(func):
    @wraps(func)
    def wrap(*args,**kwargs):
     print(f'Executing ......{func.__name__}')
     t1=time.time()
     func(*args , **kwargs)
     returned=func(*args,**kwargs)
     t2=time.time()
     total=t2-t1
     print (f'This function takes{total} sec to run') 
     return returned
    return wrap    

@calculate_time
# t=time.time()
def funcl():
        print("this is function")
funcl()        
# t1=time.time()
# print(t1-t)      
# this func takes 3 sec to run
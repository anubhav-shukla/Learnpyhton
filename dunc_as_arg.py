# sorry not dunc 
# it is function
# def square(a):
#     return a**2

# map
l=[1,2,3,4]
sq=map(lambda a:a**2,l)
print(list(sq)) #you get the output

# today make a function that take as a input a function\\

def my_map(func,l):
    new_list=[]
    for item in l:
       new_list.append(func(item))
    return new_list

print(my_map(lambda a:a**3,l))#Hope now you able to do it...ArithmeticError
# /now you make  a func like map
# Hope it help you
   
# cAN we do it with list comprehension

def map_fun2(func,l):
    return [func(item) for item in l]
print(map_fun2(lambda a:a**3,l))    

# here we variable scope in function inside and outside
# python func_scope.py
x=5 # global  variable we can change this value inside function see
def func():
    global x  #now you get  result as same
    x=7 #local variable
    return x

    #Before calling function value is global after call change in func() 
print(x) # output is 5
print(func()) # it show result 7 because we call func()
# print(x) it show  a error because it not access out side the scope
print(x) # it show result is 5

# Now I hope it clear about local variable and global variable
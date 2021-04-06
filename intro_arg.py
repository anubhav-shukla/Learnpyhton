# make flexible function

# *operator
# *args

# why we need  it

def total(a,b):
    return a+b

# print(total(3,4,5,7))#it give error

# but we can solve it using * operator

def all_total(*args): #according to convetion we use args
    print(args)
    print(type(args))
all_total(1,2,3,4,4,5,6)    
# 1st it create tuple

# make a function that total all numbers
def all_total_num(*args):
    total=0
    for num in args:
        total += num
    return total

print(all_total_num(1,2,3,4,5,6))        

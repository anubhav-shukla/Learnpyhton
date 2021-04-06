# here we define a list take input from user for square ,quibic and more
i=int(input("Enter a number :  "))
def to_power(l,*args):
    lis=[]
    for i in args:
        lis.append(i**l)
    return lis 
nums=[2,3,4]
# print(to_power(i,*nums))     # it is a normal form

def power_t(l,*args):
    if args:
        return [i**l for i in args]
    else:
        return"You didn't pass aby args"    
print(power_t(i,*nums))    



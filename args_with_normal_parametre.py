# *args with normal parametre

def multiply_nums(num,*args):
    multiply=1
    print(num) #1
    print(args) #(2,3,4)
    for i in args:
        multiply *=i
    return multiply
print(multiply_nums(1,2,3,4))    
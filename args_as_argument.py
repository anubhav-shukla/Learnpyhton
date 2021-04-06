# when define function than it is called parametre
# when we call define funtion thanit call argument
def multiply_nums(*args):
    multiply =1
    print(args) #([2,3,4])
    for i in args:
        multiply *=i
    return multiply

nums =[2,3,4]
print(multiply_nums(*nums))#using * it unpack the list ,dictionary or tuple


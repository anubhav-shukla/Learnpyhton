# here we  see a function inside a function
def greater(a,b):
    if a>b:
        return a
    else:
        return b
         # it is function that we are use to make another function
def greatest(a,b,c):
    # bigger=greater(a,b)
    return greater( greater(a,b),c) # for optimization purpose use  py programmer

print(greatest(10,22,33))

#it is an example of funnction inside a function  


# python function_in_func.py

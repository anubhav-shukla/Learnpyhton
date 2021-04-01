# chapter7 cube of element
# python chapter7_exe1.py
# x*x*x

def cube_find(x):
    d1={}
    for i in range(1,x+1):
         d1[i] =i**3
    return d1

print(cube_find(3))




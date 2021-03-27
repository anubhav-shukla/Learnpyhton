# python func_return_2_value.py

def two_valure(m ,n):
    add=m+n
    multiply = m*n
    return multiply,add
# print(two_valure(2,3)) #6multiply,5add
multiply ,add = two_valure(2,3)
print(multiply)
print(add)



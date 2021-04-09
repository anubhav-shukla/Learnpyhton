# You have to have a complete understannding of functions
# first class function / closures
# then finally we will learn about decorator


def square(a):
    return a**2
print(square(7))    

s=square #you not call function here
# now you can use s as a function

print(s(7)) #same output

# verify it 

print(s.__name__)
print(square.__name__)
print(s)
print(square)#see both are on same locatin





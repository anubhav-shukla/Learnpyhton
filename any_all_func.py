# any , all function

number1=[2,4,6,8,10]
number2=[1,3,5,7]
evens1=[]
for num in number2:
    evens1.append(num%2==0)
print(evens1)    

# Now we use all function

print(all([True, False, True, True, True])) #when all true , it returns true
# return False



# Now we use list comprehension'
print(all([num%2==0 for num in number1])) #true

# do same for number2
print(all([num%2==0 for num in number2])) #False


# Now see any Function


print(any ([num%2==0 for num in number1])) #true

print(any([num%2==0 for num in number2]))#false


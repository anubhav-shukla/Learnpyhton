# filter function

def ie_even(a):
    return a%2==0
numbers=[2,3,34,4,5,5,6,77,8]

# print(filter(ie_even,numbers)) #it return a  object

print(list(filter(ie_even,numbers))) #now you got the output

# now we use lambda expression to solve same problem
print(list(filter(lambda a:a%2==0,numbers)))#you get the same output

evens=filter(lambda a:a%2==0,numbers)#you get the same output
# you can iterate it only one time


for i in evens:
    print(i) 
    
for i in evens:
    print(i) #it has no validation 

    # if we convert it into tuple or  list than iterate it multiple time

evens=tuple(filter(lambda a:a%2==0,numbers))#you get the same output
for i in evens:
    print(i) 
for i in evens:
    print(i) 
for i in evens:
    print(i) 
# Now you can iterate it multiple times


# You can't iterate map and filter more than one time



# you think you can do it with list comprehension
# yes you can do it

new_evens=[i for i in numbers if i%2==0]
print(evens)
print(new_evens)
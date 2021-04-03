# most powerful topic in python
# list comprehension

# python list_comprehension.py

# today we create a list with the help o list comprehension

# create a list of squares from 1 to 10

# it is a simple way to create  a list square

# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)    


# Now we see using list comprehension

# square2=[i**2 for i in range(1,11)]
# print(square2) # result is same hope it clear


# create a list of negative number 

# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative) # you got a negative list

# #  now see list comprehendion

# negative2=[-i for i in range(1,11)]
# print(negative2) #result is same  hope it now clear in your mind

# see something unique

names=['Anubhav','Golu','Snaghrs']
new_list=[] #form upper list first character store in new_list
for name in names:
      new_list.append(name[0])
print(new_list)      

# now see using list comprehension

name2=[name[0] for name in names]
print(name2)
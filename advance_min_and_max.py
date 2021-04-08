# advance min() and max()

# numbers =[1,2,3,4,5,7]
# print(min(numbers)) #1 is result

# def fun(item):
#     return len(item) #now you can use lambda expression

name=['Anubhav','Golu','Ashish']
print(max(name,key=lambda item:len(item)))#this is way to print max

print(min(name,key=lambda item:len(item)))#this is way to print min


# here we make a list and a dictionary

students1={
    'Anubhav':{'score':95,'age':24},
    'Golu':{'score':98,'age':15},
    'Ashish':{'score':92,'age':19}
}

students2=[
    {'name':'Anubhav','score':99,'age':24},
    {'name':'Golu','score':98,'age':15},
    {'name':'Ashish','score':92,'age':19}
]

print(max(students2,key=lambda item:item.get('score'))['name'])
# hope you understand it

# now we calculate max from student1

print(max(students1,key=lambda item:students1[item]['score']))
# it is important hope it clear

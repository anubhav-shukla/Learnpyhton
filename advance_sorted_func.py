# here we understand about advance sorted function

fruits=['grapes','mango','apple']
# sort
fruits.sort()
print(fruits) #see your list is sorted 

# But sort method is  only available in list

fruits1=('grapes','mango','apple')
# if you use sort in it than you get error

# you can use sorted
print(sorted(fruits1))  #it is make a list and than sort it  
print(fruits1)#it is not changed because tuple is immutable

fruits2={'grapes','mango','apple'}
# same in the set
print(sorted(fruits2)) #it make a new list and than sort it

print(fruits2) #it has no order

# See an real life example

guitars=[
    {'model':'Yamaha f310','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor 814ce','price':450000},
]

print(sorted(guitars,key= lambda d:d['price'],reverse=True))
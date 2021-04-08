# map Function

numbers =[1,2,3,4]

def square(a):
    return a**2
# {square(1),square(2),square(3)} it is a manual way

# do it by using map_func

squares=list(map(square,numbers))
print(squares)

# we can do same using list comorehension

squares_new=[i**2 for i in numbers]
print(squares_new)
# you got the same result


# you can  do same using lambda function
# without define map_func

squares=list(map(lambda a:a**2,numbers))
print(squares)
# get the same output by using it


# without list comprehension and map function

new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)    
# got the same output 

# we use map and  list comprehension for make small code

names=['abc','abcd','abcde']
length=map(len,names)
for i in length:
    print(i) #now you get the length of string in list
# for i in length:
#     print(j)  #run loop only one time in map

print(length)
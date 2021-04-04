# list coprehension with if statement

numbers=list(range(1,11))
print(numbers)

# even_nums=[2,4,6]

# num=[]
# for i in numbers:
#     if i%2==0:
#         num.append(i)
# print(num)        


# now see how  can we use if in list comprehension

even_num=[i for i in numbers if i%2==0]
print(even_num) #it's output is same  as above

# we can do same  work without making a list of numbers
even_num2=[i for i in range(1,11) if i%2==0]
print(even_num2) #work is same as before

#  now  see how can we found odd  numbers

odd_num=[i for i in range(1,11) if i%2 != 0]

print(odd_num)
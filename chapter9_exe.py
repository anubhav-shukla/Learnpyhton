# define a function that take list of strings
# list containing  reverse of every string

# eample 
# l=['abc','tuv','xyz']
# reverse_string(l) ------> ['bac','vut','zyx']

l=['abc','tuv','xyz']

# def reverse(l):
#     store=[]
#     for i in l:
#         store.append(i[::-1])
#     return store
# print(reverse(l))  


# now we see using list comprehension

def reverse_Str(l):
    return[i[::-1] for i in l]
print(reverse_Str(l))    

# getting same output

# hope now it is clear
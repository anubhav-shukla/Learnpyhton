# python more_about_tuple.py

#  use for or while in tuple:
mix=('name','fame','money','grown',2,3,5,[6,7,8,'number'])
# for i in mix:
    # print(i) #here it print everything that available in list

# single element tuple
# m=(1,) # use , for making tuple is important
# print(type(m))  # it is tuple 

    #tuple without parenthesis
color='red','blue','orange','black'   
# print(type(color)) # it is tuple without parenthesis
# unnpacking in tuple
i,j,k,l=color
print(i)
print(j)
print(k)
print(l)
# if you miss an variable i j k than it gives error
# careful

# list inside tuple

number=(1,2,3,[3,4,5])
# here [3,4,5] is a list
# now you can perform any operatio of list

l=number[3].pop()
print(l) # 5 it popped

m=number[3].append(11)
print(number) # see 11 is added in list

# some methods min() max() sum()

table=(11,222,333,44,55)
print(max(table))#333
print(min(table))#11
print(sum(11))



# zip()2

l1=[1,2,3,4]
l2=[2,4,5,7]
# In part 1 we understand how can we combine list and make tuple

# But in part2 we understand how to make list from tuple input

# l=[(1,2),(2,4),(3,5),(4,7)]

# using * first we unpack list

# l1,l2=list(zip(*l))
# print(list(l1))
# print(list(l2))

# Now you able to do it..


# what more do with zip ()
new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)



# You can do it with multiple way but it one of those




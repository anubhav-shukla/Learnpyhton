# today we learn set 
# data type
# unordered collection of unique items

# python set_intro.py
s={1,2,3,2} #it holds only unique items

print(s) #output is {1,2,3}

# unordered 
# print(s[1]) #it shows error 
# in set we not do indexing

# why learn set?
l=[1,2,3,4,555,6,66,6,7,8,9,5,5,5]
# for remove duplicacy
s2=set(l)
print(s2)
# output:
#      {1, 2, 3, 4, 66, 6, 7, 8, 9, 5, 555}
# ********after remove duplicacy you can convert in list and use it
print(list(s2))
# ************it is a great purpose to use set


# methods of set
# add()
s.add(4)
print(s) #{1, 2, 3, 4}

# if i want readd it in set 
s.add(4)
print(s) #result  remain same

# remove()

s.remove(4)
print(s) #it remove element {1,2,3}

# discard()
s.discard(4) #it not in my set
print(s) #it not give  error print same

# clear()
# s.clear()
# print(s) #output set()

# copy()
s1=s.copy()
print(s1) #make new set {1,2,3}

# you can store anything in set like string , number 

s1.add("string")
print(s1) # it add string in set

# *** you can't add list and  dictionary in set

# Hope  now all concepts are clear

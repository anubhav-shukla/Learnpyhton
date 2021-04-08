# zip function
user_id=['user1','user2','user3']
names=['Anubhav','mohit','rohit']

# it gives zip object as a tuple

# ('user1','Anubhav'),('user2','mohit')

print(list(zip(user_id,names))) #now you get expected output


# second condition

user_id1=['user1','user2']
names1=['Anubhav','mohit','rohit']
print(list(zip(user_id1,names1))) #only gives two tuple as output

# you can convert it in dictionary
example=[('a',1),('b',2)]
print(dict(example))

# zip only work with two list ?
# no , it can work with multiple list
last_name=['Shukla','Kumar','kumar']
print(list(zip(user_id,names,last_name))) #you combine all list

# hope now you understand the power of zip

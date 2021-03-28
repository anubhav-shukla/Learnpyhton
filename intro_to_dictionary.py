# today we learn  about dictionary 
#  dictionary is a data structure
# python intro_to_dictionary.py
# what are dictionaries?
# unordered collections of data in keyb : value pair.

# how we can  create  dictionary
user={'name' : 'Anubhav','age':24}
# .print(user)
# print(type(user))

# Second method to create a dictionary
user1= dict(name="Anubhav",age="22")
print(user1)

# we can't access data by index

# how to access data from dictionary
print(user['name'])

# which type of data a dictionary can store?
# anything
# numbers , Strings , list , dictionary

user_info={
    'name':'Anubhav',
    'age'  :'22',
    'fav_movie':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale']
    } 

print(user_info['fav_movie'])  

# you can store complex data in dictionary

user_info2={}
user_info2['name']='Anubhav'
print(user_info2)
user_info2['age']=22
print(user_info2)

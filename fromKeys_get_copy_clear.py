# formkey use  for creating dictonary
# k={'name':'unknown','age':'unknown'}
# python fromKeys_get_copy_clear.py

# like list
# L=dict.fromkeys(['name','age','height','length'],'unknown')
# print(L)
# if we make it list {'name': 'unknown', 'age': 'unknown', 'hright': 'unknown', 'length': 'unknown'}

# make it tuple output is same

# L=dict.fromkeys(('name','age','hright','length'),'unknown')
# print(L)
# if we make it list {'name': 'unknown', 'age': 'unknown', 'hright': 'unknown', 'length': 'unknown'}

# we can make string
# L=dict.fromkeys("abc",'unknown')
# print(L)

# output is like it 
        #    {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

# here we use and show you range()
# L=dict.fromkeys(range(1,11),'unknown')
# print(L)

# output:{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8:'unknown', 9: 'unknown', 10: 'unknown'}


# we can create aa tuple for dict

L=dict.fromkeys(['name','age'],['unknown','unknown'])
print(L)

# result is like this :
          # {'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}     

# ***** Now we see a get method

K={'name':'Anubhav','age':22}
print(K.get('name'))#better

#  see an example to use it
if K.get('name'):
    print('present')
else:
    print('not present')    
# output is  present 

# ***** Now we see clear()

# it clear your dictionary
# K.clear()
# print(K)
# output = {} 
# means empty

# ************** now we learn how  to use copy()

d1=K.copy() #use copy() it make a new dictionary
print(d1)
  
# if we do here poppeditem result
print(d1.popitem())#('age', 22)
print(K) #{'name': 'Anubhav', 'age': 22}    
# no chage  in the dict 


# but  if we assign =
d2=K
print(d2) #give same output 
# if we pop something from d2 
print(d2.popitem()) #('age', 22)
print(K) #{'name': 'Anubhav'}

print(d1 is K)
# false means a new dictionary is created

print(d2 is K)
#True means d2 and K is same

# Sumarry is fromKays, get, copy and clear use of it in your program 
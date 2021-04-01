# today we learn about in and iteration
# python in_and_iterations.py
user_info={
    'name':'Anubhav',
    'age'  :'22',
    'fav_movie':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale']
    } 

    # check if key exist inn dictionary
# if 'name' in user_info:
#         print('present')
# else:
#          print('Not present')


# loops in dictionary 
# for i in user_info:
#     print(i)
# it only  print some number of elemennt 
 
#  but if we want to ptrint value than what '

# for i in user_info.values():
#     print(i)
    # it represent the value of the dictionary
 

#  values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

#  but here you use it like list 

# learn new technique to print it
for i in  user_info:
    print(user_info[i])# it work similar like values 

    # *** use 'in' or 'values' to print values

    # ****item method
#    we see how it works

    user_items=user_info.items()
    print(user_items)
    print(type(user_items))    # it make a dictionary as a tuple there we can perform any operation

    # return dict as a tuple

    #  now we see why we use it

    









# check if value exist is dictionary
# if 24 in user_info:
#         print('present')
# else:
#          print('Not present')
 

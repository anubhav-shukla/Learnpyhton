# add and delete data
# python add_delete_data.py
user_info={
    'name' : 'Anubhav',
    'age'  : 22,
    'fav_movie':'intelligence',
    'fav_book' : 'the intelligent investor'
}

# how to add data
user_info['fav_song']=['song1','song2']
print(user_info)

# pop method

popped = user_info.pop('fav_movie')
print(f"popped item is {popped}")


# popitem method

popped_item=user_info.popitem()
print(type(popped_item))
print(user_info)
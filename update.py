#  here we see how work update method
# python update.py
user_info={
    'name' : 'Anubhav',
    'age'  : 22,
    'fav_movie':'intelligence',
    'fav_book' : 'the intelligent investor'
}

# we make a second list
user_address=dict(town="ghaziabad",state="uttar pradesh",region="NCR")

#  see how update work

# user_info.update(user_address)
# print(user_info)


# it is the output of the dict
# {'name': 'Anubhav', 'age': 22, 'fav_movie': 'intelligence', 'fav_book': 'the intelligent investor', 'town': 'ghaziabad', 'state': 'uttar pradesh', 'region': 'NCR'}


# what happens when same key appear in both dict
user_address=dict(name="Anubhav Shukla",town="ghaziabad",state="uttar pradesh",region="NCR")
user_info.update(user_address)

# name  :'Anubhav shukla'
# here name is update 'Anubhav shukla'
# {'name': 'Anubhav Shukla', 'age': 22, 'fav_movie': 'intelligence', 'fav_book': 'the intelligent investor', 'town': 'ghaziabad', 'state': 'uttar pradesh', 'region': 'NCR'}


# a more condition if  dict is {} empty

user_info.update({})
print(user_info)

# output is :
        #    {'name': 'Anubhav', 'age': 22, 'fav_movie': 'intelligence', 'fav_book': 'the intelligent investor'}


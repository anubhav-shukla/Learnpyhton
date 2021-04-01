# make a dictionary take input from user
#python chapter7_exe2.py 


user_info={}
name=input('what is your name: ')
age=input('What is your age: ')
fav_movies= input('your fav_movies seprated by comma').split(',')
fav_songs=input('Your fav song seprated by comma').split(',')

user_info['name']=name
user_info['age']=age
user_info['fav_movies']=fav_movies
user_info['fav_songs']=fav_songs


for key,value in user_info.items():
    print(f"{key}:{value}")


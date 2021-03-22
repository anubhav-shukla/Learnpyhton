# we take input from user
# ask user name and age
# if user name start from 'A' and 'a'
# print 'You can watch coco movie'
# else print : ''Sorry you can not watch coco'

# python exercise2.py

name=input('Enter you name: ')
age = int(input('Enter  your age: '))
a=name.lower()
if a[0]=='a' and age>=10:
    print('You can watch coco movie')
else:
    print("Sorry , you can't watch coco movie")  
    #python exercise2.py
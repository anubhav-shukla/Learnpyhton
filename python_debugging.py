import pdb # import pdb module

#want definition and other stuff than you simply google it..

# We understand step of debugging
# 1.) set trace
#  2.) execute code line by line



#  1. you can do manually by comment program and after uncomment one by one

# using module pdb

pdb.set_trace()
name= input('Please type your name : ')
age = input('please type your age: ')
print(f'hello {name} your age is {age}')
# age2 =age +5 #here error is string(age) can't cancatenate with int(5)
age2=int(age)+5
print(f'{name} you will be {age2} in next five years')

# after completed debugging to run your program enter 'c'

# we use three commands :
            # l
            # c- continue
            # q - quit

# you can put it annywhere in the program..


# it is done now


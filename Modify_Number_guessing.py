# Modify Number Guessing Game

import random
num = int(input('Enter a number: '))
m=1
wining_number = random.randint(1, 100)
correct = False

while not correct:
    if num == wining_number:
         print(f'MAtched ! You Win,  you Guess it {m} times ')
         correct = True
    else:
       if num < wining_number:
          print('Too low ')
          m += 1
          num = int(input('guess Again: '))
       else:
            print('Too high')
            m += 1
            num = int(input('guess Again: '))
      
# python Modify_Number_guessing.py 

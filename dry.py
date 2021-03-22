# Modify Number Guessing Game
# usiing dry principlr 

# D-Don't
# R-Repeat
# Y-Yourself

import random
# num = int(input('Enter a number: '))
m=1
wining_number = random.randint(1, 100)
# correct = False DRy

while True: #not correct
    num = int(input('Enter a number: ')) # it is a change 
    if num == wining_number:
        print(f'MAtched ! You Win,  you Guess it {m} times ')
        break  #result is same
    else:
       if num < wining_number:
          print('Too low ')
        #   m += 1
        #   num = int(input('guess Again: '))
       else:
            print('Too high')
            # m += 1                               #we are use it 2 places
            # num = int(input('guess Again: '))
    m += 1
    continue # num = int(input('guess Again: ')) #result is same After use dry principle
# python Modify_Number_guessing.py 

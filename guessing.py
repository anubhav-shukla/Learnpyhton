# it is  while loop program
# python guessing.py
print("It is a guessing game")
import random
random_number =random.randrange(1,10)
guess=int(input("what could be tthe Number? "))
correct=False
print(random_number)
while not correct:
   if guess==random_number:
       print("congrats you got it")
       correct=True
   elif guess>random_number:
        print("too high")
        break
   elif guess<random_number:
       print("too low")     
       break
else:
        print("try something else")

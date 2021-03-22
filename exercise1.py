# Hope you play and win it
print("::::::::::::::::::Game of guessing a Number::::::::::::::::")
import random
random_number=random.randrange(1,10)
guessing_number=int(input("Enter a number  between 1 to 10 : "))

if random_number==guessing_number:
    print("You Win !!! random number is Matched "+str(random_number))

elif guessing_number>=random_number:
    print("Too high random number is "+str(random_number))  
elif guessing_number<=random_number:
    print("Too low random number is "+str(random_number))

    # python exercise1.py
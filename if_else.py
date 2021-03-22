# Syntax
#    if condition:
#          statement
#    else:
#        statement  

Name,age=input("Enter your  name and age: ").split(" ")
if int(age) >=14:
    print("Welcome ,your name is "+Name +" Your age is"+age)
else:
    print("You are not able to enter")    
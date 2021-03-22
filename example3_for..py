# take  input from user
# name is Anubhav
# A : 2
# n : 1
# u : 1
# b : 1
# h : 1
# v : 1

name = input(" Enter your Name: ")
temp_var= ""
for i in range(0,len(name)):
    if name[0] not in temp_var:
      
       print(f"{name[i]} : {name.count(name[i])}")
       temp_var += name
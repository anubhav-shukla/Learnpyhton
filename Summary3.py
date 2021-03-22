# if statement
# python Summary3.py
name=input("Enter your name: ")
if name=="Anubhav" or name=='anubhav':
    print('You are anubhav')
elif name =="Mohit" or name=="mohit":
    print("You are mohit")
else:
    print("You are not harshit or mohit")    

#    while

i=0
while i<10:
    print(i)
    i+=1

#  for loop  break and continue  #  
for i in range (1,11):
    if i==5:
        break
    print(i)

# continue
for i in range(1,11):
    if i==5:
        continue
    print(i)

# for with string

for i in "Anubhav":
    print(i)

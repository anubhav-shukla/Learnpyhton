#  problem 
# take 2 input more than one digit
# calculate it 
#python exercise3.py

num =input(' Enter more  than one number : ')
total = 0
i= 0
while i<=len(num)-1:
    total += int(num[i])
    i += 1
    print(total)



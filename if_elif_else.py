# python if_elif_else.py

#show  ticket  pricing
# 1 to 3 (free)
# 4 to 20(150)
# 11 to 60(250)
# above 60(200)

age = input("please Ennter  your age :")
age=int(age)
if age<=0:
    print('You can not watch')
elif age<=3 :
    print('Ticket price : Free')
elif 3<age<=10:
    print('Ticket price : 150')
elif 10<age<=60:
    print('Ticket price : 250')
else:
    print('TIcket price : 200')            

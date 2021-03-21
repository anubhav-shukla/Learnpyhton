#  make a function take 2 input and find greater number
#python  exercese_ch4.py
def greater_num(a,b):
     if a>b:
       return "first is Greater"
     return "second is greater"

num1=int(input("Enter first number : "))       
num2=int(input("Enter second number: "))
print(greater_num(num1,num2))
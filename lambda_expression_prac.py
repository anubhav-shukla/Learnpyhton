# lambda expression practice

# def is_even(a):
#     return a%2==0 #get same output
    # if a%2==0:
    #     return True
#     # return False
# print(is_even(5))   

# # now we use lambda expression

# is_even1=lambda a:a%2==0
# print(is_even1(8)) #true

# def last_char(s):
#     return s[-1]

last_char=lambda s:s[-1]  
print(last_char('golu'))  #output is u

# Lambda with if , else
def func(a):
    if len(a)>5:
        return True
    return False

  #Use lambda function

length=lambda l: True if len(l)>5 else False
print(length('anu'))

# do same work without if else
leng =lambda l: len(l)>5
print(leng('Shukla'))

# Hope now it is clear




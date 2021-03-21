# function practice with anubhav
# python func_prac.py
def inp_name(a):
    return a
print(inp_name("Anubhav")) 
      
#  just for result input as string

# def odd_even(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "odd"

# print(odd_even(19))          

def odd_even(a):
    if a%2==0:
        return "Even"
    
    return "odd"

print(odd_even(19))          

# is_even()
def is_even(num):
    return num%2 == 0 
print(is_even(10))

    # it return true

    
    # What is parameter?
    # is_even(num) num is a parameter
    # what is argument?
    # when we call a function is_even(10) here 10 is a argument

    # we can define null parameter function

def song():
    return"Happy Birthday song"

print(song())   
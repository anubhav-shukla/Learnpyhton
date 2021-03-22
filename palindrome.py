#  here  we make a program to check it palindrome or not
# python palindrome.py
def is_palindrome(a):
    rev = a[::-1]
    if a==rev:
        return a 
    else:
        return "Input is not"
print(is_palindrome("anubhav")+" a palindrome") 

        #Let's see a optimization solution
def palindrome(word):
    if word==word[::-1]:
        return True
    return False

print(palindrome("naman"))      
# output is true

#  see more optimize progrm

def palindrome1(word):
    return word==word[::-1]
print(palindrome1("anubhav")) 
# output is false
# hope now it is clear 

         
    

# generators

# generators are iterators

# Notes:
     #when you run iterable than it first convert in itrator than give result
        #  use of iterable is: list , tuple , dictionary
    #  but if you run iterator than it gives result #
           #it use in : map() and other function or methods

# Generator :
    #it's sequence but not iterable , it is iterator

# why use generator?:
                 #memory (--it save your memory----) 
                 #   use same place 
                 #   enhance performance
 #if you want to perform some functionlity multiple times than you use list
 # you want use only one time than you must use generator
                 
               # ******NOW WRITE GENERATOR*******
      # You can use two way for it:
                          # Generator function
                          # Generator comprehension


#Generator function

def nums(a):
    for i in range(1,a+1):
        yield(i) #for create generator we use yield
number=nums(10)

for nums in number:

      print(nums)     #it give result

# only use generator when we want only one time use it

for nums in number:

      print(nums)  #not show result because element removed
      
# memory ------> 
             

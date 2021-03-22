# ask a user for name
# Example - Anubhav shukla
# print count of each number
# output:
       #   A : 3
       #   n : 1 
       #   u : 2
       #   b : 1
       #   h : 2
       #   v : 1
       #   u : 1
       #   k : 1
       #   l : 1
       #    : 1
# python exercise4.py
name=input('Enter your whole name: ') #First take input
temp_var = "" #it is a variable here we store value that count one time
i = 0 # it ia variable
while i < len(name): # start here while loop for i to 10(for above example)
       if name[i] not in temp_var: #here we use if statement and not in 
              temp_var += name[i] # here we store name[i] value in temp_var
              print(f"{name[i]} : {name.count(name[i])}") #now print here
       i += 1 #here is increment 
     
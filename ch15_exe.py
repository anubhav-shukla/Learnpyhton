# exercise:
# define generator function
# take one number as argument
# generate a sequence of evem  numbers from 1 to that number

def gen_even(l):
    
    for i in range(1,l+1):
        if i%2==0:
         yield(i)
for i in gen_even(5):
    print(i)        

for i in gen_even(5):
    print(i)    

for i in gen_even(5):
    print(i)    

    #  you can generate it multiple time


# if :
num =gen_even(10) 
for i in num:
    print(i)      

for i in num:
    print(i)      
    #  see you not able to print it  


    # HACK******: #now you print it multiple time
for i in gen_even(10):
    print(i)      

for i in gen_even(15):
    print(i)      
    # print(i)      

# it is the solutiom ....


# **** attention ***:
               # if you generate sequence one time than you can't generate

            #    but if not than you can use it 


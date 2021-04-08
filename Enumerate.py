# We use enumerate function with for loop to 
# Track posision of our Item in iterable


# How we can do this without enumerate function
names=['abc','abcdef','Anubhav']
pos=0
for  i in names:
    print(f"{pos}---->{i}")
    pos +=1
    
#with enumerate function
for pos, name in enumerate(names):
    print(f"{pos}-------->{name}") 
    #get same output



# Define a function that take two arguments
# 1.) list containing string 
# 2.) string that want to find in your list
def two_arg(l,s):
    pos=0
    for pos,i in enumerate(l):
        if i== s:
            return pos
        
    return -1
        
print(two_arg(names,"Abc"))           


# Hope enumerate() is clear


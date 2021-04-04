# num to string
# define a function

# input -------->[True,False.[1,2,3],1,1.0,3]
# output -----> ['1','1.0','3']

# l=[True,False,[1,2,3],1,1.0,3]
def num_str(l):
    string=[]
    for i in l:
        if type(i)== int or type(i)== float:
            string.append(str(i))
    return string
print(num_str([True,False,[1,2,3],1,1.0,3]))    

# now see comprehensive way

def num_to_string(l):
    return[str(i) for i in l if type(i) == int or type(i) == float]
print(num_to_string([True,False,[1,2,3],1,1.0,3]))    

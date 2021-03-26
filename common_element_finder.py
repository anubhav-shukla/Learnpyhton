# common element finder 
# python common_element_finder.py
a=list(map(int,input("\n Enter the Numbers for 1st list: ").strip().split())) 
b=list(map(int,input("\n Enter the Numbers for 2nd list: ").strip().split())) 
def common_element(l,m):
    common=[]
    for i in l:
        if i in m:
         common.append(i)
    return common
print(common_element(a,b))        
    
# here we reverse any list using pop and append
# python chapter5_exe2.py
def reverse_list(l):
    reverse=[]
    for i in l:
        j=l.pop()
        reverse.append(j)
    return reverse
list2=list(range(1,13))
print(reverse_list(list2))        



# here we take input as list and reverse each element
# python chapter5_exe3.py
def reverse_all(l):
    reverse=[]
    for i in l:
        reverse.append(i[::-1])
    return reverse

listj=['mango','apple','banana']
print(reverse_all(listj))    

# def a function
name=['anubhav','golu']

# print(func(names))
# print(func(names,reverse-str=true))

def reverse_str(l,**kwargs):
    if kwargs.get('reverse_st')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
print(reverse_str(name,reverse_st = True))            
    
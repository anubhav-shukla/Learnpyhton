# kwargs (kayword argument)
# **kwargs (double star operator)

# it print argument as ****dictionary

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(first_name='Anubhav',last_name='Shukla')   #it give output as dictionary

# now run a loop in the dictionary 
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
func(first_name='Anubhav',last_name='Shukla')   #it give output as dictionary

# pass two parametre
# def func(name,**kwargs):
#     print(kwargs)
#     print(name)#golu
#     print(type(kwargs))
# func('Golu',first_name='Anubhav',last_name='Shukla')   #it give output as dictionary

# unpacking in dictionary

d={'name':'Anubhav','age':22}
func(**d)



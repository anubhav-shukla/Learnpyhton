# functions with all parameters
# very important to understand

# PADK

#|# parametres #simple parametres
#|# *args #we understand it
#|# default parametre #when we not give any input that it print by default something
#|# **kwargs # we understand it/..

# it is the order to use parametre


def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Anubhv',1,2,3, a=1,b=2)    #it give correct result

# keep in mind while using all in your software and programs





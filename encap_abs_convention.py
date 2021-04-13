# we talk about :
# encapsulation #we store useful data at one place and after use it when required
# abstraction # it is use for hide  data from user
# some special naming convention
# name mangling


class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=price
    def make_a_call(self,phonr_number):
        print(f"callin{phonr_number}....")
    def full_name(self):
        return f"{self.brand}{self.model_name}"

l=[1,6,3,2,9]
l.sort() #python use tim sort algorithm to sort a list,tuple and dictionary
print(l)   #here sort is like a encapsulation of list class

# now we understand 
# we use a api for chat..
    #   who chat through this application he/she not know what happen in background , he only use service


# Naming convention:-

# _name :- it is a convetion for private name,like instance variable
# but in python everything is public
# __name__ :- dunder/magic method  , Like __init__

# Name mangling:
       # __price()
phone1=Phone('Nokia','1100',1000)
# print(phone1.price) 

# now use __price()
# print(phone1.__price)  #it show error

print(phone1.__dict__)
    #   {'brand': 'Nokia', 'model_name': '1100', '_Phone__price': 1000}
    # see name is automatically change
print(phone1._Phone__price)    
# _Phone__price is not private
# python only change the name

# see hoe we can change it
phone1._Phonr__price=-1000
print(phone1._Phonr__price)

# see hope it is clear noe...
# special magic method/dunder methods  start__ and end with __
# operator overloading
# polymorphism  #operator overloading is an example of polymorphism
              # method overriding is an example of polymorphism

class Phone:
    def __init__(self,brand,model,price):
        # super().__init__()
        self.brand=brand
        self.model=model
        self.price=price
    def phone_name(self):
        return f"{self.brand} {self.model}"  

# l=[1,2,3,4]
# print(len)

#  2 methods we can use :
# *str # it for common user
# repr - representation #it use by developer
def __repr__(self):
    return f'{self.brand} {self.price}'
def __str__(self):
    return f' {self.brand} {self.model_name} and price is{self.price} '  
my_phone=Phone('nokia','1100',1000)
print(str(my_phone))
print(repr(my_phone))

# operator overrloading

def __add__(self,other):
    return self.price + other.price #operator overrloading

#2+3=5
# 'abc'+'def'='abcdef'

# l=[1,2,3]
# print(len(l))
# t=(1,2,3)
# s='Anubhav'
# print(len(t))
# print(len(s))

my_phone=Phone('micromax','Lemon',1500)
my_phone2=Phone('ikall','2',999)
print(__add__(my_phone,my_phone2)) #it is example of overloading
# print(len(my_phone))


 #class SmartPhone(Phone):
 #     def __init__(self,brand,model,price,camera):
 #               
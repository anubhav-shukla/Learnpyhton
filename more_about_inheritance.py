# can we derive more than one class from base class
# multilevel inheritance  ********line:9-35  is multilevel inheritance
# method resolution order  
# method overriding
# isInstance(),issubclass()
 


class Phone: #base class,/parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price = max(price,0)
        # if we use  property decorator than we do't need to use as a function
    @property
    def complete_specification(self):
         return f"{self.brand } {self.model_name} and price {self.price}"

class SmartPhone(Phone): #derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
         super().__init__(brand,model_name,price)
         self.ram=ram
         self.internal_memory=internal_memory
         self.rear_camera=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is  {self.price}" #method override

class flagshipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is  {self.price} and front camera ={self.front_camera}" #method override

        # phone #Phone('nokia','1100',1000)
 
# phone=Phone('nokia','1100',1000)
smartphone=SmartPhone('onePlus','5',30000,'6GB','64GB','20mp')
oneplus=flagshipPhone('onePlus','5',30000,'6GB','64GB','20mp','16mp')
# print(oneplus.full_name())
# print(help(flagshipPhone))
# print(smartphone.full_name()+f" and price isc{smartphone.price}")

# isinstance
# print(isinstance(oneplus,SmartPhone)) #true
# print(isinstance(SmartPhone,Phone)) #false
# print(isinstance(oneplus,flagshipPhone)) #true

# issubclass()
print(issubclass(SmartPhone,Phone))#true
print(issubclass(SmartPhone,flagshipPhone))#false




# here we inherit class phone property and make a new class smartPhone
# In Inheritance we inherit the property of class phone 
# hope it help you ..


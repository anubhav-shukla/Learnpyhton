# we take previous 3xaple to understand
# this example is help you to understand inheritance 
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price = max(price,0)
        # if we use  property decorator than we do't need to use as a function
    @property
    def complete_specification(self):
         return f"{self.brand } {self.model_name} and price {self.price}"

        # Now use getter and setter
    # for getter
    @property    
    def  price(self):
        return self.price
    # setter
    def price(self,new_price):
        self.price=max(new_price,0)

    def make_a_call(self,phonr_number):
        print(f"callin{phonr_number}....")
    def full_name(self):
        return f"{self.brand}{self.model_name}"
class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
         super().__init__(brand,model_name,price)
         self.ram=ram
         self.internal_memory=internal_memory
         self.rear_camera=rear_camera

phone=Phone('nokia','1100',1000)
smartphone=SmartPhone('onePlus','5',3000,'6GB','64GB','20mp')
print(phone.full_name())
print(smartphone.full_name()+f" and price isc{smartphone.price}")

# here we inherit class phone property and make a new class smartPhone
# In Inheritance we inherit the property of class phone 
# hope it help you ..


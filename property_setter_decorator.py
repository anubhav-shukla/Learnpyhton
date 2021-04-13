# property, setter .decorator

# use getter : property decorator
# use setter : setter decorator

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

phone1=Phone('Nokia','1100',1000)
print(phone1.brand)
print(phone1.model_name)
phone1.price=1100
print(phone1.price)
print(phone1.complete_specification)#we use property decorator @property 

# hope it clear now........
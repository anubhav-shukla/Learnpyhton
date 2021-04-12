# discount on product

#  we take previous code of laptop


class laptop:
    discount_percent=10
    def __init__(self,brand_name,model_name,price):
        self.Q_brand_name=brand_name
        self.Q_model_name = model_name
        self.R_Price=price
        self.laptop_name_model=brand_name+' '+model_name #you can combine two instance variable
    def discount_calc(self):
        percentage=(self.discount_percent/100)*self.R_Price
        actual_price=self.R_Price-percentage
        return actual_price


laptop1=laptop('Hp','au114x ',38000)
laptop2=laptop('Lenovo','Yoga Series',45000)
laptop3=laptop('apple','macbook pro',230000)
laptop3.discount_percent=50
print(laptop3.__dict__)
print(laptop3.discount_calc())

# print(laptop1.laptop_name_model,laptop1.R_Price)
# print(laptop2.Q_brand_name,laptop2.Q_model_name,laptop2.R_Price)
# print(f"After discount price is laptop brand {laptop1.laptop_name_model}{laptop1.discount_calc(15)}")
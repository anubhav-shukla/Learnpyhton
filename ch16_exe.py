# create a  laptop class with attributes like brand name , model name , price
# create two objects/instance of your laptop class

class laptop:
    def __init__(self,brand_name,model_name,price):
        self.Q_brand_name=brand_name
        self.Q_model_name = model_name
        self.R_Price=price
        self.laptop_name_model=brand_name+' '+model_name #you can combine two instance variable
laptop1=laptop('Hp','au114x',38000)
laptop2=laptop('Lenovo','Yoga Series',45000)

print(laptop1.laptop_name_model,laptop1.R_Price)
print(laptop2.Q_brand_name,laptop2.Q_model_name,laptop2.R_Price)

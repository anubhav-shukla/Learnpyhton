
class mobile:
    def __init__(self,name):
        self.name=name
class mobileStore:
    def __init__(self):
        self.mobiles=[]
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,mobile):
           self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class')
oneplus=mobile('one plus 6')
samsung='samsung galaxy s8'
moboStore=mobileStore()

# print(mobostore.mobiles)
moboStore.add_mobile(oneplus)
mobophones=moboStore.mobiles
print(mobophones[0].name)

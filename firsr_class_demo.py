# let's create a class
# init method ,#other programming called constructor
class Person:
    def __init__(self, first_name,last_name,age):
        # self -------- Convention 
        # you can write anything in place of self but everywhere same
        # verify
        print('init method / constructor get called')
        # instance variables
        self.first_name=first_name #it is not mandatory write same name first_name=first_name
        # write like person_first_name-d=firstname  #it is a instance variable
        self.last_name=last_name
        self.age=age
p1=Person('ANubhav','Shukla',22)
p2=Person('Ashish','Shukla',24)
print(p1.first_name)
print(p2.first_name)


# hope now it is clear

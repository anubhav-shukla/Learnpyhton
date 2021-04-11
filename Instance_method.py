# instance methods
l=[1,2,3] #l is a instance(object) of list class
l.pop() #pop is a method
# method is pre define in the class

# here , self is a object 
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
     
       return f"{self.first_name}{self.last_name}"
    
     # we make a method age_above()
    def age_18(self):
        return self.age>18


p1=Person('Anubhav',' Shukla',22)
p2=Person('Anubhav',' Shukla',10)

print(p1.full_name()) 
# What happen when write it 
print(Person.full_name(p1)) #internal process after call

print(p1.age_18())    #true
print(p2.age_18())    #false

l=[1,3,5]
# use clear,pop
# l.clear()

# print(l) #[]
# list.clear(l)
# print(l) #[]

# l.append(10)
list.append(l,10) #background process
# it is the  importance of self ..
print(l)





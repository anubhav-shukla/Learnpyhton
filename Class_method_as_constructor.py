# class method use as a constructor
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 # class method
# we use less time of class method

class Person:
     count_instance=0 #class variable or  attribute
     def __init__(self,first_name,last_name,age):
          Person.count_instance+=1
          self.first_name=first_name
          self.last_name=last_name
          self.age=age

     @classmethod
     def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
 
# first argument is class
     @classmethod 
     def count_instances(cls):
         return f"you have created {cls.count_instance} instances of {cls.__name__} class" 

     def full_name(self):
         return f"{self.first_name}{self.last_name}"
     
p1=Person('Anubhav','shukla',22)
p2=Person('GOlU','shukla',22)
p3=Person('Ashish ','SHukla',24)
print(p1.count_instances())

# from string function use like a constructor

p4=Person.from_string('Anubhav ,Shukla,22')
print(p4.full_name())

# hope you understand how to create it

# 'You have  created 4 instances of person class'
 
            # hope it is clear
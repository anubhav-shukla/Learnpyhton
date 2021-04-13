# it has no connection to instance and object
# it is like a normal function
# but it logically connected with class

class Person:
     count_instance=0 #class variable or  attribute
     def __init__(self,first_name,last_name,age):
          Person.count_instance+=1
          self.first_name=first_name
          self.last_name=last_name
          self.age=age

# first we use @staticmethod Decorator
     @staticmethod
     def hello():
       print('Hello , it is a static method')
Person.hello()
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 # class method
# we use less time of class method

class Person:
     count_instance=0 #class variable or  attribute
     def __init__(self,first_name,last_name,age):
          Person.count_instance+=1
          self.first_name=first_name
          self.last_name=last_name
          self.age=age
# first argument is class
# classMethod :
def  count_instance(clsd):
    return f"you have created {clsd.count_instance} instances of {clsd.__name__}" 


p1=Person('Anubhav','shukla',22)
p2=Person('GOlU','shukla',22)

print(Person.count_instance)

# 'You have  created 4 instances of person class'
 
            # hope it is clear
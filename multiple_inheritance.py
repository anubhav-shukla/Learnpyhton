# multiple inheritance

class A:
    def class_a_method(self):
        return 'I\'m just a class A method'
    def hello(self):
        return 'hello from class A'
# instance_a=A()

# print(instance_a.class_a_method())
class B:
    def class_b_method(self):
        return 'I\'m just a class B method'
    def hello(self):
        return 'hello from class B'

class c(B,A): #if you change the order of passing than you get result as passing
    pass
instance_c=c()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c
.hello())
# print(c.mro()) #mro function
print(c.__mro__)
# raise error 1
# NotImplementedError
# Abstract method is NotImplementedError 

class Animal:
    def __init__(self):
        self.name=name
    def sounf(self):
        raise NotImplementedError("You have to define this method in subclass")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)  
        self.breed=breed

    def sound(self):
        return 'bhow bhow'    
class cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)  
        self.breed=breed

    def sound(self):
        return 'meao meao'

doggy=Dog('boony','pug')
print(doggy.sound)            
        
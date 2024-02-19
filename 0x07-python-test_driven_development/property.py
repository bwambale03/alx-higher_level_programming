#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """the getter method for the name property"""
        print("Getting name!")
        return self._name
    
    @name.setter
    def name(self, value):
        print(f"Seetting th value to/l: {value}")
        self.value = value
        
    @name.deleter
    def deleter(self):
        print("Deleting name!")
        del self._name
        
# creating an instance of a person
p = Person("John")

# accessing the name property invokes the getter
print(p.name)

# setting a value to the name property invokes the setter
p.name = 'Dave'  # settig name to Dave

del p.name  # Deleting name

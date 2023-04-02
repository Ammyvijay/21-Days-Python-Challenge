"""
Note : Class Variable 

In Python, a class is a blueprint for creating objects, and each object that is created from a class is called an instance.

Class variables are variables that are defined within the class, but outside of any method, and are shared across all instances of that class. Some use cases for class variables include: Defining constants, storing configuration data, keeping track of counts, and sharing data between instances.
"""

class Car:
    num_wheels = 4

    def __init__(self,make,model):
        self.make = make
        self.model = model

car1 = Car("Toyoto","Camry")
car2 = Car("Honda","Civic")

print(car1.num_wheels)
print(car2.num_wheels)
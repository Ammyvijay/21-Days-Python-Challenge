"""
Note : 

magic methods in Python are special methods that are used to define how objects of a class behave in different situations. These methods have names that start and end with double underscores, such as __init__, __str__, or __eq__. These methods are called automatically by Python when certain operations are performed on objects of a class.

For example, the init method is a special method in Python that is used to initialize an object's attributes when it is created. It is called automatically when an object is instantiated from a class and is used to set default values for the object's attributes.
"""

class Person:

    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
person = Person("John",30)
print(person)
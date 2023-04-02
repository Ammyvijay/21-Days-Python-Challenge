"""
Note : Classmethod

In Python, a class method is a method that is bound to the class and not the instance of the class. Class methods are defined using the @classmethod decorator and take the class itself as the first argument, conventionally named cls. Unlike instance methods that operate on the instance of the class, class methods operate on the class itself.

"""

import datatime

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls,name,birth_year):
        current_year = datatime.dataetime.now().year
        age = current_year - birth_year
        return cls(name,age)
    
person = Person.from_birth_year('John',1990)
print(person.age)
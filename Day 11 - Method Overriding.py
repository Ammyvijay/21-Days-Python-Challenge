"""
Note : Method overriding is a concept in Object-Oriented Programming where a child class provides a different implementation for a method that is already defined in the parent class. In Python, method overriding is achieved by defining a method with the same name in the child class as the one in the parent class.

Method overriding in Python allows for customizing the behavior of a method for a specific class, promoting code reusability and polymorphism.
"""

class Data:
    def __init__(self,data) -> None:
        self.data = data

    def summary(self):
        print("Data SUmmary")

class DataFrame(Data):

    def __init__(self,data) -> None:
        super().__init__(data)
    
    def summary(self):
        print("Dataframe Summary")
        print(self.data.describe())


"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows for the creation of new classes based on existing classes.

Inheritance enables a new class to inherit the attributes and methods of an existing class, which can then be modified or extended to create a new class with specific features or behaviors. Inheritance is a powerful concept that promotes code reuse, modularity, and flexibility in Python.
"""

from typing import List

class Data:

    def __init__(self,name:str) -> None:
        self.name = name
        self.data: List[int]=[]

    def add_data(self,data:int)->None:
        self.data.append(data)
    
    def describe(self)->None:
        print(f"This is {self.name} data.")

class SalesData(Data):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def average_sale(self)->float:
        return sum(self.data)/len(self.data)
    
sales_data = SalesData("Sales")
sales_data.add_data(100)
sales_data.add_data(200)
sales_data.add_data(300)

sales_data.describe() # Output: This is Sales data
print(sales_data.average_sale())
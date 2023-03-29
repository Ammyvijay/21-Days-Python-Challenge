"""
Notes :
In Python, methods are functions that are defined within a class and operate on instances of that class. They allow for specific actions to be performed on the attributes of an instance.
Methods are an essential tool for Python developers and offer a number of benefits in terms of code organization, reusability, consistency, and functionality.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    name:str
    salary:int

class EmployeeDataset:

    def __init__(self,employee_list:List[Employee]) -> None:
        self.employee_list = employee_list

    # Define a method to perform a certain action
    def calculate_average_salary(self)->float:
        total_salary = 0
        for employee in self.employee_list:
            total_salary+=employee.salary
        return total_salary/len(self.employee_list)
    
employee_list = [
    Employee('John',50000),
    Employee('Jane',60000),
    Employee('Bob',45000),
]

dataset = EmployeeDataset(employee_list)
average_salary = dataset.calculate_average_salary()

print(f"The Average salary of the employees is ${average_salary:.2f}")
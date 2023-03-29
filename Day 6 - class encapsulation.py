"""
Note :

Encapsulation is a core concept in object-oriented programming (OOP) that helps us to keep variables and methods private within a class.

In Python, encapsulation is achieved through naming conventions, where variables and methods that should not be accessed from outside the class are prefixed with underscores. Encapsulation helps to ensure that data is accessed and modified in a controlled way, reducing the risk of errors.
"""

class Customer:

    def __init__(self,name:str,email:str) -> None:
        self.name = name
        self.__email = email
    
    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self,new_email:str)->None:
        self.__email = new_email

cus = Customer("Abcd","ammyvijay.b@gmail.com")
print(dir(cus))
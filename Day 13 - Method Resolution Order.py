"""
Note :

Method Resolution Order (MRO) is a concept in Python that determines the order in which methods are searched for in a hierarchy of classes. 
When a method is called on an object, Python searches for the method in the class of the object, and then in its parent classes, following the MRO. 
This allows for multiple inheritance and method overriding, where a subclass can override a method defined in a parent class.
In the example, we create an instance of D and call its greet method, the method resolution order determines that the greet method of B is called first, followed by the greet method of C, and then the greet method of A.
"""

class A:

    def greet(self):
        print("Hello from A")

class B(A):

    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):

    def greet(self):
        print("Hello from C")
        super().greet()

class D(B,C):
    def greet(self):
        print("Ok")
        return super().greet()

d= D()
d.greet()
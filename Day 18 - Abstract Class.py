"""
Note : Abstract Classes in Python are classes that cannot be instantiated but are meant to be inherited. They contain one or more abstract methods, which are methods that are declared but not implemented.

The benefits of using abstract classes in Python include:
1. Encourages code reuse and modularity by creating a hierarchy of related classes.
2. Provides a clear contract for any classes that inherit from the abstract class, ensuring that they implement the required methods.
3. Helps to enforce consistent behavior across related classes.
4. Makes it easier to add new classes that fit into the existing hierarchy. 
"""

from abc import ABC, abstractmethod

class DataProcessor(ABC):

    @abstractmethod
    def load_data(self,path):
        pass

    @abstractmethod
    def process_data(self,data):
        pass
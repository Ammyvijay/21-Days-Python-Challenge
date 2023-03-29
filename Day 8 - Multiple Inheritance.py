"""
Multiple inheritance in Python allows a class to inherit attributes and methods from multiple parent classes. This means that a child class can have the properties of multiple classes, which can be useful in situations where a class needs to inherit behavior from different sources.

The benefits of using multiple inheritance include code reusability, flexibility in design, and the ability to create complex hierarchies of classes. However, it is important to use multiple inheritance judiciously and avoid creating complicated and confusing class hierarchies.
"""

class DataProcessor:
    def process_data(self)->None:
        pass

class Plotter:
    def plot_data(self)->None:
        pass

class DataPlotter(DataProcessor,Plotter):
    def plot_processed_data(self)->None:
        self.process_data()
        self.plot_data()
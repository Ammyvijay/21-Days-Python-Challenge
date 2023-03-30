"""
Note: In Python, the super() function is used to call a method in the parent class from a child class. It provides a way to access inherited methods that have been overridden in a subclass. 

For instance, if a child class inherits from a parent class and wants to call a method defined in the parent class, the super() function can be used to accomplish this.

Using super() in Python helps to reduce duplication of code and allows for better inheritance of functionality across classes.
"""

class DataSource:

    def __init__(self,file_path) -> None:
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path,'r') as f:
            data = f.read()
        return data
    
class CsvDataSource(DataSource):

    def __init__(self, file_path,delimiter=",") -> None:
        super().__init__(file_path)
        self.delimiter = delimiter

    def read_data(self):
        with open(self.file_path,'r') as f:
            data = f.read().split('\n')
        return [line.split(self.delimiter) for line in data]


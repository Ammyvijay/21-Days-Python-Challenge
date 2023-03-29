"""
Note :

Polymorphism in Python is the ability of objects of different classes to be used interchangeably. This means that objects with different types can be used in a single code block, resulting in simpler and more flexible code.

Using polymorphism allows for increased code flexibility and reusability, simplified code maintenance, and reduced code duplication. 
"""

import json

class DataReader:

    def __init__(self,filename) -> None:
        self.filename = filename
    
    def read_data(self):
        pass

class CsvReader(DataReader):

    def read_data(self):
        with open(self.filename,'r') as f:
            data = [line.strip().split(',') for line in f]
        return data
    
class JsonReader(DataReader):

    def read_data(self):
        with open(self.filename,'r') as f:
            data = json.load(f)
        return data
    
def process_data(reader):
    data = reader.read_data()
    # Process the data here...
    print(f"Data processed from {reader.filename}.")

csv_read = CsvReader("data.csv")
json_data = JsonReader("data.json")

process_data(csv_read)
process_data(json_data)
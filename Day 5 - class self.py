"""
Note :

In Python, "self" is a reference to the instance of a class. It's a way for objects to refer to themselves and interact with their own attributes and methods. When we create an instance of a class, Python automatically passes that instance as the first argument to any method you call on that instance. By convention, this first argument is always named "self".

"""

from typing import List

class Dataset:

    def __init__(self,data:List[int]) -> None:
        self.data = data

    def mean(self)->float:
        return sum(self.data)/len(self.data)
    
data = [1,2,3]
dataset = Dataset(data)

print(f"Mean : {dataset.mean()}")
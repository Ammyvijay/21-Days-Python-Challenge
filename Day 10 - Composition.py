"""
Note:
composition in Python is the practice of creating complex objects by combining simpler objects. This technique allows for building objects with specific functionalities, where each object is responsible for a particular aspect of the overall functionality.

This approach avoids the potential conflicts and complexity of for example multiple inheritance, making the code easier to understand, maintain, and modify. It also enhances code reusability since the individual components can be used in various contexts. 
"""


class DataLoader:

    def __init__(self,filepath) -> None:
        self.filepath = filepath

    def load_data(self):
        pass

class DataProcessor:
    def preprocess(self,data):
        # Perform data preprocessing
        pass

class DataPipeline:

    def __init__(self,loader,processor) -> None:
        self.loader = loader
        self.processor = processor

    def run_pipeline(self):
        data = self.loader.load_data()
        processed_data=self.processor.preprocess(data)

loader = DataLoader('data.txt')
processor = DataProcessor()

pipleline = DataPipeline(loader,processor)
pipleline.run_pipeline()
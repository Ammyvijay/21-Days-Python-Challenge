"""

Notes :

In Python, a class is a blueprint for creating objects that can have attributes (variables) and methods (functions). Think of a class as a template that defines the characteristics and behaviors of an object. Once a class is defined, we can create objects (also known as instances) of that class, each with its own set of values for the attributes.

Using classes in Python can make our code more modular, reusable, reliable, flexible, and efficient. By leveraging these benefits, we can create more complex and sophisticated programs while minimizing errors and improving maintainability

"""

class DataPipeline:

    def __init__(self,input_path:str,output_path:str) -> None:
        self.input_path=input_path
        self.output_path=output_path

    def extract_data(self)->dict:
        # code to extract data from input_path
        print("Extracting Data")
        pass

    def transform_data(self,data:dict)->dict:
        # Code to transform data
        print("Transforming Data")
        pass

    def save_data(self,data:dict)->None:
        # Code to save transformed data to output_path
        print("Saving Data")
        pass

data_pipeline = DataPipeline("input.csv","output.csv")
raw_data = data_pipeline.extract_data()
transform_data = data_pipeline.transform_data(raw_data)
data_pipeline.save_data(transform_data)

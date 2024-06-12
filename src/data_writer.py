import json

from src.constants import DEFAULT_DATA_PATH

class DataWriter:
    def __init__(self, data: str):
        self.data = data

    def write(self, path: str, ):
        with open(f'{DEFAULT_DATA_PATH}/{path}', 'w', encoding='utf-8') as file:
            file.write(self.data)
            

class CSVDataWriter(DataWriter):    
    def __init__(self, data: str) -> None:
        super().__init__(data)
        

class JSONDataWriter(DataWriter):    
    def __init__(self, data: dict) -> None:
        super().__init__(json.dumps(data))
    

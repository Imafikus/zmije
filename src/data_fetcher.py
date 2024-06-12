
import requests

class DataFetcher:    
    def __init__(self, data_source: str) -> None:
        self.data_source = data_source
    
    def fetch_data(self) -> None:
        raise NotImplementedError("fetch_data method is not implemented")
    
class RandomUserDataFetcher(DataFetcher):
    
    def __init__(self) -> None:
        super().__init__("https://randomuser.me/api/")
    
    def fetch_data(self) -> dict:
        
        data = requests.get(self.data_source, timeout=20)
        
        return data.json()

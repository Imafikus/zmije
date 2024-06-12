
from src.data_fetcher import RandomUserDataFetcher
from src.data_writer import JSONDataWriter, CSVDataWriter
from src.models import RandomUserResponse

if __name__ == "__main__":
    data = RandomUserDataFetcher().fetch_data()
    
    parsed_data = RandomUserResponse.model_validate(data)
    
    result = parsed_data.results[0]
    
    JSONDataWriter(result.location.model_dump()).write('random_user_data.json')
    CSVDataWriter(str(result.login)).write('random_user_data.csv')
    
    
    
    
from abc import ABC, abstractmethod

class BaseFetcher(ABC):
    def __init__(self, config: dict):
        self.config = config
    
    @abstractmethod
    def get_forecast(self, zone):
        pass

    @abstractmethod
    def get_weather(self, zone):
        pass

    def get_source_name(self):
        return "Unknown"
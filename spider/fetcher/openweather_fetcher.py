import requests
from .base_fetcher import BaseFetcher

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

class OpenWeatherFetcher(BaseFetcher):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = config['api_key']
        self.units = config.get("units", "metric")
    
    def get_forecast(self, zone):
        params = {
            "lat": zone.lat,
            "lon": zone.lon,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(FORECAST_URL, params=params)
        return response.json()

    def get_weather(self, zone):
        params = {
            "lat": zone.lat,
            "lon": zone.lon,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(WEATHER_URL, params=params)
        return response.json()

    def get_source_name(self):
        return "openweather"
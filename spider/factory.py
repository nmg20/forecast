from .fetcher.openweather_fetcher import OpenWeatherFetcher

def get_fetcher(source_name, config):
    if source_name == "openweather":
        return OpenWeatherFetcher(config=config)
    else:
        raise ValueError(f"Fuente no soportada: {source_name}.")
from spider.zone import load_zones, Zone
from spider.factory import get_fetcher

import yaml
import os
import json

keys_path = "config/keys.yaml"
zones_path = "config/zones.yaml"

def main():
    with open(keys_path) as f:
        keys = yaml.safe_load(f)
    
    zones = load_zones(zones_path)
    source = "openweather"
    fetcher = get_fetcher(source, keys[source])

    os.makedirs("data", exist_ok=True)

    for zone in zones:
        print(f"Consultando {source} para {zone.name}")
        weather = fetcher.get_weather(zone)
        forecast = fetcher.get_forecast(zone)

        with open(f"data/{zone.id}_weather_{source}.json","w", encoding="utf-8") as f:
            f.write(json.dumps(weather))
        
        with open(f"data/{zone.id}_forecast_{source}.json","w", encoding="utf-8") as f:
            f.write(json.dumps(forecast))

if __name__ == "__main__":
    main()
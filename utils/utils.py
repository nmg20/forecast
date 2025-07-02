import pandas as pd
from datetime import datetime
import os

def save_json_forecast(data, zone_name):
    df = pd.json_normalize(data['list'])
    df['zone'] = zone_name
    os.makedirs('data', exist_ok=True)
    date = datetime.now().strftime("%Y%m%d_%H%M")
    df.to_csv(f"data/forecast_{zone_name}_{date}.csv", index=False)

def save_json_weather(data, zone_name):
    df = pd.json_normalize(data['list'])
    df['zone'] = zone_name
    os.makedirs('data', exist_ok=True)
    date = datetime.now().strftime("%Y%m%d_%H%M")
    df.to_csv(f"data/weather_{zone_name}_{date}.csv", index=False)

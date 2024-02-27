import requests
from dotenv import load_dotenv
import os

from weather import Weather

load_dotenv()

api_key = os.getenv("OPEN_WEATHER_API_KEY")
lat = 42.65416676939424
lon = 23.352346378642736

weather_api = Weather(api_key)
print(weather_api.get_weather(lat, lon))
